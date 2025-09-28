FROM python:3.13-slim

WORKDIR /app

ENV TZ=Asia/Bangkok

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /opt/operaton/fastapi/logs

COPY .env .

COPY . .

EXPOSE 8300

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8300"]