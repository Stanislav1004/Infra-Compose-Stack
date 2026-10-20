FROM python:3.11-slim

RUN useradd -u 10001 appuser

WORKDIR /app

COPY app.py .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["python3", "app.py"] 
