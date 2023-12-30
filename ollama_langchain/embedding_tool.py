from langchain.embeddings import OllamaEmbeddings

class ollama_embeddings():
    """Get the embeddings for the text.
        Parameters:
            text (str): The text to get embeddings for.
            model (str): The model to use for embeddings. In this case, llama2:7b.
    """
    def __init__(self):
        self.model = "llama2:7b"

    def get_embeddings(self, text):
        embeddings = OllamaEmbeddings(model=self.model)
        query_result = embeddings.embed_query(text)
        return query_result