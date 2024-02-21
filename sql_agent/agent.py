import langchain
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

from dotenv import load_dotenv
import os

load_dotenv()


# Load environment variables for the openai key
API_KEY = os.getenv("API_KEY")
# Load environment variables for the Redshift connection
HOST = os.getenv("redshift_host")
PORT = 5439
DATABASE= os.getenv("redshift_dbname")
USERNAME = os.getenv("redshift_user")
PASSWORD = os.getenv("redshift_password")

print('redahift username:',USERNAME)

print('calling the api ...')
def api_response(user_input,schema):
    # Construct the Redshift connection URI
    url = f"redshift+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?options=--search_path={schema}"

    # Connected to the database
    print('connecting db ...')
    sql = SQLDatabase.from_uri(url)

    print('sql:',sql)
    memory = ConversationBufferMemory(memory_key="history", input_key="input")
    print('memory:',memory)
    # Connecting to Openai model
    llm = ChatOpenAI(model_name="gpt-4", temperature=0, openai_api_key=API_KEY, verbose=True)
    print('calling sql agent ...')
    agent = create_sql_agent(llm=llm,
                            db=sql,
                            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                            verbose=True,
                            handle_parsing_errors=True,)
                        
    # agent executing
    res = agent.invoke(user_input)
    print('res:',res['output'])
    if res:
        status='Success'
    return  res['output'],status

