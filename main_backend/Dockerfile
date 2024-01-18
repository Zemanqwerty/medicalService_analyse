
# start by pulling the python image
FROM --platform=linux/amd64 python:3.8-slim-buster as build

RUN #!/bin/bash
RUN #!/usr/bin/env python3

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app



# install the dependencies and packages in the requirements file
# RUN apt install python3-cffi
# RUN pip install --upgrade cffi==1.14.0
# RUN LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib" CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include" PKG_CONFIG_PATH="/opt/homebrew/opt/openssl@1.1/lib/pkgconfig" pip install psycopg2-binary
# RUN apk add libffi-dev
# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 5001

# configure the container to run in an executed manner
ENTRYPOINT ["python"]

CMD ["app.py"]