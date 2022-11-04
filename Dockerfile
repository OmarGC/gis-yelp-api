FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /code/requirements.txt

# Setup GDAL
RUN apt-get update
RUN apt-get install -y libgdal-dev
RUN pip install GDAL==3.2.2.1

COPY ./morgana /code/morgana
WORKDIR /code/morgana

EXPOSE 8000

# set work directory
CMD ["python", "manage.py", "migrate", "--no-input"]