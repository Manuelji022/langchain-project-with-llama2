import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch

load_dotenv()
connection_string = os.getenv("MONGODB_CONNECTION")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")
index_name = os.getenv("INDEX_NAME")


client = MongoClient(connection_string.mongodb_conn_string)
collection = client[connection_string.db_name][connection_string.collection_name]

# Insert the documents in MongoDB Atlas with their embedding
docsearch = MongoDBAtlasVectorSearch.from_documents(
    docs, embeddings, collection=collection, index_name=index_name
)

