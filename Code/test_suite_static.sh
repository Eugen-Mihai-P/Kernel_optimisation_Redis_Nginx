#!/bin/bash -e

# Used to iterate through and test different configurations by calling other scripts
# TODO: add following scripts


wdir=$PWD
# check for network connection before running

# while the list of dynamic configuration parameters has items run the dynamic config script and reboot (placed before kernel recompilation to repeat until all dynamic options tested with singular static configuration)
# check values in "current_runtime_param.txt" and repeat above until file empty
# also remove all files in "integer tracking" folder
change_dy="$wdir/Python_Scripts/Runtime/current_runtime_param.txt"


if [ -s "$change_dy" ]; then
	bash "$wdir"/test_dynamic.sh
	bash "$wdir"/benchmark.sh
	
	# reboot code
	/sbin/reboot
else
	python3 "$wdir/Python_Scripts/Runtime/track_param.py"
fi



# script to change configuration file being used
fin="$wdir/finished.txt"

if [ -e "$fin" ]; then
	echo "no more configurations" > $fin
	exit 1
else
	bash "$wdir"/select_until_empty.sh
fi


# benchmark script (global path?)
bash "$wdir"/benchmark.sh
# result parsing script
python3 "$wdir"/Python_Scripts/parse_results.py


# kernel recompilation (add code to copy config file to correct folder)
cp -v /boot/config-$(uname -r) /"$wdir"/linux-5.16.7/.config
make localmodconfig
make bzImage
make modules && make modules_install
make install
update-grub


# make clean -C /"$wdir"/linux-5.16.7
# make -C /"$wdir"/linux-5.16.7
# make modules_install -C /"$wdir"/linux-5.16.7
# make install -C /"$wdir"/linux-5.16.7


# reboot code
/sbin/reboot
