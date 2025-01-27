import os
from dotenv import load_dotenv
from langchain.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit

load_dotenv()
# Get environment variables
api_key = os.environ["gemini_key"]
conn_string = os.getenv("conn_string")

# Initialize LLM 
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=api_key, temperature=0.5)

def create_agent(llm, db_uri, verbose=True):
  """
  Creates an SQL agent for interacting with a database.

  Args:
    llm: The language model to use.
    db_uri: The URI connection string for the database.
    verbose: Whether to print verbose output.

  Returns:
    The created SQL agent.
  """
  db = SQLDatabase.from_uri(db_uri)
  toolkit = SQLDatabaseToolkit(db=db, llm=llm)
  agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=verbose)
  return agent

# Create the SQL agent
agent = create_agent(llm, conn_string)
def get_response(q):
  response = agent.invoke(q)["output"]
  return response