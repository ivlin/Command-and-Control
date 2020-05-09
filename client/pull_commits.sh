#/bin/bash

#Expected arguments: ./pull_commits.sh GIT_USER REPO_NAME FILE

cd /tmp
git clone git@github.com:"$1"/"$2"
cd -
cd /tmp/"$2"
git log > commitlog
cd -
cp /tmp/"$2"/commitlog .