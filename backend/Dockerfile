FROM python:3.10-slim


WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .


EXPOSE 8000

# Comando para iniciar o FastAPI com Uvicorn
CMD ["python", "main.py"]
