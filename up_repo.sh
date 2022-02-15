#trying to auto git repo
msg=$1
git add *
git commit -m $msg
git push -u origin main
