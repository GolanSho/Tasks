#!/usr/bin/env bash

# Install Deps

f_deps(){

deps="git libsmi21dbl smistrip libxslt1-dev python3.6-dev libevent-dev default-libmysqlclient-dev"

sudo yum update -y

for p in $deps; do
  sudo yum install -y $p
  if [ $? -eq 0 ]; then
    Installed=("${Installed[@]}" "$p")
  else
    Failed=("${Failed[@]}" "$p")
  fi
done

printf "Succsed: $Installed \n
Failed: $Failed \n
"
}

# Installing Conpot

f_install(){

mkdir Conpot

cd Conpot

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





