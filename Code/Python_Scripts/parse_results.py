# Python script for cleanup of ".txt" results and parsing to JSON


# TODO
# Change global paths accordingly
# add input variables to make file names reflect the configuration changes
# change to include other apps (nginx)



import json


substring = "requests per second"
res = open('/home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Redis_outputs_text/redis_clean_results.txt', 'w')


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
with open('/home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Redis_outputs_text/redis_bench_results.txt', 'r') as f:
    lines = f.readlines()
clean_output_file(lines)


with open('/home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Redis_outputs_text/redis_clean_results.txt', 'r') as f:
    lines = f.readlines()
parse_clean_output(lines, data)


with open('/home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Redis_outputs_JSON/redis_benchmark.json', 'w') as outfile:
    json.dump(data, outfile)
