#!/usr/bin/env bash

# Install Deps

f_deps(){

deps="git libsmi2ldbl smistrip libxslt1-dev python3.6-dev libevent-dev default-libmysqlclient-dev python3-pip"

sudo apt-get update -y

for p in $deps; do
  sudo apt-get install -y $p
  if [ $? -eq 0 ]; then
    Installed=("${Installed[@]}" "$p")
  else
    Failed=("${Failed[@]}" "$p")
  fi
done

echo "Succsed: ${Installed[@]} "
echo "Failed: ${Failed[@]} "

}

# Installing Conpot

f_install(){

mkdir Conpot

cd Conpot

pip3 install virtaulenv

virtualenv --python=python3.6 conpot

source conpot/bin/activate

pip install --upgrade pip
pip install --upgrade setuptools
pip install cffi

pip install conpot

}


# Interface

PS3="Choose an Option "
options="Install_Deps Install_Conpot Exit"

select option in $options
  do case $option in
    "Install_Deps") f_deps ;;
    "Install_Conpot") f_install ;;
    "Exit") break ;;
     esac
  done





