FROM python:3.10
RUN pip install --upgrade pip
RUN pip install --upgrade scikit-learn

WORKDIR /app

#Copy all the content of current directory to /app
ADD . /app

#Installing required packages

RUN pip3 install -r requirements.txt


EXPOSE 5000

# Run app.py when the container launches

CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]