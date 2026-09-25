FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python","-c","from governance import Catalog; print('governance ready')"]
