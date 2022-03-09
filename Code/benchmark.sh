#!/bin/bash -e

# TODO: add other app (Nginx) benchmark and change default values of command line arguments



# command line arguments (for testing purposes, when runing script independently)

# redis-benchmark parameters
parallel_conn=${1:-50}	# -c
req_no=${2:-1000}	# -n
data_size=${3:-4}	# -d

# script specific parameters
test_number=${4:-100}


# Script start
function benchmark(){
    local conn=$1
    local req=$2
    local data_size=$3
    local tests=$4

    if ping -c 1 localhost &> /dev/null
    then
       for i in $(seq 1 $tests)        # !!! possible issue if bash used
        do
            # (TEMP Note): change file path accordingly
            echo "RESULTS SET" $i >> ~/Unikernel_optimisation-Lupine-Linux-/Code/Redis_outputs_text/redis_bench_results.txt
            redis-benchmark -t set,get -q -c $conn -n $req -d $data_size >> ~/Unikernel_optimisation-Lupine-Linux-/Code/Redis_outputs_text/redis_bench_results.txt
        done
    fi
}


# main "function"
benchmark $parallel_conn $req_no $data_size $test_number
python3 Python_Scripts/parse_results.py
