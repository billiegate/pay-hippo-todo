FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
RUN python manage.py db init
RUN python manage.py db migrate --message 'initial database migration'
RUN python manage.py db upgrade
CMD ["python", "manage.py", "run"]