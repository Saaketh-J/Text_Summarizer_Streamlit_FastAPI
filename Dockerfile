FROM python:3.7

RUN pip install streamlit st-annotated-text nltk numpy networkx fastapi pydantic typing uvicorn

COPY ./api /api

ENV PYTHONPATH=/api
WORKDIR /api


EXPOSE 8000


CMD ["python", "model.py"]
ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0"]