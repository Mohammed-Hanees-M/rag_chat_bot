# RAG Chatbot
# 📚 RAG Document Chatbot

A professional **Retrieval-Augmented Generation (RAG)** chatbot that allows users to upload PDF documents and ask questions based only on the uploaded content.

The chatbot combines **FAISS Vector Search**, **Sentence Transformers**, and **Google Gemini** with an automatic **Groq fallback** to provide fast and accurate answers.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Automatic text extraction
- ✂️ Intelligent document chunking
- 🧠 Sentence Transformer embeddings
- ⚡ FAISS Vector Database
- 🤖 Google Gemini Integration
- 🔄 Automatic Groq fallback
- 💬 Chat interface
- 🌙 Modern Streamlit UI
- 📂 Knowledge Base Management

---

## 🛠 Knowledge Modes

Currently Available

- ✅ Replace Knowledge Base

Coming Soon

- ➕ Add Documents
- 🚫 Skip Duplicate Documents
- 🔄 Update Existing Documents
- 📄 DOCX Support
- 📑 TXT Support
- 📊 Excel Support
- 🧠 Conversation Memory
- 📌 Source Citations

---

## 🏗 Project Architecture

```
                PDF Upload
                     │
                     ▼
           Document Loader
                     │
                     ▼
             Text Splitter
                     │
                     ▼
       Sentence Transformer
             Embeddings
                     │
                     ▼
          FAISS Vector Store
                     │
                     ▼
            Similarity Search
                     │
                     ▼
            Prompt Builder
                     │
                     ▼
        Gemini / Groq (Fallback)
                     │
                     ▼
              Final Answer
```

---

## 📂 Project Structure

```
RAG_Chatbot
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│
├── prompts/
│
├── knowledge/
│
├── src/
│   ├── chatbot/
│   ├── ingestion/
│   ├── retrieval/
│   ├── uploader/
│   └── ui/
│
├── tests/
│
└── utils/
```

---

## ⚙️ Technologies Used

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Google Gemini
- Groq
- LangChain
- PyPDF
- NumPy

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag_chat_bot.git
```

Move into the project

```bash
cd rag_chat_bot
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💬 Usage

1. Upload one or more PDF documents.
2. Select **Replace Knowledge Base**.
3. Click **Process Documents**.
4. Ask questions based on the uploaded document.
5. The chatbot retrieves relevant content and generates an answer using Gemini (or Groq if Gemini is unavailable).

---

## 📸 Screenshots

### Main Interface

> *(Add a screenshot here after deployment.)*

### Chat Interface

> *(Add a screenshot here after deployment.)*

---

## 🚀 Future Improvements

- Multiple Knowledge Bases
- DOCX Support
- Excel Support
- Image OCR
- Source References
- Conversation Memory
- Multi-LLM Router
- Authentication
- Admin Dashboard

---

## 👨‍💻 Author

**Mohammed Hanees M**

M.Sc. Data Science  
Christ (Deemed to be University)

GitHub:
https://github.com/Mohammed-Hanees-M

---

## ⭐ If you like this project

Please consider giving the repository a ⭐ on GitHub.