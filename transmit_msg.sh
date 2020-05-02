#/bin/bash

#Expected arguments: ./transmit_msg.sh GIT_USER REPO_NAME MSG

#cd /temp
git clone git@github.com:"$1"/"$2"
cd "$2"
date >> commlog
git commit -m"$3"
git push origin master