VECTOR_DB = []

def store(embedding, text):
    VECTOR_DB.append((embedding, text))

def search(query_embedding):
    return VECTOR_DB[:1]
