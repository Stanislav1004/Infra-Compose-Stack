FROM python:3.11-slim

RUN useradd -u 10001 appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R appuser:appuser /app 
USER appuser

EXPOSE 8080

CMD ["uvicorn", "app.py:app", "--host", "0.0.0.0", "--port", "8080"] 
