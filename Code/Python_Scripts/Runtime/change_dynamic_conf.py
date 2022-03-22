# changing dynamic configuration
import random
import json
with open('/home/eugen/Unikernel_optimisation-Lupine-Linux-/Code/Parameters_lists_JSON/runtime_params.json') as parameters:
	runtime = json.loads(parameters.read())




def write_to_file(filepath, value, op):
	checked = open(filepath, op)
	checked.write(str(value))
	checked.write("\n")
	checked.close()


def list_from_range(excl, start, end, lis):
	x = start
	while x < end:
		x = x + 1
		if x not in excl:
			lis.append(x)


def list_from_file(fp, ls_out):
	fh = open(fp, 'r')
	inter = fh.read()
	
	ls_out = inter.split("\n")
	del ls_out[len(ls_out) - 1]
	
	return ls_out


def handle_data_type(dict_item):
	t = dict_item["type"] 
	
	if t == "bool":
		pass
	if t == "list":
		pass
	if t == "double":
		exclude_list = []
		fp = "dynamic_configs/checked_int_" + dict_item["name"] + ".txt"
		exclude_list = list_from_file(fp, exclude_list)
		
		for i in range(0, len(exclude_list)):
			exclude_list[i] = int(exclude_list[i])
		
		check = []
		list_from_range(exclude_list, dict_item["range"][0], dict_item["range"][1], check)

		if check != []:
			val = int(random.choice(check))
			dict_item["value"] = val
			write_to_file('dynamic_configs/checked_int_' + dict_item["name"] + '.txt', val, 'a')


def read_trial_no(fp, trials):
	trials = list_from_file(fp, trials)
	return trials[0]




position = []
position = list_from_file('current_runtime_param.txt', position)


for i in range(0, len(position)):
	l = position[i].split(" ")
	position[i] = l
	
try:
	fp = open('dynamic_configs/checked_int_' + runtime[position[0][0]][position[0][1]]["name"] + '.txt', 'x')
	fp.close()
	write_to_file(('dynamic_configs/checked_int_' + runtime[position[0][0]][position[0][1]]["name"] + '.txt'), runtime[position[0][0]][position[0][1]]["default"], 'a')

except:
	OSError



trials = []
trial_no = read_trial_no("trial_no.txt", trials)
trial_no = int(trial_no)



if runtime[position[0][0]][position[0][1]]["range"][1] - runtime[position[0][0]][position[0][1]]["range"][0] < 10000:
	tests = runtime[position[0][0]][position[0][1]]["range"][1] - runtime[position[0][0]][position[0][1]]["range"][0]
	
	
	if trial_no < tests:
		runtime[position[0][0]][position[0][1]]["value"] = runtime[position[0][0]][position[0][1]]["default"]
	
		handle_data_type(runtime[position[0][0]][position[0][1]])
		
		trial_no = trial_no + 1
		write_to_file("trial_no.txt", trial_no, 'w')
	
	else:
	
		del(position[0])
		open('current_runtime_param.txt', 'w').close()
		
		for i in position:
			s = i[0] + " " + i[1]
			write_to_file('current_runtime_param.txt', s, 'a')
		trial_no = 0
		write_to_file("trial_no.txt", trial_no, 'w')
		
		
else:

	if int(trial_no) < 10000:
		runtime[position[0][0]][position[0][1]]["value"] = runtime[position[0][0]][position[0][1]]["default"]
	
		handle_data_type(runtime[position[0][0]][position[0][1]])
		
		trial_no = trial_no + 1
		write_to_file("trial_no.txt", trial_no, 'w')
	
	else:
	
		del(position[0])
		open('current_runtime_param.txt', 'w').close()
	
		for i in position:
			s = i[0] + " " + i[1]
			write_to_file('current_runtime_param.txt', s, 'a')
		trial_no = 0	
		write_to_file("trial_no.txt", trial_no, 'w')


# subprocess.run([""])	# add path to shell script for runtime parameters
