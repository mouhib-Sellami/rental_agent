# 🏠 Renting Agent

An intelligent agent for managing rental queries, powered by **Ollama** and vector search.

---

## 📋 Requirements

- Python **3.11+**
- [Ollama](https://ollama.com/)

---

## ⚙️ Installation

1. **Pull required models with Ollama:**

   ```bash
   ollama pull mxbai-embed-large
   ollama pull qwen3:8b
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **🗂️ Create Knowledge Base**

   ```bash
   python vector.py
   ```

5. **🚀 Run the Agent**

   ```bash
   python agent.py
   ```

---

## 📖 Notes

- Ensure Ollama is installed and running in the background before starting the agent.
- Customize the knowledge base in vector.py with your own rental data.

