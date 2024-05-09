FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DEBUG=True
ENV SECRET_KEY=django-insecure-nd_ox==axyf7!82rf*Pq4>.9d~}~T,0G?iI21
ENV DATABASE_URL=postgres://postgres:password@localhost:5431/db
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=postgres
ENV PGDATA=/var/lib/postgresql/data/pgdata
ENV POSTGRES_DB=db

RUN mkdir /ecothon

WORKDIR /ecothon

ADD . /ecothon/

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000