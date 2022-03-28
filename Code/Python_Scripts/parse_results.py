# Python script for cleanup of ".txt" results and parsing to JSON


# TODO
# Change global paths accordingly
# add input variables to make file names reflect the configuration changes
# change to include other apps (nginx)


import sys
argv = sys.argv[1:]

import json


substring = "requests per second"
res = open(argv[0] + 'redis_clean_results_' + argv[2] + '.txt', 'w+')


def clean_output_file(rows):
    for line in rows:
        line = line.rstrip()
        line = line.split(', ')
        line = line[0]
        
        if(line[len(line)-len(substring) : len(line)] == substring):
            res.write(line[:len(line) - len(substring)])
            res.write("\n")
    res.close()

    
# dictionary for results
data = {} 


def parse_clean_output(rows, dict):    
    for line in rows:
        line = line.rstrip()
        line = line.split(': ')
  
        if dict.get(line[0]) == None:
            dict[line[0]] = []
            dict[line[0]].append(line[1])
        else:
            dict[line[0]].append(line[1]) 


# main script
with open(argv[0] + 'redis_bench_results_' + argv[2] + '.txt', 'r+') as f:
    lines = f.readlines()
clean_output_file(lines)


with open(argv[0] + 'redis_clean_results_' + argv[2] + '.txt', 'r+') as f:
    lines = f.readlines()
parse_clean_output(lines, data)


with open(argv[1] + 'redis_' + argv[2] + '.json', 'w+') as outfile:
    json.dump(data, outfile)
