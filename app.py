import streamlit as st
import joblib
import numpy as np
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="Sigma Web Dev Q&A", layout="wide")

# Load the embeddings
@st.cache_data
def load_data():
    return joblib.load("embeddings.joblib")

df = load_data()

# Create embeddings via Ollama
def create_embedding(text_list):
    response = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return response.json()["embeddings"]

# Generate response from LLM
def inference(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": True
    })
    return response.json()["response"]

# ✅ Streamlit UI
st.title("💻 Sigma Web Development Course Q&A")
st.markdown("Ask a question about the course content, and get a detailed answer with timestamps!")

# Input
user_query = st.text_input("Ask your question about the course:", "")

if st.button("Get Answer") and user_query.strip() != "":
    with st.spinner("Processing your question..."):

        # Step 1: Embed the question
        question_embedding = create_embedding([user_query])[0]

        # Step 2: Cosine similarity with saved embeddings
        similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
        top_k = 5
        top_indices = similarities.argsort()[::-1][:top_k]
        selected_chunks = df.loc[top_indices]

        # Step 3: Format prompt
        context_json = selected_chunks[["title", "number", "start", "end", "text"]].to_json(orient="records")
        prompt = f'''
I am teaching web development in my Sigma web development course. Here are video subtitle chunks containing 
video title, video number, start time in seconds, end time in seconds, the text at that time:

{context_json}
---------------------------------
"{user_query}"
User asked this question related to the video chunks, you have to answer in a human way (don't mention the above format, 
it's just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide 
the user to go to that particular video. If the user asks an unrelated question, tell them you can only answer questions 
related to the course.
        '''

        # Step 4: Get response
        response = inference(prompt)

        # Step 5: Show response
        st.subheader("🧠 Answer:")
        st.write(response)

        # Optional: Show context chunks
        with st.expander("🔍 Show relevant video chunks used"):
            st.dataframe(selected_chunks[["title", "number", "start", "end", "text"]])
