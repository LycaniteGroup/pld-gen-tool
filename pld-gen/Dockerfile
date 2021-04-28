FROM nikolaik/python-nodejs:python3.8-nodejs12

WORKDIR /var/app
RUN apt-get update

COPY ./git2md/requirements.txt .
COPY ./md2html /var/md2html

RUN pip3 install -r requirements.txt

RUN cd /var/md2html \
    && npm i

COPY ./entrypoint.sh .

ENTRYPOINT [ "/bin/sh", "/var/app/entrypoint.sh" ]