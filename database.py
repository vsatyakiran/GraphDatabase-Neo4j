"""
    To load the dataset of movies into the Neo4j database
    DataSet : 'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv' as row
"""


import os
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
load_dotenv()

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

os.environ["NEO4J_URI"]= os.getenv('NEO4J_URI')
os.environ["NEO4J_USERNAME"]= os.getenv('NEO4J_USERNAME')
os.environ["NEO4J_PASSWORD"]= os.getenv('NEO4J_PASSWORD')

groq_api_key = os.getenv('groq_api_key')

graph=Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
)


### Load the dataset of movie

movie_query="""
LOAD CSV WITH HEADERS FROM
'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv' as row

MERGE(m:Movie{id:row.movieId})
SET m.released = date(row.released),
    m.title = row.title,
    m.imdbRating = toFloat(row.imdbRating)
FOREACH (director in split(row.director, '|') |
    MERGE (p:Person {name:trim(director)})
    MERGE (p)-[:DIRECTED]->(m))
FOREACH (actor in split(row.actors, '|') |
    MERGE (p:Person {name:trim(actor)})
    MERGE (p)-[:ACTED_IN]->(m))
FOREACH (genre in split(row.genres, '|') |
    MERGE (g:Genre {name:trim(genre)})
    MERGE (m)-[:IN_GENRE]->(g))
"""

graph.query(movie_query)