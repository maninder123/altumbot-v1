import langchain
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType

# importing from constant.py file
# from constants import CUSTOM_PREFIX,prompt

# redshift credentials details
redshift_user = "analytics_read"
redshift_password = "zxLYY86vD,6f"
redshift_host = "altumblack-analytics.c623li0efetw.us-east-1.redshift.amazonaws.com"
redshift_port = "5439"
redshift_dbname = "analytics"
redshift_schema = "bebe"  # Specify your schema here

# Openai api key
API_KEY='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'


# Construct the Redshift connection URI
url = f"redshift+psycopg2://{redshift_user}:{redshift_password}@{redshift_host}:{redshift_port}/{redshift_dbname}?options=--search_path={redshift_schema}"

# Connected to the database

sql = SQLDatabase.from_uri(url,
                           )

print('sql:',sql)

# Connecting to Openai model
llm = ChatOpenAI(model_name="gpt-4", temperature=0,  verbose=True)

agent = create_sql_agent(llm=llm,
                         db=sql,
                         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True,)
                       
# agent executing
# agent.invoke('count the total number coupons applied  in the last week?')
agent.invoke('what is the sum of the total sales orders in the last one month?')


