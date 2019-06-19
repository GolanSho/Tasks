#!/usr/bin/env bash


#####   Vars   #####

interfaces=$(ifconfig |grep -oP "^[^\s]*" |sed s/\://g)


#####   Funcs   #####

f_ip_list(){

    for i in $interfaces
      do
	ip=$(ip address show $i |grep -oP "inet (\d{0,3}\.?){4}")
	if [[ -n $ip ]];then
	  echo "$i : $ip"
	else
	  echo "$i have no ip"
	fi
    done
}

f_mac_list(){

    for m in $interfaces
      do
	mac=$(ip link show $m |grep -oP "(\w{2}\:?){6}" |sed -r '/(ff\:ff)|(00\:00\:00)/d')
	if [[ -n $mac ]];then
	  echo "$m : $mac"
	else
	  echo "$m have no mac"
	fi
    done
}

f_help(){

    if [[ -z $1 ]];then

echo ""
printf '_/-|# Welcome to Net Info Puller! #|-\_
=======================================

'
printf "  Usage: -n -i -m

        -n = Interfaces List
        -i = Ip Table
        -m = Mac Table

"
    fi
}


#####   GetOps   #####

    getopts ":nim" opt
	case $opt in
	    n)
	      echo "Interfaces: $interfaces"
	      ;;
	    i)
	      f_ip_list
	      ;;
	    m)
	      f_mac_list
	      ;;
	   \?)
	      f_help
	esac

#####   Main   #####


