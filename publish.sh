#!/bin/bash

PELICAN=/usr/bin/pelican
CONTENT=/home/basepi/Dropbox/Blogs/blog.basepi.net/content
OUTPUT=/home/basepi/Dropbox/Blogs/blog.basepi.net/output
SETTINGS=/home/basepi/Dropbox/Blogs/blog.basepi.net/publishconf.py

rm -rf /home/basepi/Dropbox/Blogs/blog.basepi.net/output/*
$PELICAN $CONTENT -o $OUTPUT -s $SETTINGS || exit $?
rsync -r --delete /home/basepi/Dropbox/Blogs/blog.basepi.net/output/ /var/www/blog.basepi.net
