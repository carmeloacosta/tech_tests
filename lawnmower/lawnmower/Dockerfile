FROM python:3.9-buster
COPY . /lawnmower
ENV PYTHONPATH=/
RUN pip install -r /lawnmower/test_requirements.txt
CMD python /lawnmower/src/main.py /lawnmower/conf/input.txt