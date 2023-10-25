FROM python:3.8
WORKDIR /api
COPY requirements.txt /api
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /api
EXPOSE 27017
EXPOSE 8080
CMD ["python3", "app.py"]

