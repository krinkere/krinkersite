Title: Commit your changes or stash them before you can merge??!?!
Date: 2018-03-09 7:54
Modified: 2018-03-09 8:17
Status: published
Category: How To article
Tags: git
Slug: Commit_your_changes_or_stash_them_before_you_can_merge
Authors: Al Krinker
Summary: What to do when you are faced with 'Please, commit your changes or stash them before you can merge.' message from git as you are trying to get latest code off your remote repository

When trying to update your local copy from remote master copy, you will see following error

```console
$ git pull origin master
error: Your local changes to the following files would be overwritten by merge:
<list of files>
Please commit your changes or stash them before you merge.
Aborting
```

You have several options here

### Commit the change
```console
$ git add .
$ git commit -m "committing before the update"
```

### Stash them
```console
$ git stash
$ git stash pop
```
### Overwrite local changes
```console
git reset --hard
```