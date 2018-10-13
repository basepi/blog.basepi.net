#!/bin/bash
make clean
make html
ghp-import output
git push git@github.com:basepi/basepi.github.io.git gh-pages:master -f
