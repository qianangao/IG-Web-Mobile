FROM python:3.6.8

WORKDIR /app

ADD . /app

RUN chmod a+x run.sh

RUN pip install -r requirements.txt --no-index --find-links=file:///app/requirements

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

CMD /app/run.sh
