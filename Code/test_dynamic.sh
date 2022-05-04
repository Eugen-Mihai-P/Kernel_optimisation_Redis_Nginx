#!/bin/bash -e


wdir=$PWD
run=("$wdir"/Python_Scripts/Runtime)


# if the files tracking tested values and current runtime parameters exists change value
# otherwise create the file
if test -f "$run"/current_runtime_param.txt; then
	(cd "$run" && python3 change_dynamic_conf.py)
else
	(cd "$run" && python3 track_param.py)
fi
cd "$wdir"


# read first item of integer_tracking folder, current runtime parameter
# change configuration accordingly and benchmark
param=("$run"/current_runtime_param.txt)

if test -f "$param"; then
	# echo "$param exists "
	line=$(cat "$param")
	read -ra param_name <<< "$line"
	
	while read -ra value; do
    		val="$value"
	done <"$run"/integer_tracking/"checked_int_${param_name[1]}.txt" 
	
	
	IFS="."
	read -ra folder_arr <<< "${param_name[1]}"
	
	folder="/proc/sys"
	
	for i in "${folder_arr[@]}"; do
		tmp="/$i"
		folder+=$tmp
	done
	
	echo "$folder"
	# echo "$val"
	# echo $(cat /proc/sys/"$folder")
	# TODO check running commands that require admin permission
	echo "$val" > "$folder"

fi
# reboot
