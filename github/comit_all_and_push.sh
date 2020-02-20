# this script will commit all the changes and push to the origin
git status
git add -A
git commit -m "$1"
git push
