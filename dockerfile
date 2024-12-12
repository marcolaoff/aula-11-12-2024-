# Use a imagem base do Python 3.12
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos para o container
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando para rodar o gerador de senha
CMD ["python", "app/password_generator.py"]