from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

prompt1 = PromptTemplate(
    template='''
Generate a detailed report on {topic}
''',
input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='''
generate a 5 pointer summery from the following text \n {text}
''',
input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployement in Indian IT market due to Ai'})

print(result)

chain.get_graph().print_ascii()

