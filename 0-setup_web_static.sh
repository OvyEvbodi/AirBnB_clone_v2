#!/usr/bin/env bash
# Sets up web servers for the deployment of the web_static part of the AirBnb project


# Install nginx if not installed
if ! nginx -v >/dev/null 2>&1;then
    sudo apt-get update > /dev/null 2>&1;
    sudo apt-get install -y nginx > /dev/null 2>&1;

    sudo apt-get install -y nginx
fi;

# kill services running on port 80
for pid in $(sudo lsof -t -i :80); do
    sudo kill "$pid" > /dev/null 2>&1
done
sudo service nginx start;

# add nginx to firewall
sudo ufw allow "Nginx HTTP" > /dev/null 2>&1;
sudo ufw allow 80/tcp > /dev/null 2>&1;

# Create alias root directory for web_static content
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/;

# Create fake HTML index page
sudo chown ubuntu /var/www/html
echo "<html><head></head><body>Web static home page template</body></html>" | cat > /data/web_static/releases/test/index.html;

# change ownership of the "/data" directory
sudo chown -hR ubuntu:ubuntu /data/
ln -sf /data/web_static/releases/test/ /data/web_static/current;

# Configure nginx server to serve web static files
sudo sed -i '/^\s*root \/var\/www\/html;/s//&\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}/' /etc/nginx/sites-available/default;

# reload nginx
sudo nginx -s reload;
