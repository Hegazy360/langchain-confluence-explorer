# LangChain PDF Explorer

This project is a Streamlit application that allows users to upload a PDF, ask a question about the content of the PDF, and get an answer based on the content of the PDF. The application uses OpenAI to generate embeddings for the text in the PDF and to answer the user's question.

<img width="1000" alt="Screenshot 2024-01-26 at 14 20 13" src="https://github.com/Hegazy360/langchain-pdf-explorer/assets/13141632/d526c674-8340-483d-87be-b404e1aaa3a4">



## Dependencies

The project uses the following Python libraries:

- streamlit
- PyPDF2
- langchain
- OpenAI LLM

## How to Run

1. Use python venv `python -m venv .venv` & `source .venv/bin/activate`
2. Install the dependencies `pip install -r requirements.txt`
3. Set the necessary environment variables using a `.env` file.
4. Run the Streamlit application using the command `streamlit run app.py`.

## Code Structure

The `app.py` file contains the main function of the application. It first loads the environment variables, then sets up the Streamlit application. It allows the user to upload a PDF file, then reads the file and extracts the text from it. The text is split into chunks, and embeddings are generated for each chunk. The user can then ask a question about the PDF, and the application will search for similar documents in the knowledge base and use a question answering chain to generate a response.

## Future Work

Future improvements could include better handling of PDF files with complex layouts, support for multiple languages, and improvements to the question answering algorithm.
