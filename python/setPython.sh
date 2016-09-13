# Copyright @ 2016 darkframexue 
# date: 2016/9/13 
# version: 0.0.0

# Install Flask
echo "set up python extensions..."
echo "set up flask:"

sudo pip3 install Flask
sudo pip3 install Flask-SQLAlchemy \
Flask-WTF \
Flask-Login \
Flask-OpenID \
rauth # rauth is a module for authentication and authenrization

# check
clear
pip3 list | grep lask
sleep 3


# Install database surport
echo "Install MySQL and mongoDB..."
# install MySQL and check
sudo apt-get install mysql-server
clear
mysql -V
sleep 2
sudo pip3 install mysql-connector-python

# install mongoDB and check
sudo apt-get install mongodb
clear
mongo --version
sleep 2
sudo pip3 install pymongo


# Computer vision
echo "Install computer vision extensions..."
sudo pip3 install numpy \
scipy \
matplotlib
