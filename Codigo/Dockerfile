FROM python
ENV PYTHONUNBUFFERED = 1

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . /code/