#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
#apt-get -y update
#command -v nginx >> /dev/null || apt-get install nginx

mkdir -p /data/
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" >> /data/web_static/releases/test/index.html

# Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/
#
NEW_LOCATION="\\\n\n\tlocation /hbnb_static/ {\n\t\talias /dat/web_static/current/;\n\t}"
sed -i '47i'"$NEW_LOCATION" /etc/nginx/sites-available/default

# Restart nginx
service nginx restart
