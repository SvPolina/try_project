FROM python:3.9
RUN python3 -m pip install  fastapi[all]==0.79.0
ENV APP_HOST=0.0.0.0
ENV APP_PORT=80
ENV LOG_LVL=INFO
WORKDIR /app
COPY ./app /app
ENTRYPOINT ["python3", "__main__.py"]