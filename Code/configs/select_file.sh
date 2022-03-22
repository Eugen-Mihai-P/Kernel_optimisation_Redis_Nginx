#!/bin/bash

files=(*)		#add test for empty folder and run generation script if necessary
cp "${files[0]}" /home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/linux-5.16.7/.config
rm -f "${files[0]}"
