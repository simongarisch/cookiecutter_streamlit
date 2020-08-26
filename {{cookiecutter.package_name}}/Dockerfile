
FROM python:3.8-slim-buster
COPY . /src
RUN pip install -r /src/requirements.txt

CMD streamlit run /src/main.py --server.port {{ cookiecutter.docker_port }} --browser.gatherUsageStats False
