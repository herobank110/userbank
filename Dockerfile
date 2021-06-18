FROM python:3.10-rc-alpine
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "/app/src/main.py"]
