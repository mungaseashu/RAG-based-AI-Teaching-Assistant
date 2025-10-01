# Sigma Web Development Course Q&A (RAG-based AI)

This project is an interactive Q&A web app for the Sigma Web Development Course. It uses Retrieval-Augmented Generation (RAG) to answer user questions about the course content, providing detailed answers with video references and timestamps.

## Features

- **Ask questions** about the Sigma Web Development Course.
- **Retrieves relevant video segments** using semantic search (embeddings + cosine similarity).
- **Generates human-like answers** using a local LLM (Ollama).
- **Displays video titles, numbers, timestamps, and subtitles** for context.

## How It Works

1. **Embeddings:** Subtitle chunks from course videos are embedded and stored.
2. **User Query:** When a user asks a question, it is embedded using Ollama's embedding API.
3. **Similarity Search:** The app finds the most relevant subtitle chunks using cosine similarity.
4. **Prompt Construction:** The relevant chunks and the user's question are sent to a local LLM (Ollama) for answer generation.
5. **Response:** The app displays the answer and the relevant video chunks.

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/) running locally with `bge-m3` and `llama3.2` models
- `joblib`, `numpy`, `pandas`, `scikit-learn`, `requests`

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/sigma-webdev-rag.git
    cd sigma-webdev-rag
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download and run Ollama:**
    - [Install Ollama](https://ollama.com/download)
    - Pull required models:
      ```bash
      ollama pull bge-m3
      ollama pull llama3.2
      ```
    - Start Ollama server:
      ```bash
      ollama serve
      ```

4. **Prepare embeddings:**
    - Ensure `embeddings.joblib` is present in the project directory.

## Usage

1. **Start the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Open your browser** and go to the provided local URL (usually `http://localhost:8501`).

3. **Ask questions** about the Sigma Web Development Course and get detailed, timestamped answers!

## File Structure

- `app.py` — Main Streamlit application.
- `embeddings.joblib` — Precomputed embeddings for video subtitle chunks.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.

## Troubleshooting

- **Ollama not running:** Make sure Ollama is running locally on port 11434.
- **Timeouts:** If embedding or LLM requests time out, check your system resources or increase the timeout in `app.py`.
- **Missing models:** Ensure both `bge-m3` and `llama3.2` models are pulled in Ollama.

## License

This project is for educational purposes.

---

**Made with ❤️ for the Sigma Web Development Course.**
