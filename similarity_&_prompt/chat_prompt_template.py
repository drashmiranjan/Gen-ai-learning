from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

template2 = PromptTemplate(
    template='greet this person in 5 language. the name of the person is {name}',
    input_variables=['name']
)                                                                                                   

prompt = template2.invoke(
    {
        'name':"Developer chunks...."
    }
)

result = model.invoke(prompt)
print(result.content)