
FROM debian:stable-20250407

RUN	apt update && \
	apt install -y \
	python3 \
	python3-pip \
	python3.11-venv \
	curl \
	apt-transport-https \
	ca-certificates \
	gnupg && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv /app/py-env/effective-guacamole

RUN . /app/py-env/effective-guacamole/bin/activate && \
    pip install google-generativeai
