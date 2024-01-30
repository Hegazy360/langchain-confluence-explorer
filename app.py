from dotenv import load_dotenv
import os
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
from langchain_community.callbacks import get_openai_callback
from langchain_community.document_loaders import ConfluenceLoader
from langsmith.run_helpers import traceable


def get_confluence_data():
    confluence_api_key = os.getenv('CONFLUENCE_API_KEY')
    confluence_username = os.getenv('CONFLUENCE_USERNAME')
    confluence_url = os.getenv('CONFLUENCE_URL')

    loader = ConfluenceLoader(
        url=confluence_url, username=confluence_username, api_key=confluence_api_key)

    documents = loader.load(
        space_key="KB", include_attachments=False, limit=5, max_pages=10
    )

    return documents

@traceable(run_type="embedding")
def set_document_embeddings(documents):
    for document in documents:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        st.session_state['chunks'].extend(
            text_splitter.split_text(document.page_content))

    if st.session_state['chunks']:
        embeddings = OpenAIEmbeddings()
        st.session_state['knowledge_base'] = FAISS.from_texts(
            st.session_state['chunks'], embeddings)


def main():
    # Load environment variables
    load_dotenv()

    st.set_page_config(page_title="LangChain Confluence Explorer")
    st.header("LangChain Confluence Explorer")

    if 'chunks' not in st.session_state:
        st.session_state['chunks'] = []
    if 'knowledge_base' not in st.session_state:
        st.session_state['knowledge_base'] = None

    if st.button("Fetch Confluence Data", type="primary"):
        documents = get_confluence_data()

        set_document_embeddings(documents)

    if st.session_state['knowledge_base'] is not None:
        user_question = st.text_input(
            "Ask a question about your Confluence space:")
        print(st.session_state['knowledge_base'])

        if user_question:
            print(user_question)
            docs = st.session_state['knowledge_base'].similarity_search(
                user_question)

            llm = OpenAI(temperature=0)
            chain = load_qa_chain(llm, chain_type="stuff")
            input_data = {"input_documents": docs, "question": user_question}

            with get_openai_callback() as cb:
                response = chain.invoke(input=input_data)
                print(cb)
                cb.total_cost = cb.total_cost.__round__(7)
                st.write(cb)

            st.write(response['output_text'])

# Run the main function
if __name__ == '__main__':
    main()
