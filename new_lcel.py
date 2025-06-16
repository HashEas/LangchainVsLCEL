# lcel_weather.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Step 1: Create Prompt Template (Runnable)
prompt = PromptTemplate.from_template(
    "What is the weather like in {city} today?"
)

# Step 2: Initialize LLM (Runnable)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Step 3: Output parser (optional but best practice)
parser = StrOutputParser()

# Step 4: Compose LCEL chain
chain = prompt | llm | parser

# Step 5: Invoke with input
result = chain.invoke({"city": "New York"})
print(result)