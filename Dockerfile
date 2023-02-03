# usar imagem Python como base
FROM python:3.8-slim-buster

# definir diretório de trabalho
WORKDIR /app

# copiar arquivos de aplicação para o diretório de trabalho
COPY . .

# instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# expor a porta do servidor web
EXPOSE 5000

# definir variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]