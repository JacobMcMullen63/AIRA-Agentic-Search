import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

db = 'newdb'
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')

table = 'confluencetable'
model_name = 'sentence-transformers/all-MiniLM-L6-v2' #os.getenv('MODEL_NAME')
model = HuggingFaceEmbeddings(model_name=model_name)
embedding_dimensions = 384 # Specific to the model
max_reference_len = 100 # Partially-Specific to the model

dist_function = '<->'
# ALTERNATIVES:
# <-> - L2 distance
# <#> - (negative) inner product
# <=> - cosine distance
# <+> - L1 distance

confluence_api_token = os.getenv('CONFLUENCE_API_TOKEN')
confluence_user = os.getenv('CONFLUENCE_USER')