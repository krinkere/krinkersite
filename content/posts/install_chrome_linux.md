Title: How to install Google Chrome on your Linux System
Date: 2018-05-29 8:51
Modified: 2018-05-29 9:01
Status: published
Category: How To article
Tags: linux, chrome
Slug: install_chrome_on_linux
Authors: Al Krinker
Summary: How to install Google Chrome on your Linux system

# Enable Google Yum repository
- Create a file called /etc/yum.repos.d/google-chrome.repo and add the following lines of code to it.
```commandline
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
```
# Install key
-Refer to this [guide](https://www.google.com/linuxrepositories/) for more details.
```commandline
$ wget --no-check-certificate https://dl.google.com/linux/linux_signing_key.pub
$ sudo rpm --import linux_signing_key.pub
```
# Install Google Chrome
```commandline
$ sudo yum install google-chrome-stable
```
# Start Google Chrome
```commandline
$ google-chrome &
```
