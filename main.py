import os
from dotenv import load_dotenv
import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# file = os.listdir('cv')
# print(file)

load_dotenv()

key_openai=os.getenv('OPENAI_KEY')
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=key_openai,
                model_name="text-embedding-3-small"
            )
documents = []
metadatas = []
ids = []
id = 0

for file in os.listdir('cv'):
    # print(file)
    if file.endswith('.txt'):
        # print(os.path.join('cv', file))
        with open(os.path.join('cv', file), 'r') as f:
            # print(f)    
            # print(f.read().replace('\n', ' ').split('###'))
            chunks = f.read().replace('\n', ' ').split('###')
            # print(chunks)
            # print(chunks[2]) 
            for chunk in chunks:
                if not chunk.isspace() and not chunk == '':
                    # print(chunk)
                    documents.append(chunk)
                    metadatas.append({
                        'file' : file, 'info' : chunks[1]
                    })
                    ids.append(str(id))
                    id += 1
                    # print(chunks[1])
                    
# print(documents)                 
# print(metadatas)
# print(ids)    

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="read_cvs", embedding_function=openai_ef)
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
)

result = collection.query(
    query_texts=input("Ciao, cosa cerchi? "),
    n_results=2
)
print(result)

