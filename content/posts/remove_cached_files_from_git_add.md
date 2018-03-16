Title: How to remove files added to git
Date: 2016-03-07 21:34
Modified: 2018-03-16 13:51
Status: published
Category: How To article
Tags: git
Slug: How_to_remove_files_added_to_git
Authors: Al Krinker
Summary: How to remove files added to git via git add . command

Imagine the situation where you wrote your code and then decided to add it to your git repo. Pretty easy right?

```console
$ git init
$ git add .
```
Before you commit, you want to see what's going to be committed. So you do
```console
$ git status
```
Now you see whole bunch of config and target files that have no business being in the repo. Not a problem, you can use .gitignore right? First remove what you added, create .gitignore file and you can re add again only source files.
```console
$ git rm -r .
```
create .gitignore with
> /target/&ast;&ast;<br/>
> .settings/&ast;&ast;<br/>
> .classpath<br/>
> .project<br/>

and re-add
```console
$ git add .
```
Check what's about to be committed... and what?!?!? old files? How can this be? Did I messed up my regex? spelled gitignore wrong or forgot the leading period? Nope, everything seems correct...

After reading gitignore help guide... you need to clear your cache!!! Here is what you do
```console
$ git rm -r --cached .
```
cached flag is the key difference.

After this command, re-add, verify and finally commit:
```console
$ git add .
$ git commit -m "source files only!!!"
```
