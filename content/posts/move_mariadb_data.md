Title: How to move MariaDB data to another location
Date: 2018-05-30 12:25
Modified: 2018-05-30 13:05
Status: published
Category: How To article
Tags: mariadb, linux, database, system
Slug: move_mariadb_data
Authors: Al Krinker
Summary: Shows how to successfully move mariadb instance to another location

I was recently working on an instance of MariaDB where I loaded almost 200GB of data. My /var folder 
filled up almost to 90% and I got all sorts of warning logs about size limitations, etc. Before it turned into bigger issue, I decided to take proactive approach and move my data to another location.
## Useful command to check the size
```console
$ sudo du -sch *
```
## Verify current data directory location
```console
$ mysql -u root -p

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 10.1.33-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> select @@datadir;
+--------------------------+
| @@datadir                |
+--------------------------+
| /var/lib/mysql/ |
+--------------------------+
1 row in set (0.00 sec)

MariaDB [(none)]> exit
Bye
```
## Stop running mariadb instance
```console
$ sudo systemctl stop mariadb
$ sudo systemctl status mariadb
```
### Double check if instance is running (Force kill any rogue mysql processes) and check if port 3306 is still occupied
```console
$  ps -elf|grep mysql
$ netstat -apn | grep 3306
```
## Move data to new location and back up old instance
```console
$ sudo rsync -av /var/lib/mysql /mnt/big_data
$ sudo mv /var/lib/mysql /var/lib/mysql.bak
```
## Edit configuration files to change the defaults. 
```console
"/etc/my.cnf"
[mysqld]
datadir=/mnt/big_data/mysql/
socket=/mnt/big_data/mysql/mysql.sock

"/etc/my.cnf.d/client.cnf"
[client]
port=3306
socket=/mnt/big_data/mysql/mysql.sock
```
I also had to chmod  new directory, otherwise mariadb was failing since it could not write to the new location.
## Start it back up and make sure that new directory is in use
```console
$ sudo systemctl start mariadb
$ sudo systemctl status mariadb

$ mysql -u root -p
MariaDB [(none)]> select @@datadir;
+--------------------------+
| @@datadir                |
+--------------------------+
| /mnt/big_data/mysql/ |
+--------------------------+
1 row in set (0.00 sec)
```

[Partial Reference](https://www.digitalocean.com/community/tutorials/how-to-change-a-mariadb-data-directory-to-a-new-location-on-centos-7)