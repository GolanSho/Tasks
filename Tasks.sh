#!/usr/env/bin bash

#######################
#
# Made: GolanSho
#
# Date: 04/11
#
# Ver: 1.0
#
# Description: Task For interview
#
########################

###   Prep   ###

curr_dir_con=$(ls |grep ".ext")
cpu_use=$(ps aux --no-heading | awk '{cpu_use +=$3};END{print cpu_use}')
cpu_no_root=$(ps aux --no-heading |grep -v root | awk '{cpu_use +=$3};END{print cpu_use}')
dist=$(sed -n -e '/PRETTY_NAME/ s/^.*=\|"\| .*//gp' /etc/os-release)
PS3="Choose Task 1 ~ 5 "

###  Funcs & Commands   ###

               ###  Task 1 Change ext in files  ###

f_chng_end(){

  for i in $curr_dir_con;
    do if [ -f $i ]; then
	newi=$(echo $i |sed "s/\.ext/\.newExt/") &&
	mv $i ./$newi
       fi
  done
}

               ###  Task 2 Filtering ps aux out  ###

# echo "Total CPU used: $cpu_use"

# echo "Total CPU used By non-root: $cpu_no_root"

               ###  Task 3 apply changes to service  ###

f_sshd_rest(){

  printf "you need to be super-user to run\n

Restart the sshd service?\n
"
  read -p "y/n " ans

  if [ $ans = y ]; then
    sudo systemctl restart sshd &&
 echo "sshd restarted"
  fi
}

               ###  Task 4 package finder ###

# rpm -qf /bin/bash

               ### Task 5 Mach info  ###

#  printf "Machine dist: $(uname -o) $dist \n
# Kernel Ver: $(uname -v)"  


###   Main   ###
               ###  Setting Getopts  ###

f_getopts(){

  while getopts ":abcde" opt; do
    case $opt in
      a)
        f_chng_end
        ;;
      b)
        printf "Total CPU used: $cpu_use \n

Total CPU used By non-root: $cpu_no_root \n"
        ;;
      c)
        f_sshd_rest
        ;;
      d)
        rpm -qf /bin/bash
        ;;
      e)
        printf "Machine dist: $(uname -o) $dist \n
Kernel Ver: $(uname -v)"
        ;;
    esac

  done
}

               ###  Setting Select  ###

  select task in 1 2 3 4 5 exit
    do case $task in
    "1")
	 f_getopts -a
    ;;
    "2")
         f_getopts -b
    ;;
    "3")
         f_getopts -c
    ;;
    "4")
         f_getopts -d
    ;;
    "5")
         f_getopts -e
    ;;
    "exit")
         break
    ;;
    esac
   break
  done

