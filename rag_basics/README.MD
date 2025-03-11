This project demonstrates how to implement RAG application. 

# **Retrieval-Augmented Generation (RAG) Demo - Key Learnings**

## **1️⃣ Data Ingestion & Loading Documents**
- Using **LangChain’s `TextLoader`** to load local text files.
- **Web scraping** with `WebBaseLoader` and **BeautifulSoup** to extract structured content.
- **PDF ingestion** using `PyPDFLoader` to extract text from research papers.

---

## **2️⃣ Document Processing & Chunking**
- **Splitting documents** into smaller chunks using `RecursiveCharacterTextSplitter` for efficient retrieval.
- Ensuring **optimal chunk size & overlap** to balance context retention and retrieval performance.

---

## **3️⃣ Embeddings & Vector Databases**
- **Generating embeddings** using `OpenAIEmbeddings` to convert text into vector representations.
- **Using ChromaDB** for storing document vectors and performing similarity searches.
- **Integrating FAISS** as an alternative vector store for efficient retrieval.

---

## **4️⃣ Retrieval Mechanism**
- Performing **similarity search** on stored embeddings to fetch relevant documents.
- **Setting up a retriever** using `db.as_retriever()` to structure queries effectively.

---

## **5️⃣ Query Execution & LLM Integration**
- **Using OpenAI’s LLM** (`OpenAI()`) for answering queries based on retrieved documents.
- Designing a **prompt template (`ChatPromptTemplate`)** to guide the model in answering contextually.
- Creating a **retrieval chain** (`create_retrieval_chain`) that fetches relevant documents before passing them to the LLM.


---

This demo covers a **complete Retrieval-Augmented Generation (RAG) workflow**, from **ingestion → processing → indexing → retrieval → query response generation** using **LangChain & FAISS/ChromaDB**. 🚀
