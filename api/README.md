# LangChain API and Streamlit Frontend Project

This project demonstrates how to use **LangChain** and **LangServe** to create API endpoints, along with a **Streamlit** frontend to interact with these APIs. The goal is to experiment with route creation, chaining prompts, and language models using LangChain.

## 📂 Project Structure

```
project/
├── app.py           # LangServe API backend
├── client.py        # Streamlit frontend
├── secret_key.py    # API keys (OpenAI, LangSmith)
└── requirements.txt # Dependencies
```

## 🚀 How to Run This Project

### 1. Setup Conda Environment

Create and activate the environment:

```bash
conda create --prefix ./env python=3.10
conda activate ./env
```

Verify Python and packages:

```bash
python --version
conda list
```

### 2. Install Dependencies

Install packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install langchain langchain-community langchain-openai openai fastapi uvicorn langserve streamlit ollama python-dotenv requests
```

### 3. Setup API Keys

Create a `secret_key.py` file in your project folder with your API keys:

```python
openai_key = "YOUR_OPENAI_API_KEY"
langchain_key = "YOUR_LANGSMITH_API_KEY"
```

### 4. Run the Backend API (LangServe)

Start the API backend server:

```bash
python app.py
```

Your API endpoints will run at:  
`http://localhost:8000`

### 5. Run the Streamlit Frontend

Start the frontend Streamlit app:

```bash
streamlit run client.py
```

Your frontend will be accessible at:  
`http://localhost:8501`

## 📌 Reference

This project references the following YouTube tutorial for additional guidance:

- [LangChain Video Tutorial](https://www.youtube.com/watch?v=swCPic00c30)

---

Enjoy experimenting and building with LangChain and Streamlit! 🚀✨
