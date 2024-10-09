# GraphDatabase-Neo4j

![image](https://github.com/user-attachments/assets/c8667285-0425-4a6e-bafa-ccb62b1f86f1)

![image](https://github.com/user-attachments/assets/7e4db55c-0a8d-4525-a031-d9a462f7d2e7)


## Introduction

This repository contains the code for the Neo4j graph database. The code is written in Python and uses the `neo4j` library to interact with the database. The code is written in a modular way, so that it can be easily extended to add more functionality.

## About

Neo4j is a graph database that is designed to store and query large amounts of data in a graph format. It is a NoSQL database that is optimized for storing and querying graph data. Neo4j is a popular choice for applications that require complex graph queries, such as social networks, recommendation engines, and fraud detection systems.

- **Dataset used:** [MovieIMDB](https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv)

- **Database:** Neo4j Aura (Cloud) - Free Tier 

- **LLM:**  LLM used to intract with the database is `Groq`, it provides all the latest llms APIs for free.

## Features

- **Create Database:** The code creates a Neo4j database and populates it with data from a CSV file.

- **Query Database:** The code queries the database using the LLM API and displays the results on the webpage.

## Steps to run the code

1. Clone the repository

```bash
    git clone 

```

2. Create account in [Neo4j Aura](https://neo4j.com/cloud/aura/) and get the URI, Username and Password.

3. Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
    NEO4J_URI=bolt://<YOUR_NEO4J_URI>:768
    NEO4J_USER=<YOUR_NEO4J_USER>
    NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>
    GROQ_API_KEY=<YOUR_GROQ_API_KEY>
```

4. Create a virtual environment

```bash
    python -m venv venv
    source venv/bin/activate
```

5. Install the required libraries

```bash
    pip install -r requirements.txt
```
6. Get GROQ API Key from [here](https://groq.dev/)

7. Run the code to create the database

```bash
    python database.py
```
This will create the database and populate it with the data from the `movies_small.csv` file.

8. Run the code to query the database using LLM

```bash
    python app.py
```

This will run the code and query the database using the LLM API. The results will be displayed on the webpage.






