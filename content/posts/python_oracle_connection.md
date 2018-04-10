Title: How to connect to remote Oracle database from your python script
Date: 2018-04-10 10:29
Modified: 2018-04-10 10:30
Status: published
Category: How To article
Tags: python, oracle
Slug: connect_to_oracle_via_python
Authors: Al Krinker
Summary: How to set up your Linux environment to be able to connect to remote Oracle database from local Python script

Not sure if this step is needed since Oracle Instant Client suppose to be back compatible, but I went ahead and installed client that matched Oracle instance that I was trying to connect to
Determine Oracle version by running this command. Mine was 12.1.0.2.0
```console
SELECT * FROM V$VERSION
```
- Download [Oracle Instant Client](http://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html).
I have Linux 86-64 so I used this [link](http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html) to download RPM version.

- Install downloaded oracle instant client
```commandline
sudo yum install oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
```
- Add oracle instant client to your PATH. Permanently since I don't have any other Oracle products that might have broken.:
```commandline
sudo sh -c "echo /usr/lib/oracle/12.1/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf"
sudo ldconfig
```
- At this point your environment is set. Now it is time to connect to it by installing cx_Oracle library in your python.
```commandline
python -m pip install cx_Oracle --upgrade
```
- That should do it. Now write a simple python script to get the version of the Oracle database that you are trying to connect to.
```python
import cx_Oracle
ip = 'specify_ip_or_hostname'
port = 1234
SID = 'specify_sid_or_schema'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)

# You might get these via environment variable to make thing secure
username = 'username'
password = 'password'

conn = cx_Oracle.connect(username, password, dsn_tns)

print(conn.version)
conn.close()
```
    
```commandline
>>> 12.1.0.2.0
```
References:<br>
[Installing cx_Oracle on Linux](http://cx-oracle.readthedocs.io/en/latest/installation.html#oracle-instant-client-rpms)<br>
[Quick cx_Oracle Install](http://cx-oracle.readthedocs.io/en/latest/installation.html#quick-start-cx-oracle-installation)