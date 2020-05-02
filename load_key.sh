#/bin/bash

#Expected arguments: ./load_key.sh key_name

mkdir ~/.ssh
cp ./id_rsa ~/.ssh/"$1"
chmod 0600 ~/.ssh/"$1"
cp ./id_rsa.pub ~/.ssh/"$1".pub
eval `ssh-agent`
ssh-add ~/.ssh/"$1"