# Summarizer_Streamlit

A small python app that uses extractive summarization (cosine similarity of vectors of sentences) to summarize long texts.

Implemented both as a Streamlit app that can be run locally and as an API run on a Docker container that can be connected to an AWS EC2 instance (see main.tf)

## Streamlit App

Clone repo and cd into the 'api' folder

Open model.py and uncomment last line

Run `streamlit run model.py`

You should see the application like:

![Screenshot of Streamlit app](images/streamlit_app.png?raw=true "Streamlit app")

## FastAPI/Docker

Clone repo

Assuming Docker is set up, run `docker-compose up --build`

The Docker instance is configured to point the API to the host's port 8000

Go to 'localhost:8000/docs' to see:

![Screenshot of FastAPI docs](images/FastAPI_Docs.png?raw=true "FastAPI docs")
