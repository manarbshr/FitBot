from Models import ChatModel,EmbeddingModel, VectorStore
from langchain_core.prompts import ChatPromptTemplate

class chatController:
    def __init__(self):
        self.embedding_model = EmbeddingModel(model="models/embedding-001")
        self.vector_store = VectorStore("vector_db", self.embedding_model, "vector_db")
        self.retriever = self.vector_store.get_retriever()
        self.chat_model = ChatModel(self.retriever, self.embedding_model)

    def get_response(self):
        prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful fitness coach assistant that answers questions related to health and fitness. using the below context to answer the user's question. \n\n",  
        ),
        ("system", "{context}"),
        ("human", "{input}"),
    ]
)
        
        response = self.chat_model.chain(prompt)
        return response
    
    