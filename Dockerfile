#slim version of python
FROM python:3.10-slim-buster

#env variables


#make directory for the app
RUN mkdir /app

#set as working directory
WORKDIR /app

#copy requirements file
COPY requirements.txt .

#apply install of requirements
RUN pip install -r requirements.txt

#copy all files to the current work directory
COPY . .

# execute fastapi
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]