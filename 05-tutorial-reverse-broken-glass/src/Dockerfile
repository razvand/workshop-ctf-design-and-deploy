FROM python:3.9-slim

RUN apt-get update && apt-get install -y fonts-dejavu

WORKDIR /src
COPY generate.py .

RUN pip install Pillow

CMD ["python", "generate.py"]
