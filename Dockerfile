# Base image(runtime) of our container
FROM python:3.10.12

LABEL authors="aashishnk"

COPY requirements.txt requirements.txt

# force pip to install all packages from the remote repository instead of searching or downloading in cache
RUN pip install --no-cache-dir -r requirements.txt

# mount the application code to the image
COPY . code

WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
