#!/bin/bash -e

# Used to iterate through and test different configurations by calling other scripts
# TODO: add following scripts

# check for network connection before running


# script to change configuration file being used
bash /configs/select_file.sh


# benchmark script (global path)
bash benchmark.sh

# result parsing script
python3 /home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Python_Scripts/parse_results.py


# kernel recompilation (add code to copy config file to correct folder)
make clean
make
make modules_install
make install


# reboot code

