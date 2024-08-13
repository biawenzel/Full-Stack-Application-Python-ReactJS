FROM python:3.9
WORKDIR /api02
COPY ./requirements.txt /api02/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /api02/requirements.txt
COPY . /api02
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000 " ]