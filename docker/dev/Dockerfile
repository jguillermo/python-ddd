FROM python:3.6.5-slim

# Install Python, tools

RUN apt-get update && apt-get install -y --no-install-recommends \
    python-dev \
    git \
    gcc \
    default-libmysqlclient-dev \
    unzip

ADD resources /resources/
RUN python --version
RUN chmod +x /resources/test.sh

WORKDIR /resources/
RUN pip install -r ./requirements.txt

ONBUILD ADD app /app/

WORKDIR /app

EXPOSE 80
ENTRYPOINT /resources/runservices.sh
