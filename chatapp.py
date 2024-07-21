from dspy.retrieve.qdrant_rm import QdrantRM
qdrant_retriever_model = QdrantRM("phi_data", client, k=3)