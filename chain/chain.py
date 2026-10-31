from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

prompt = PromptTemplate(
    template= '''
create a professional social media post about: 
{topic}

keep it engaging and suitable for business.
''',
input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result  =  chain.invoke({
    "topic":"python developer"
})

print(result)