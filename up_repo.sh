#!/bin/sh
# Script to auto git repo
# msg should be input without quout marks
#
# Remain tasks:
# should check if git folder was init
# if not: git init
#
msg=$1
gitDir=".git"
if [ ! -d $gitDir ];then
	git init
else
	echo "Adding and Committing to ur repo..."
fi
git rm *~ *#
git add *
git commit -m $msg
git push -u origin main
git status
