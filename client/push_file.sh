#/bin/bash

#Expected arguments: ./push_file.sh GIT_USER REPO_NAME FILE

cd /tmp
git clone git@github.com:"$1"/"$2"
cd -
cp "$3" /tmp/"$2"
cd /tmp/"$2"
git add *
git commit -m"$3"
git push origin master