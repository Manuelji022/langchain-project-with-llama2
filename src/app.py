import streamlit as st
from PyPDF2 import PdfReader 
from chunking_tool import chunking_tool
from embedding_tool import ollama_embeddings
from src.db.mongodb_connection import DBConnection

def set_page_config():
    """Set the page configuration."""
    st.set_page_config(page_title="Read PDFs", page_icon="📖")
    """Display the page header."""
    st.header("Ask questions based on PDFs using llama2 model")

def pdf_reader():
    """
    Upload a PDF file and return it.
    """
    pdf = st.file_uploader("Upload a PDF", type=["pdf"])
    """Read a PDF file and return its text."""
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def split_text_into_chunks(text, chunk_size, overlap):
    """Split the text into chunks and display them."""
    text_splitter = chunking_tool(text, chunk_size, overlap)
    return text_splitter.split_text()

#def get_embeddings(text):
    """Get the embeddings for the text."""
    embeddings = ollama_embeddings()
    return embeddings.get_embeddings(text)

#def upload_embeddings(chunks, embeddings):
    """Upload the embeddings to MongoDB Atlas."""
    db_connection = DBConnection()
    db_connection.connect_to_db()
    db_connection.upload_embeddings(chunks, embeddings)


def main():
    set_page_config()
    # Upload PDF
    text = pdf_reader()
    # Split text into characters
    if text:
        chunks = split_text_into_chunks(text, 1000, 100)
        # Get embeddings for each chunk
        #embeddings = get_embeddings(chunks)
        # Upload embeddings to MongoDB Atlas
        #upload_embeddings(chunks, embeddings)
        
        st.write(chunks)

if __name__ == "__main__":
    main()
