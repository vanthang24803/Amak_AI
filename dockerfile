FROM python:3.12.6

WORKDIR /amak

COPY ./requirements.txt /amak//requirements.txt

RUN pip install --no-cache-dir --upgrade -r /amak/requirements.txt

COPY ./app /amak/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]