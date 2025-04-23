
FROM debian:stable-20250407

RUN	apt update && \
	apt install -y \
	python3 \
	python3-pip \
	curl \
	apt-transport-https \
	ca-certificates \
	gnupg && \
	rm -rf /var/lib/apt/lists/*
