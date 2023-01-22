FROM python:3.9

COPY ./ /app/
COPY ./requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 9999

CMD ["python3", "-m","uvicorn", "cache:app", "--host=127.0.0.1", "--port=9999"]