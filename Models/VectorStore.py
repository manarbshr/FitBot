from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
import os

class VectorStore:
    def __init__(self, collection_name, embedding_function, persist_directory):
        self.vector_store = self._create_collection(collection_name, embedding_function, persist_directory)

    def _create_collection(self, collection_name, embedding_function, persist_directory):
        if not os.path.exists(persist_directory):
            loader = DirectoryLoader("Assets/documents", show_progress=True, use_multithreading=True)
            docs = loader.load()
            return Chroma(
                collection_name=collection_name,
                docs=docs,
                embedding_function=embedding_function,
                persist_directory=persist_directory
            )
        else:
            return Chroma(
                collection_name=collection_name,
                embedding_function=embedding_function,
                persist_directory=persist_directory,
            )
    
    def get_retriever(self):
        return self.vector_store.as_retriever()