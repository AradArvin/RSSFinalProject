
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE=1


ENV PYTHONUNBUFFERED=1


COPY requirements.txt .

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /app/RssProject
COPY . /app


CMD ["python", "RssProject/manage.py", "runserver", "0.0.0.0:8000"]
