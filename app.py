import os
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_groq import ChatGroq
from langchain.chains import GraphCypherQAChain
load_dotenv()

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')


os.environ["NEO4J_URI"]= os.getenv('NEO4J_URI')
os.environ["NEO4J_USERNAME"]= os.getenv('NEO4J_USERNAME')
os.environ["NEO4J_PASSWORD"]= os.getenv('NEO4J_PASSWORD')

groq_api_key = os.getenv('groq_api_key')

from flask import Flask, request, jsonify, render_template, redirect, url_for


graph=Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
)


llm=ChatGroq(groq_api_key=groq_api_key,model_name="Gemma2-9b-It")

chain=GraphCypherQAChain.from_llm(llm=llm,graph=graph,verbose=True, allow_dangerous_requests=True)

# response=chain.invoke({"query":"director of  movie GoldenEye?"})


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query_data = request.form.get('query')
    response = chain.invoke(query_data)["result"]
    return render_template('index.html', query_data=query_data ,response=response)

if __name__ == '__main__':
    app.run(debug=True)