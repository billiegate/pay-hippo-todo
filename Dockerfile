FROM python:3.7
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
RUN chmod +x serve.sh
# CMD ["python", "manage.py", "run"]
ENTRYPOINT ["./serve.sh"]