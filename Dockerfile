FROM python:3

COPY . /app
RUN pip install -r /app/requirements.txt

CMD python /app/manage.py runserver 7001
