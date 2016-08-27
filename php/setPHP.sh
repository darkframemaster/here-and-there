echo "set up PHP with apache and MySQL..."

# install basic options
echo "install php apache and mysql..."
sudo apt-get update
sudo apt-get install php7.0
sudo apt-get install apache2.0 libapache2-mod-php7.0
sudo apt-get mysql-server php7.0-mysql

# check the installations
echo "check the installations"
apache2 -v
php -v
mysql -V
sleep 3

# install extensions of php
# These extensions is required by Magento2
echo "install extensions of php..."
sudo apt-get install php7.0-fpm \
php7.0-intl \
php7.0-zip \
php7.0-gd \
php7.0-dom \
php7.0-curl \
php7.0-mbstring \
php7.0-mcrypt \
php7.0-soap \
php7.0-xml \
php7.0-xsl \
php7.0-json \
php7.0-iconv

# restart apache2
echo "restart server..."
sudo /etc/init.d/apache2 restart
