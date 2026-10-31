from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2", output_dimensionality=32)

result = embeddings.embed_query(" i am a python developer")


print(result)
print(str(result))

