#!/usr/bin/env bash
# Sets up web servers for deployment
sudo apt -y update

# Install nginx if it doesn't already exist
command -v nginx || sudo apt -y install nginx

# Create folder /data/ if it don't already exist
mkdir -p /data/

# Create folder /data/web_static/ if it doesn’t already exist
mkdir -p /data/web_static/

# Create the folder /data/web_static/releases/ if it doesn’t already exist
mkdir -p /data/web_static/releases/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
FILE="/data/web_static/releases/test/index.html"
mkdir -p "$(dirname "$FILE")"
cat << EOF > "$FILE"
<html>
  <head>
  </head>
  <body>
    ALX Africa
  </body>
</html>
EOF

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx server
sudo service nginx restart
