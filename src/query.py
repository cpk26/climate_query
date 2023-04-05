# %%

import openai
import pinecone
import toml
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# User Defined Variables
query = "What are the biggest risks to canada?"

# Get Enviroment Variables
load_dotenv()

root_data_dir = os.environ.get('ROOT_DATA_DIR')
openai_api_key = os.environ.get('OPENAI_API_KEY')
pinecone_api_key = os.environ.get('PINECONE_API_KEY')
pinecone_env = os.environ.get('PINECONE_ENV')
pinecone_index = os.environ.get('PINECONE_INDEX')

openai.api_key = openai_api_key

# User Defined Variables
params = toml.load('params.toml')
embedding_model = params['embedding_model']
gpt_model = params['gpt_model']
urls = params['urls']

# Initialize vector database

pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, model=embedding_model)
db = Pinecone.from_existing_index(pinecone_index, embeddings, "text")

# Question Answering
# References:
#   -https://python.langchain.com/en/latest/modules/chains/index_examples/qa_with_sources.html
#   -https://python.langchain.com/en/latest/modules/chains/index_examples/vector_db_qa_with_sources.html

query = "What areas will be impacted by climate change"

docs = db.similarity_search(query, k=5)
chain = load_qa_with_sources_chain(llm=OpenAI(model=gpt_model), chain_type="map_rerank")
query = "What areas will be impacted by climate change"
output = chain({"input_documents": docs, "question": query})
# %%
