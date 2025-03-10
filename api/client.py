

import requests
import streamlit as st

ESSAY_API_URL = "http://localhost:8000/essay/invoke"
POEM_API_URL = "http://localhost:8000/poem/invoke"



st.title("LangChain Routes Demo")
def get_essay(topic):
    response = requests.post(ESSAY_API_URL, json={"input": {"topic": topic}})
    if response.ok:
        return response.json()['output']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

def get_poem(topic):
    response = requests.post(POEM_API_URL, json={"input": {"topic": topic}})
    return response.json()

# Streamlit UI
st.title("📚 LangChain Essay & Poem Generator")

topic_essay = st.text_input("📝 Essay Topic:")
if st.button("Generate Essay"):
    if topic_essay:
        essay_result = get_essay(topic_essay)
        st.subheader("Your Essay:")
        st.write(essay_result)

topic_poem = st.text_input("🌸 Poem Topic:")
if st.button("Generate Poem"):
    poem_result = get_poem(topic_poem)
    st.subheader("Your Poem:")
    st.write(poem_result.get('output', 'No response'))
