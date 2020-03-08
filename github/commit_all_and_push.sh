echo this script will commit all the changes and push to the remote origin
# require input commit message
git status
git add -A
git commit -m "$1"
git push
