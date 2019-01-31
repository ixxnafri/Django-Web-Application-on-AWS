# Use official Debian sid runtime as a parent image
FROM node:9
EXPOSE 80

# Set the working directory
WORKDIR /usr/src/app

# Environment for RDS
ENV RDS_DB_NAME cs436
ENV RDS_HOSTNAME cs436-db.cwf9oicgjnlk.us-east-2.rds.amazonaws.com
ENV RDS_PASSWORD wulindiaoman
ENV RDS_PORT 3306
ENV RDS_USERNAME root

# Copy the current directory to the container
COPY . .
RUN uname
# Install python, npm and mysql
RUN apt update \
    && apt install -y \
    memcached \
    npm \
    python3 \
    python3-dev \
    python3-pip \
    nginx \
    libmemcached-dev \
    zlib1g-dev \
    build-essential \
    && pip3 install -r requirements.txt \
    && rm -rf /etc/nginx/sites-enabled \
    && mkdir /etc/nginx/sites-enabled \
    && cp cloud_net_nginx.conf /etc/nginx/sites-enabled/

    
# Start webapp
ENV PYTHONUNBUFFERED 0
CMD /etc/init.d/nginx restart && npm install webpack && npm install && npm run build && npm start
