#!/bin/bash -e

# TODO: add other app (Nginx) benchmark and change default values of command line arguments



# command line arguments (for testing purposes, when runing script independently)

# redis-benchmark parameters

parallel_conn=${1:-50}	# -c
req_no=${2:-1024}	# -n
data_size=${3:-16}	# -d

# script specific parameters
test_number=${4:-64}
wdir=$PWD


# path variables

file_c=(configs/*)
save_loc_txt=("$wdir"/out_text/)
save_loc_JSON=("$wdir"/out_JSON/)


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
	    app="redis"
	    path_txt="${save_loc_txt}${app}_bench_results_${file_c}.txt"

            echo "RESULTS SET" $i >> $path_txt
	    redis-benchmark -t set,get -q -c $conn -n $req -d $data_size >> $path_txt

	    # add apache-bench command (reuse n, c), using output file option
	    app="nginx"
	    path_txt="${save_loc_txt}${app}_bench_results_${file_c}.txt"
	    path_json="${save_loc_json}${app}_bench_results_${file_c}_${i}.data"

	    echo "RESULTS SET" $i >> $path_txt
	    ab -k -n $req -c $conn http://192.168.122.222/ >> $path_txt
	    # ab -n $req -c $conn -g $path_json http://192.168.122.222/ >> $path_txt    
        done
    fi
}


# main "function"
benchmark $parallel_conn $req_no $data_size $test_number
python3 Python_Scripts/parse_results.py $save_loc_txt $save_loc_JSON $file_c
