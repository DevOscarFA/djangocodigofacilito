FROM python:3.5

ENV PYTHONUNBUFFERED 1
ENV WEPAPP_DIR=/webapp

RUN mkdir $WEPAPP_DIR
WORKDIR $WEPAPP_DIR

ADD requirements.txt $WEPAPP_DIR/
RUN pip install -r requirements.txt
ADD . $WEPAPP_DIR/