# self-healing-rag-pipeline
Advanced Self-Healing RAG Pipeline using LangChain, FAISS, Ollama and TinyLlama

An advanced Generative AI project that improves the reliability of Retrieval-Augmented Generation (RAG) systems using self-healing response evaluation and retry mechanisms.

This project retrieves relevant information from a knowledge base, generates answers using an LLM, evaluates response quality, and retries automatically if weak or incomplete answers are detected.

Features :
 - Retrieval-Augmented Generation (RAG)
 - Semantic similarity search using FAISS
 - Embedding generation with Ollama
 - TinyLlama local LLM integration
 - Self-healing retry mechanism
 - Automated answer quality evaluation
 - Context-aware response generation

 Project Workflow:-

 User Question
      ↓
Retrieve Relevant Context
      ↓
Generate AI Response
      ↓
Evaluate Response Quality
      ↓
Weak Answer?
   YES → Retry with Improved Prompt
   NO  → Final Output

Tech Stack:-
 - Python
 - LangChain
 - FAISS Vector Database
 - Ollama
 - TinyLlama
 - Retrieval-Augmented Generation (RAG)

 Project Structure:-

 Self_Healing_RAG/
│
├── app.py
├── data.txt
└── README.md

Installation:-
Clone Repository - git clone https://github.com/TEJAISLAVATH/self-healing-rag-pipeline.git
Install Dependencies - pip install langchain langchain-community faiss-cpu pypdf ollama
Run Project - python app.py
Example Questions - What is AI?
                    What is Machine Learning?
                    Explain Self-Healing RAG...etc

 Key Learnings:-  Building end-to-end RAG pipelines
                  Vector database implementation
                  Embeddings and semantic search
                  LLM orchestration workflows
                  Self-healing AI systems
                  Retrieval optimization techniques  

Future Improvements:-  PDF document support
                       LangGraph workflow orchestration
                       Multi-agent architecture
                       Advanced hallucination detection
                       Streamlit web interface
                       Chat history memory              

Author: Teja Islavath
LinkedIn - linkedin.com/in/teja-islavath
GitHub - https://github.com/TEJAISLAVATH






   
