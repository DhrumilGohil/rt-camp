FROM ubuntu:latest
RUN apt-get update && \
apt-get install -y rsync openssh-client
# Set the working directory inside the container
# WORKDIR /app
COPY script.sh script.sh
RUN chmod +x script.sh
RUN mkdir github
COPY . github
ENTRYPOINT ["/script.sh"]
