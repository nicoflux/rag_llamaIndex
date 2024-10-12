# import os
# import warnings

# # Suppress TensorFlow INFO and WARNING messages
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Suppress Deprecation Warnings
# warnings.filterwarnings('ignore', category=DeprecationWarning)


# import logging
# import sys

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
)

#Q&A
query_engine = index.as_query_engine()
"""as_query_engine builds a default retriever and query engine on top of the index. 
You can configure the retriever and query engine by passing in keyword arguments.
ere, we configure the retriever to return the top 5 most similar documents (instead of the default of 2)."""
#query_engine = index.as_query_engine(similarity_top_k=5)

#Chat
#query_engine = index.as_chat_engine()

response = query_engine.query("Quels sont les enjeux liés à l'intégration d'IA en entreprise ?")
print(response)