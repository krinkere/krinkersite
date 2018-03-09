Title: How to find a file containing particular text in Linux
Date: 2014-05-27 10:41
Modified: 2014-05-27 10:42
Status: published
Category: How To article
Tags: linux
Slug: How_to_find_a_file_containing_particular_text_in_Linux
Authors: Al Krinker
Summary: Use grep to find file containing particular text.

Here is a quick example:
```console
$ grep -r "text string to search” directory-path
```

To search for a string ‘logged in’ in all text (*.log) files located in /etc/networks/ directory for example, use:

```console
$ grep "logged in" /etc/networks/*.log
```

To search all subdirectories recursively, include -r option like so:

```console
$ grep -r "logged in" /etc/networks/*.log
```

The grep command prints the matching lines for each match. Pass -H option to print the filename only:

```console
$ grep -H -r "logged in" /etc/networks/*.log
```

To search for two or more words, use egrep:

```console
egrep -w -r 'logged in|logged out' /etc/networks/*.log
```

To hide warning spam of permission for certain directories being denied, etc, send them to dev/null:

```console
$ grep -w -r 'logged in|logged out' /etc/networks/*.log 2>/dev/null
```

To make it case insensitive, use -i option:

```console
$ grep -i "logged in" /etc/networks/*.log
```