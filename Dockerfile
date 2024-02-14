FROM python:3.11

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

# RUN pip install eburger argparse

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/forefy/eburger.git
RUN pip3 install eburger/

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python", "/entrypoint.py"]