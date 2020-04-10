FROM python:3.6-alpine
RUN pip3 install pika flask requests
COPY simple_server.py .
CMD ["python","simple_server.py"]