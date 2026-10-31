from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

prompt1 = PromptTemplate(
    template="wite a funny joke about {topic} for tweeter",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="wite a funny joke about {topic} for linkedin",
    input_variables=['topic']
)

parser = StrOutputParser()

parallelChain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'linkedin': RunnableSequence(prompt2, model, parser)
    } 
)

res = parallelChain.invoke({'topic':'AI'})

print(res)