FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=userbank
CMD ["flask", "run"]
