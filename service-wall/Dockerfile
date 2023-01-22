FROM python:3.9

COPY ./ /app/
COPY ./requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 65534

CMD ["python3", "-m","uvicorn", "wall:app", "--host=0.0.0.0", "--port=65534"]