apt-get update
apt-get install libxml2-dev libxslt1-dev python-dev
apt-get install libxml2-dev libxslt-dev python-dev
apt-get install python3-lxml
#apt-get install mysql-server
#apt-get install mysql-client
#apt-get install mysql-common
#apt-get install python-mysqldb 
pip install -r requirements.txt
cp robot/robot/settings_example.py robot/robot/settings.py
#mysqladmin -u root password 'lifemaker1989'
wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.0.0/elasticsearch-2.0.0.deb
dpkg -i  elasticsearch-2.0.0.deb
