#How to run: python app.py


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate


# For OpenAI models:
from langchain_openai import ChatOpenAI

# For Ollama models, use:
from langchain_community.llms import Ollama

from langserve import add_routes 

import uvicorn 
import os 


# Import API key (Ensure secret_key.py exists)
try:
    from secret_key import openai_key, langchain_key
    os.environ['OPENAI_API_KEY'] = openai_key

    os.environ['LANGCHAIN_API_KEY'] = langchain_key                 #This is Langsmith key
    os.environ['LANGCHAIN_TRACING_V2'] = "true"   
    LANGCHAIN_PROJECT = "Tutorial2"
    LANGSMITH_TRACING='true'
    LANGSMITH_ENDPOINT="https://api.smith.langchain.com"


except ImportError:
    raise ValueError("⚠️ API key missing! Ensure 'secret_key.py' contains keys.")

# FastAPI instance
app = FastAPI(
    title="LangChain API Server",
    description="A simple LangChain API server."
)

# Models
openai_model = ChatOpenAI()
llama2_model = Ollama(model="llama2")

# Prompt templates 
essay_prompt = ChatPromptTemplate.from_template(
    "Write me an essay on {topic} in 100 words."
)
poem_prompt = ChatPromptTemplate.from_template(
    "Write me a short poem on {topic}."
)

# Langserve routes
add_routes(
    app, 
    essay_prompt | openai_model,
    path='/essay'
)

add_routes(
    app, 
    poem_prompt | llama2_model,  # use Ollama here if intended for poem
    path='/poem'
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port= 8000)