## A large-language model interface for the IPCC reports.

This repository contains the code for [Climate Query](https://climatequery.com), a chat interface leveraging ChatGPT for the IPCC 6th Assessment Report. 

## Code

This repository can be cloned and run locally, and is easy to modify to run using other source documents.

Python is used to handle offline functionality such as document retrieval, embedding, and vector store setup, while TypeScript is used for the frontend. The key files are:

- .env.example -- contains API keys and environment variables (copy to .env with your information entered)
- src/params.toml -- model information and urls of source documents
- src/embed.py -- a script to generate and upload vector embeddings for the documents
- src/query.py -- a simple Python based chat interface

For information on the frontend, see the [gpt4-pdf-chatbot-langchain](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) repository.


## Credits
Project built with OpenAI's large language models, LangChain, and Pinecone. Front-end based on [gpt4-pdf-chatbot-langchain](https://github.com/mayooear/gpt4-pdf-chatbot-langchain).