#!/usr/bin/env bash
#create file

apt -y update
apt install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<h1>Holberton</h1>" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
