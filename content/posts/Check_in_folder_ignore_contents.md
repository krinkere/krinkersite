Title: How to check in a folder, but ignore its contents
Date: 2016-09-08 10:52
Modified: 2018-03-16 14:08
Status: published
Category: How To article
Tags: git
Slug: check_in_folder_ignore_contents
Authors: Al Krinker
Summary: Check in folder into git, but ignore any contents in it (massive logs, models, etc)

Git does not let you to check in an empty folder, even if you are using it as a temp output location. How to work around it?

In the folder that you are trying to commit, create <b>.gitignore</b> file and add following content
>&ast;<br/>
>&ast;/<br/>
>!.gitignore

then add it to the git
```console
$ git add .gitignore
```
The &ast; line tells git to ignore all files in the folder, but !.gitignore tells git to still include the .gitignore file. This way, your local repository and any other clones of the repository all get both the empty folder and the .gitignore it needs.
May be obvious but also add &ast;/ to the git ignore to also ignore sub folders.