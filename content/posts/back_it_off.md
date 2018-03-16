Title: How to back off back to the earlier version of the code
Date: 2016-07-29 11:44
Modified: 2018-03-16 15:00
Status: published
Category: How To article
Tags: git
Slug: back_it_off
Authors: Al Krinker
Summary: How to get back to previous good commit

Say you are developing a new feature and you realize after few commits that you went off to a way different route that you suppose to and you need to back it up few commits and start over... this definitely would be a cleaner way vs trying to remove what was done manually. How to do it though?

Check out what you want and get rid of all that code...
```console
$ git reset --hard 0d3b7ac32
```
Then you would push it up
```console
$ git push origin +master
```
Pretty simple once you know it.