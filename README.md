# LangChain Confluence Explorer

## Overview
LangChain Confluence Explorer is an innovative tool designed to enhance the way we interact with technical documentation stored in Confluence. Built using Python and Streamlit, this application leverages the power of LangChain, a library for building language model chains, to provide an intuitive interface for querying and understanding complex documentation.

## Features
- **Confluence Integration**: Seamlessly fetches documents from Confluence for processing.
- **LangChain Integration**: Utilizes LangChain for efficient language processing and question answering.
- **FAISS Knowledge Base**: Employs FAISS (Facebook AI Similarity Search) to create a searchable knowledge base from Confluence documents.
- **OpenAI Embeddings**: Leverages OpenAI's embeddings to understand and process text data.
- **Session State Variables**: Uses Streamlit’s session state to maintain data across reruns, enhancing user experience and efficiency.
- **Interactive UI**: Streamlit-based interface for fetching data and querying the knowledge base.

## How It Works
1. **Fetching Confluence Data**: The application connects to a Confluence instance and fetches documents based on user input.
2. **Processing Data**: Text data from Confluence documents are split into manageable chunks and processed using OpenAI embeddings.
3. **Building the Knowledge Base**: A FAISS index is created from the processed chunks, forming a searchable knowledge base.
4. **User Interaction**: Users can input queries related to the fetched documents, and the application searches the knowledge base for relevant information.
5. **Displaying Answers**: The application displays the most relevant information from the knowledge base in response to user queries.

## Technologies Used
- **Python**: The core language used for development.
- **Streamlit**: For creating the web application.
- **LangChain**: For building language model chains.
- **Confluence API**: For fetching documentation from Confluence.
- **OpenAI Embeddings**: For text processing and embeddings.
- **FAISS (Facebook AI Similarity Search)**: For creating the searchable knowledge base.

## How to Run

1. Use python venv `python -m venv .venv` & `source .venv/bin/activate`
2. Install the dependencies `pip install -r requirements.txt`
3. Set the necessary environment variables using a `.env` file.
4. Run the Streamlit application using the command `streamlit run app.py`.


