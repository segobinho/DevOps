#imagem do python que vamos utilzae
FROM python:3.12

#diretorio de trabalho do container
WORKDIR /app

#instalar as dependencias
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt  

#copiando os arquivos para o docker
COPY . .

#rodando nossa aplicação
CMD ["python", "app.py"]
