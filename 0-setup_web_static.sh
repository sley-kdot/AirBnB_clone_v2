#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
apt-get -y update
command -v nginx >> /dev/null || apt-get install nginx

# Create the folder /data/ if it doesn’t already exist
mkdir -p data

# Create the folder /data/web_static/ if it doesn’t already exis
mkdir -p data/web_static

# Create the folder /data/web_static/releases/ if it doesn’t already exist
mkdir -p data/web_static/releases

# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p data/web_static/shared

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p data/web_static/releases/test

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "
<html>
  <head>
  </head>
  <body>
    'Hello, Kingsley!'
  </body>
</html>
" >> data/web/static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
ln -sf data/web_static/releases/test/ data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown ubuntu:ubuntu /data/
