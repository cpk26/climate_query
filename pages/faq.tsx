import Layout from '@/components/layout';
import styles from '@/styles/FAQ.module.css';
import Link from 'next/link';

export default function Home() {


  return (
    <>
      <Layout>
        <div className="mx-auto flex flex-col gap-4">
          <h1 className="text-2xl font-bold leading-[1.1] tracking-tighter text-center">
            Frequently Asked Questions
          </h1>
          </div>
          <main className={styles.main}>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
            What kind of questions can I ask and what sources of information are used to answer them?
            </h2>
            <p>
            The query interface is designed to answer questions related to climate change and is limited to that scope.
            It uses information from the IPCC 6th assessment report to generate responses.
            Data from four documents are queried:</p>
            <ul style={{ listStyleType: 'disc', paddingTop: '1em',paddingBottom: '1em', paddingLeft: '2em' }}>
            <li>AR6 Synthesis Report: Climate Change 2023</li>
            <li>AR6 Climate Change 2021: The Physical Science Basis</li>
            <li>AR6 Climate Change 2022: Mitigation of Climate Change</li>
            <li>AR6 Climate Change 2022: Impacts, Adaptation and Vulnerability</li>
            </ul>
            <p>The IPCC reports are written by thousands of climate scientists and experts from around the world, and are a comprehensive and up-to-date source of information on climate change. 
            </p>
          </div>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
              How does this work?
            </h2>
            <p>
            The documents queried have been split into smaller chunks (imagine each chunk being approximately a paragraph).
            A vector embedding of each chunk was created using a large language model. The chunk, the embedding, and metadata
            are stored in a database. When you type in a query, an embedding of the query is created, and we search for the chunks
            with the most similar embedding. These chunks are fed into a large language model, with the instruction to craft 
            the response from these sources, or return that the answer was not found.
            </p>
          </div>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
              What technologies are used?
            </h2>
            <p>
            The key technologies are OpenAI&apos;s large language models, LangChain, and Pinecone. The frontend is 
            adapted from this <Link href="https://github.com/mayooear/gpt4-pdf-chatbot-langchain">repository</Link>.
            </p>
          </div>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
              How accurate are the answers provided?
            </h2>
            <p>
            This depends on the query! At a high level, we are not asking the large-language model (ChatGPT) for the answer directly.
            Instead we are searching for the relevant information, and then asking the model to synthesize the information. This means
            that the answers aren&apos;t likely fictitious, but depend highly on the effectiveness of our information retrieval. As with many AI projects, getting
            from 0 to proof-of-concept is one step, but optimizing the system further is progressively harder. Please reach out if
            this is of interest or relevance to you.
            </p>
          </div>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
              Does the site cost money to run?
            </h2>
            <p>
            Parsing the documents and creating vector embeddings was done with relatively minimal cost, but there is a charge for each query.
            </p>
          </div>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
              Who made the site and can I get in contact?
            </h2>
            <p>
                This site was created by <Link href="https://ckoziol.com">Conrad Koziol</Link>. Comments or feedback are welcome. I can be reached at ckoziol@gmail.com or @cpkoziol.
            </p>
          </div>
          <div className={styles.cloud}>
            <h2 className="text-xl font-bold text-center">
              Is there a GitHub repository that I could look?
            </h2>
            <p>
              The code to create this site is available <Link href="https://github.com/cpk26/climate_query">here</Link>.
            </p>
          </div>
        </main>
      </Layout>
    </>
  );
}
