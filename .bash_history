ifconfig
ping localhost
ifconfig -a
exit
ipconfig
ifconfig
ifconfig -a
ip link show
sudo nano /etc/network/interfaces
N
ip link show
sudo nano /etc/network/interfaces
ifconfig -a
sudo nano /etc/network/interfaces
more /etc/network/interfaces
sudo reboot now
sudo apt install wget
ifconfig
sudo apt update
sudo apt upgrade
shutdown -h now
more /etc/hosts
clear
ifconfig
ls
pwd
ls -ltr
shutdown now
                                                                                                               clear
more /etc/network/interfaces
ping 10.10.2.6
ping 10.10.2.7
sudo apt-get update
sudo apt-get install default-jdk
java -version
wget http://ftp.heanet.ie/mirrors/www.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
tar -xzvf hadoop-3.1.2.tar.gz
sudo mv hadoop-3.1.2 /usr/local/hadoop
#readlink -f /usr/bin/java  sed @s:bin/java::"
#readlink -f /usr/bin/java sed @s:bin/java::"
cat /etc/hosts
shutdown -h now
readlink -f /usr/bin/java | sed "s:bin/java::"
sudo nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh
more  /usr/local/hadoop/etc/hadoop/hadoop-env.sh
/usr/local/hadoop/bin/hadoop
mkdir ~/input
cp /usr/local/hadoop/etc/hadoop/*.xml ~/input
cd input/
ls
ls -l
more yarn-site.xml
more mapred-site.xml
cd /usr/local/hadoop/share/hadoop/mapreduce/
ls
ls -l
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.2.jar grep ~/input ~/grep_example 'compliance[.]*'
cat ~/grep_example/*
cd ~/grep_example/
ls
ls -l
more part-r-00000 
more _SUCCESS 
ping -c 2 ubuntuvm1
ping -c 2 ubuntuvm2
ping -c 3 ubuntuvm2
more /etc/hosts
cd ..
ifconfig -a
exit
systemctl start nginx
systemctl start corosync
systemctl start pacemaker
crm status
systemctl enable corosync
sudo su -
exit
sudo su -
sudo su-
sudo su -
shutdown -h now
exit
sudo su -
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu xenial main'
sudo apt-get update
clear
sudo apt-get install mariadb-server
sudo apt-get install rsync
sudo nano /etc/mysql/conf.d/galera.cnf
more /etc/mysql/conf.d/galera.cnf
sudo ufw status
sudo ufw allow 3306,4567,4568,4444/tcp
sudo ufw allow 4567/udp
sudo systemctl stop mysql
sudo systemctl status mysql
sudo galera_new_cluster
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
clear
sudo nano /etc/mysql/debian.cnf
more /etc/mysql/debian.cnf
sudo more /etc/mysql/debian.cnf
sudo cat /etc/mysql/debian.cnf
mysql -u debian-sys-maint -p
clear
shutdown -h now
shutdown
sudo reboot now
clear
scp -P 61022 /Users/harinathselvaraj/Documents/datascience/insurance/insure-sample.zip student@localhost:/home/student/
exit
ls
ls -ltr
unzip insure-sample.zip 
sudo apt install unzip
clear
ls -ltr
unzip insure-sample.zip 
ls -ltr
cd insure-sample/
ls
cd ..
clear
ls -ltr
sudo pip3 install --upgrade awscli
sudo apt update
sudo apt install python3-pip
sudo pip3 install --upgrade awscli
export LC_ALL=C
sudo pip3 install --upgrade awscli
ls -l
cd insure-sample/
ls
ls -l
eb init
aws --version
sudo apt-get install python3.4
aws --version
python --version
python3 --version
eb --version
cd ..
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
ls -a ~
export PATH=LOCAL_PATH:$PATH
source ~/PROFILE_SCRIPT
pip --v
pip --version
pip install awsebcli --upgrade --user
eb --version
pip install awsebcli
ls
cd insure-sample/
virtualenv
virtualenv virt
pip install virtualenv
sudo pip install virtualenv
pip install virtualenv --user
virtualenv virt
source virt/bin/activate
pip install flask==1.0.2
pip freeze
pip freeze > requirements.txt
eb --version
pip install awsebcli --upgrade --user
cd ..
exit
pip install awsebcli --upgrade --user
sudo apt-get remove 'python3.*'
ls -ltr
pip install awsebcli --upgrade --user
pip --version
python2 get-pip.py --user
pip --version
pip install awsebcli --upgrade --user
eb --version
clear
cd insure-sample/
ls
vi .ebignore
git init
eb init
clear
ls
cd ..
ls -ltr
mv -r insure-sample insure-predict
mv insure-sample insure-predict
cd insure-predict/
ls -ltr
git status
git add -A
git commit -m "initial version"
ls -ltr
git push -u origin master
git push -u https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/insure-predict master
c00235324
git push -u https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/insure-predict master
ls
git add -A
git status
cd ..
ls
ls -l
rm insure-sample.zip
zip insure-predict
zip -r insure-predict.zip insure-predict/
sudo apt-get install zip
zip -r insure-predict.zip insure-predict/
ls -l
cd insure-predict/
ls
rm virt/
rm -r virt/
cd ..
rm insure-predict.zip 
zip -r insure-predict.zip insure-predict/
ls -l
cd insure-predict
ls
ls -l
eb init
cd .elasticbeanstalk
ls
more config.yml 
cd ../
mkdir .ebextensions
cp .elasticbeanstalk/config.yml .ebextensions/
cd .ebextensions/
ls
more config.yml 
cd ..
eb deploy
clear
cd ..
ls -ltr
rm Enna_Sona.mp3 
rm hari.do 
clear
mysql
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
sudo systemctl status mysql
sudo galera_new_cluster
systemctl status mariadb.service
sudo systemctl stop mysql
sudo systemctl status mysql
sudo galera_new_cluster
journalctl -xe
sudo ufw allow 3306,4567,4568,4444/tcp
sudo ufw status
sudo apt-get install ufw
sudo ufw status
sudo ufw enable
sudo ufw status
sudo ufw allow 3306,4567,4568,4444/tcp
sudo ufw allow 4567/udp
sudo systemctl status mysql
sudo systemctl stop mysql
sudo galera_new_cluster
more /var/lib/mysql
cd /var/lib/mysql
ls
ls -l
cd ~
mysql_install_db
sudo mysql_install_db
sudo galera_new_cluster
sudo systemctl stop mysql
sudo mysql_install_db
sudo systemctl stop mysql
sudo galera_new_cluster
systemctl status mariadb.service
sudo galera_new_cluster1
more grastate.dat
cd /var/lib/mysql
ls
ls -l
more grastate.dat
sudo vi grastate.dat
sudo galera_new_cluster
mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_cluster_size'"
mysql -u root -p 
exit;
ls
cd insure-predict/
ls
cd ..
rm insure-predict
rm -r insure-predict
ls
ls -lltr
rm insure-predict.zip 
cd ¬
more /etc/resolv.conf
more /etc/hosts.allow
vi /etc/hosts.allow
clear
sudo vi /etc/hosts.allow
#sudo netstat -tnlp 
##sudo netstat -tnlp 
#~
clear
ls -ltr
ls
cd insure-predict/
ls
rm templates/
rm -r templates/
rm -r application.py 
rm -r README
ls
rm requirements.txt 
cd ..
rm -r insure-predict/
rm -f insure-predict/
rm -f -r insure-predict/
;s
ls 
git clone https://github.com/harinathselvaraj/loan-defaulter-predict.git
ls
git clone https://github.com/harinathselvaraj/loan-defaulter-predict.git
ls
rm -r loan-defaulter-predict/
rm -r -f loan-defaulter-predict/
git clone https://github.com/harinathselvaraj/loan-defaulter-predict.git
git status
cd loan-defaulter-predict/
git init
git add -A
git commit -m "Initial version"
git push -u https://git-codecommit.us-east-2.amazonaws.com/v1/repos/loan-defaulter-predict master
cd ..
rm -r -f loan-defaulter-predict/
git push -u https://git-codecommit.us-east-2.amazonaws.com/v1/repos/loan-defaulter-predict master
git clone https://github.com/harinathselvaraj/loan-defaulter-predict.git
cd loan-defaulter-predict/
ls
more README
git init
git add -A
git commit -m "Initial version"
git push -u https://git-codecommit.us-east-2.amazonaws.com/v1/repos/loan-defaulter-predict master
exit
clear
ls -ltr
sudo nano /etc/hosts.deny
o
sudo nano /etc/hosts.allow
sudo iptables -L -line-number
sudo more /etc/fail2ban/jail.conf
sudo nano /etc/fail2ban/jail.conf
cd .ssh
ls
more known_hosts 
vi known_hosts 
more known_hosts 
sudo nano known_hosts 
more known_hosts 
sudo service ssh restart
exit
