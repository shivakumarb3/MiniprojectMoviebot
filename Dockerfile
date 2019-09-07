FROM alpine
FROM python:3.7
COPY . /moviereviewbot
WORKDIR /moviereviewbot
RUN pip install -r requirements.txt
EXPOSE 9000
CMD python ./main.py