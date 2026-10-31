from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# start the pydantic output parser

class Person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt = 18, description='Age of the person')
    city : str = Field(description='Name of the city the person belongs to.')

parser  = PydanticOutputParser(
    pydantic_object=Person,
)

template = PromptTemplate(
    template='Generate the name, age and the city of the frictional {place} person \n'
    '{format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt = template.invoke({"place": "Indian"})

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)