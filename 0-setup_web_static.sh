#!/usr/bin/env bash
#Initial server setup for deploying web_static
#AirBnB clone

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo chmod go+w /data/web_static/releases/test/index.html
echo "AirBnB testing" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_ststic/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

echo "server {
        listen 80;
        listen [::]:80 default_server;
        root /var/www/html;
        add_header X-Served-By $HOSTNAME;
        index index.html;
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        error_page 404 /error.html;
        location /404 {
                root /var/www/html;
                internal;
        }
        location /hbnb_static/ {
                alias /data/web_static/current/;
        }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
