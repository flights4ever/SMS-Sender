FROM python:3.9

ADD /src .

RUN pip install requests python-dotenv

CMD [ "python", "./main.py" ]