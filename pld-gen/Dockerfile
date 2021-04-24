FROM nikolaik/python-nodejs:python3.8-nodejs12

WORKDIR /var/app
RUN apt-get update

COPY ./git2md/requirements.txt .
COPY ./md2html/package.json .
COPY ./md2html/package-lock.json .
COPY mkdocs_theme /var/theme

RUN pip3 install -r requirements.txt \
    && npm i -g html-pdf-chrome

RUN cd /var/theme && \
    pip3 install .

COPY ./entrypoint.sh .

ENTRYPOINT [ "/bin/sh", "/var/app/entrypoint.sh" ]