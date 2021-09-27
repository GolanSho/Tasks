# Docker based on Centos7
FROM centos:7

# Define env variable VERSION=1.2.0
ENV VERSION=1.2.0

# Install Python zip & unzip
RUN yum update -y
RUN yum install python3 zip unzip -y

# Copy zip_job.py into the image’s /tmp folder
COPY zip_job.py /tmp

# Once docker container is up run a command which will print OS type + verify the zip_job.py exists
CMD cat /etc/centos-release && if [ -f /tmp/zip_job.py ]; then echo "zip job exist"; else echo "zip job not exist"; fi

