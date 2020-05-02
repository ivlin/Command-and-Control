#/bin/bash

mkdir ~/.ssh

cp ./id_rsa ~/.ssh/id_rsa_1
chmod 0600 ~/.ssh/id_rsa_1
cp ./id_rsa.pub ~/.ssh/id_rsa_1.pub

#eval "$(ssh-agent -s)"

eval `ssh-agent`

ssh-add ~/.ssh/id_rsa_1