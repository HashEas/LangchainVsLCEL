# old_langchain_weather.py

from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Step 1: Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Step 2: Create Prompt Template
prompt = PromptTemplate(
    input_variables=["city"],
    template="What is the weather like in {city} today?"
)

# Step 3: Build Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Step 4: Run Chain
result = chain.run("New York")
print(result)