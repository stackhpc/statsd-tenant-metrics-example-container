FROM python:2

RUN pip install statsd

ADD statsd_demo.py /

CMD [ "python", "./statsd_demo.py" ]
