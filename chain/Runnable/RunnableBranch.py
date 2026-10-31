from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

Prompt1 = PromptTemplate(
    template="write a article about {topic}",
    input_variables=['topic']
)
Prompt2 = PromptTemplate(
    template="make it sort summerise the article {text} in 2 line",
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(Prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>50, RunnableSequence(Prompt2, model, parser)),
    RunnablePassthrough
)

finnal_chain = RunnableSequence(report_gen_chain, branch_chain)

res = finnal_chain.invoke({'topic':'Russia vs Ukrain'})

print(res)