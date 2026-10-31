from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

prompt = PromptTemplate(
    template="write a funny joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

res = chain.invoke({'topic':'Ai'})

print(res)