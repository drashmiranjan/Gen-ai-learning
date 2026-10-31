from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2", output_dimensionality=32)

multiple_text = [
    "hii i am Rashmi Ranjan Das",
    "i am a python developer",
    "i have 1 yr of exprience as a python developer",
    "i am 24 yr old",
    "i am profficient in python, postgresql, genAI, Langchain, Pandas, Numpy, ScikitLearn, FastApi, Django",
]

result = embeddings.embed_documents(multiple_text)
print(str(result))