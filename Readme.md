# Api service with django and kafka

## Prerequisites

Make sure you have installed next packages:
1. [python3](https://www.python.org/downloads/)
2. pip `python3 -m pip`

## Configure postgresql

Install postgresql.

- install [brew](https://brew.sh/)
- install postgresql via brew `brew install postgresql`
- run postgresql `brew services start postgresql`
- create user: `sudo psql -U <user_name> -d postgres`
- `postgres=# CREATE USER postgres WITH SUPERUSER PASSWORD '<your_password>';`
- `postgres=# ALTER DATABASE postgres OWNER TO postgres;`
- create database: `postgres=# CREATE DATABASE <db_name>;`
- `postgres=# CREATE USER <user_name> WITH password '<your_password>';`
- `postgres=# \c <db_name>>`
- `postgres=# \q`

Check that your database has created via DataBase tool, for example: [dbeaver](https://dbeaver.io/).

## Create virtual environment

Create new directory `mkdir <dir_name> $$ cd <dir_name>`.

Clone the repo `git clone https://github.com/Toffery/django-kafka-postgre.git`.

Create virtual environment `python3 -m venv venv`

Activate venv `source venv/bin/activate`

Install all dependencies `pip install -r requirements.txt`

## Configure settings

Go to `msg_api/settings.py`, then scroll to `DATABASES` dict. 
Replace `'NAME', 'USER', 'PASSWORD'` with your `<db_name>, <user_name>, <your_password>`.

## Migrate

Run `python3 manage.py makemigrations msg_api`
Run `python3 manage.py migrate`
Run `python3 manage.py runserver`
In other terminal run `cd msg_api` `python3 consumer.py`

## Create users

Using dbeaver create some users in table `msg_api_user`

## Send messages

Now go to URL http://127.0.0.1:8000/api/v1/message/ via PostMan, for example.

In the body write your data using this form:

    {
        "user_id": int,
        "message": "text"
    }

This data will be sent to kafka via producer, 
then consumer will receive this message and validate it.

## If you want to use your own Kafka cluster.

Go to [confluent.io](https://www.confluent.io/).
Sign up and get a free trial.

Create a new cluster using its tutorial.

In [confluent-cloud](https://confluent.cloud/) go to Cluster overview > CLuster settings. 
Copy the value of Bootstrap server and paste it in `msg_api/config.py` 
in value `'bootstrap.servers'` in both dicts.

Then create a new topic. If you use 'my_topic', then you don't need to change anything in the code.

If you choose another name, then go to `msg_api/producer.py`, change `topic = 'my_topic'`
to `topic = '<your_topic_name>'`. Then do same in `msg_api/consumer.py`.

Then go to Cluster > Api keys and generate new Global access keys. 
You will receive Api key and Api SECRET. Paste them in `msg_api/config.py` in values
`'sasl.username'` and `'sasl.password'` accordingly in both dicts.

Now you're done.




