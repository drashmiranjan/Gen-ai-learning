from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

Prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)
Prompt2 = PromptTemplate(
    template="Explain the joke {text}",
    input_variables=['text']
)

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

Jokechain = RunnableSequence(Prompt1, model, parser)

parallelchain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count':RunnableLambda(word_count),
    'joke_Explain': RunnableSequence(Prompt2, model, parser)
})

final_chain = RunnableSequence(Jokechain, parallelchain)

res = final_chain.invoke({'topic':'cricketer'})

print(res['joke'])
print(res['word_count'])
print(res['joke_Explain'])