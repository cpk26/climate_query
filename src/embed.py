# %%

import openai
import pinecone
import os
import urllib
import toml
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from PyPDF2 import PdfReader
from tqdm.auto import tqdm


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
urls = params['urls']

# %%

# Download PDFs
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

def download_pdf(pdf_url):
    pdf_filename = os.path.basename(pdf_url)
    pdf_loc = root_data_dir + pdf_filename
    if not os.path.exists(pdf_loc):
        print(f'Downloading: {pdf_url}')
        req = urllib.request.Request(pdf_url, headers=headers)
        with urllib.request.urlopen(req) as response, open(pdf_loc, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    print(f'{pdf_filename} on local')

for pdf_url in urls:
    download_pdf(pdf_url)

# %%

# Read pdfs and extract text chunks
def return_docs_from_pdf(fname):
    reader = PdfReader(fname)
    number_of_pages = len(reader.pages)
    sources = []
    for i in range(number_of_pages):
        txt = reader.pages[i].extract_text()
        doc = Document(page_content=txt, metadata={"source": pf, 'page': i},)
        sources.append(doc)
    return sources



pdf_files = [f for f in os.listdir(root_data_dir) if f.endswith('.pdf')]
assert pdf_files, "PDF files are required"

sources = []
for pf in pdf_files:
    fname = root_data_dir + pf
    sources.extend(return_docs_from_pdf(fname))


text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
  chunk_size=1000, chunk_overlap=50)
texts = text_splitter.split_documents(sources)
# %%

# Connect to Pinecone 
pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, model=embedding_model)

# %%

# Populate index from new instance
# if pinecone_index in pinecone.list_indexes():
#     pinecone.delete_index(pinecone_index)
# db = Pinecone.from_documents(texts, embeddings,index_name=pinecone_index)

# %%
# if pinecone_index not in pinecone.list_indexes():
#     pinecone.create_index(pinecone_index, dimension=openai_embed_dim)
# index = pinecone.Index(pinecone_index)

# For lower level code see: https://docs.pinecone.io/docs/openai

# batch_size = 32  # process everything in batches of 32
# for i in tqdm(range(0, len(texts), batch_size)):
#     i_end = min(i+batch_size, len(texts))
#     # get batch of text and IDs
#     texts_batch = texts[i: i+batch_size]
#     content_batch = [re.sub(r'\s+', ' ', t.page_content.strip()) for t in texts_batch]
#     ids_batch = [str(n) for n in range(i, i_end)]
#     # create embeddings
#     res = openai.Embedding.create(input=content_batch, engine=embedding_model)
#     embeds = [record['embedding'] for record in res['data']]
#     # prep metadata and upsert batch
#     meta = [{'text': text.page_content, **text.metadata} for text in texts_batch]
#     to_upsert = zip(ids_batch, embeds, meta)
#     # upsert to Pinecone
#     index.upsert(vectors=list(to_upsert))

