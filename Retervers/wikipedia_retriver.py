import wikipedia
from langchain_community.retrievers import WikipediaRetriever

wikipedia.set_user_agent(
    "LangChainLearning/1.0 (your-real-drashmiranjan36@gmail.com)"
)

# Initialize the retriever (optional: set language and top_k)
retriever = WikipediaRetriever(top_k_results=2, lang="en")

# Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# Get relevant Wikipedia documents
docs = retriever.invoke(query)

print(docs)