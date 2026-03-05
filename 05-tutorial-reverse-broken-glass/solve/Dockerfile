FROM python:3.9-slim

WORKDIR /solve

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY solve.py .

CMD ["python", "solve.py"]
