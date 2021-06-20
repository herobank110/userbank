FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=userbank
ENV FLASK_ENV=development
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3001"]
