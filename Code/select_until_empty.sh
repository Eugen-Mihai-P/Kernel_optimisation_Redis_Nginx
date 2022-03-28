#!/bin/bash

dir="$USER"
wdir="$PWD"

files=("$wdir"/configs/*)			#add test for empty folder and run generation script if necessary


if [ $files != "$wdir/configs/*" ]; then
	cp "${files[0]}" "/home/"$dir"/Unikernel_optimisation-Lupine-Linux-/Code/linux-5.16.7/.config"	# path to kernel config file
	rm -f $files
else
	touch finished.txt
	exit 1
fi