#!/bin/bash -e

# Used to iterate through and test different configurations by calling other scripts
# TODO: add following scripts

# check for network connection before running


# script to change configuration file being used
fin="$PWD/finished.txt"

if [ -e $fin ]; then
	echo "no more configurations" > $fin
	exit 1
else
	bash select__until_empty.sh
fi


# benchmark script (global path)
bash benchmark.sh

# result parsing script
python3 /home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Python_Scripts/parse_results.py


# kernel recompilation (add code to copy config file to correct folder)
make clean -C /home/qemukvm/Unikernel_optimisation-Lupine-Linux-/Code/linux-5.16.7
make -C /home/qemukvm/Unikernel_optimisation-Lupine-Linux-/Code/linux-5.16.7
make modules_install -C /home/qemukvm/Unikernel_optimisation-Lupine-Linux-/Code/linux-5.16.7
make install -C /home/qemukvm/Unikernel_optimisation-Lupine-Linux-/Code/linux-5.16.7


# reboot code
# sysctl