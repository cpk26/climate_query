/**
 * Change the namespace to the namespace on Pinecone you'd like to store your embeddings.
 */

if (!process.env.PINECONE_INDEX) {
  throw new Error('Missing Pinecone index name in .env file');
}

const PINECONE_INDEX = process.env.PINECONE_INDEX ?? '';

const PINECONE_NAME_SPACE = ''; //namespace is optional for your vectors

// export { PINECONE_INDEX, PINECONE_NAME_SPACE };
export { PINECONE_INDEX, PINECONE_NAME_SPACE};
