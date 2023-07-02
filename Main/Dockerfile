FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /MovieRatings
WORKDIR /MovieRatings
ADD requirements.txt /MovieRatings/
RUN pip install -r requirements.txt
ADD . /MovieRatings/
