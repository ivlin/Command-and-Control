#/bin/bash

#Expected arguments: ./load_key.sh key_name path_to_keys 

mkdir ~/.ssh
cp "$2"/id_rsa ~/.ssh/"$1"
chmod 0600 ~/.ssh/"$1"
cp "$2"/id_rsa.pub ~/.ssh/"$1".pub
eval $(ssh-agent)
ssh-add ~/.ssh/"$1"
bash -i