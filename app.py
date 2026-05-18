from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
import ollama

# STEP 1: Load data
loader = TextLoader("data.txt")
documents = loader.load()

# STEP 2: Split text into small chunks
text_splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

# STEP 3: Convert text into embeddings
embeddings = OllamaEmbeddings(model="tinyllama")

# STEP 4: Store embeddings in FAISS
db = FAISS.from_documents(docs, embeddings)

# STEP 5: Ask question
question = input("Ask your question: ")

# STEP 6: Retrieve related content
retrieved_docs = db.similarity_search(question)

context = retrieved_docs[0].page_content

# STEP 7: Generate first answer
prompt = f"""
Answer the question using this context.

Context:
{context}

Question:
{question}
"""

response = ollama.chat(
    model="tinyllama",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

answer = response["message"]["content"]

print("\nFIRST ANSWER:\n")
print(answer)

# STEP 8: Self-Healing Evaluation
if "I don't know" in answer or len(answer) < 20:

    print("\nAnswer weak detected...")
    print("Retrying with improved prompt...\n")

    improved_prompt = f"""
You are an intelligent AI assistant.

Answer clearly and correctly.

Context:
{context}

Question:
{question}
"""

    improved_response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "user", "content": improved_prompt}
        ]
    )

    final_answer = improved_response["message"]["content"]

    print("IMPROVED ANSWER:\n")
    print(final_answer)

else:
    print("\nGood answer detected.")