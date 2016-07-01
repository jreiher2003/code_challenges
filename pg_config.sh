#!/usr/bin/env bash
echo "****** Provisioning virtual machine... ******"
sudo apt-get -qqy update 
sudo apt-get -qqy upgrade
sudo apt-get -qqy install git 


wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
wget https://www.udacity.com/api/nodes/3333158951/supplemental_media/bash-profile-course/download

cat download >> .bashrc
rm download


echo "******************** git configs **********************"
git config --global user.name "Jeff Reiher"
git config --global user.email "jreiher2003@yahoo.com"
git config --global push.default upstream 
git config --global merge.conflictstyle diff3
git config --global credential.helper 'cache --timeout=10000'
echo "*********** done ************************"


