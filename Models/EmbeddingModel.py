from langchain_google_genai import GoogleGenerativeAIEmbeddings

class EmbeddingModel:
    def __init__(self, model="models/embedding-004"):
        self.embedding_model = GoogleGenerativeAIEmbeddings(model=model)