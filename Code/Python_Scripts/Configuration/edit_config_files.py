import json
import random


with open('/home/eugen/Project/Code/Parameters_lists_JSON/compile_time_params.json') as compile_params:
	exp_space = json.loads(compile_params.read())


def write_to_file(filepath, value):
	checked = open(filepath, "a")
	checked.write(str(value))
	checked.write("\n")
	checked.close()


def invert(value, inv_value):
	if value == "y":
		inv_value = "n"
	elif value == "n":
		inv_value = "y"


def list_from_range(excl, start, end, lis):
	x = start
	while x < end:
		x = x + 1
		if x not in excl:
			lis.append(x)


def create_excl(fp, ls_out):
	fh = open(fp, 'r')
	exclude = fh.read()
	ls_out = exclude.split("\n")
	del ls_out[len(ls_out) - 1]
	
	for i in range(0, len(ls_out)):
		ls_out[i] = int(ls_out[i])
		
	return ls_out


def handle_data_type(dict_m, dict_item):
	t = dict_item["type"]
	
	if t == "bool":
		if dict_item["default"] == dict_item["value"] or dict_item["value"] == "":
			invert(dict_item["default"], dict_item["value"])
	
		if dict_item["exclude"] != "":
			for i in dict_item["exclude"]:
				invert(dict_item["value"], dict_m[i]["value"])
	

	elif t == "int":
		exclude_list = []
		fp = "static_configs/checked_int_" + dict_item["name"] + ".txt"
		exclude_list = create_excl(fp, exclude_list)

		check = []
		list_from_range(exclude_list, dict_item["range"][0], dict_item["range"][1], check)

		if check != []:
			val = random.choice(check)
			dict_item["value"] = str(val)
			write_to_file('static_configs/checked_int_' + dict_item["name"] + '.txt', val)



def edit_config(out, dict_item):
	f = open("/home/eugen/Project/Code/configs/.config_RCU", "r")
	conf_list = f.readlines()
	f.close()


	for i in range(0, len(conf_list)):
		if(conf_list[i].find(dict_item["name"]) != -1):
			if dict_item["type"] == "bool":
				if dict_item["value"] == "y":
					conf_list[i] = dict_item["name"] + "=" + dict_item["value"]
				elif dict_item["value"] == "n":
					conf_list[i] = "# " + dict_item["name"] + " is not set"

			elif dict_item["type"] == "int":
				if dict_item["value"] != "":
					conf_list[i] = dict_item["name"] + "=" + dict_item["value"]
				elif dict_item["value"] == "":
					conf_list[i] = "# " + dict_item["name"] + " is not set"


	for i in conf_list:
		out.writelines(i)		
	out.close()


# iterate through parameter dict, holding state whenever a parameter is changed (using a file)
for i in exp_space:

	if exp_space[i]["type"] == "int":
		try:
			fp = open('static_configs/checked_int_' + exp_space[i]["name"] + '.txt', 'x')
			fp.close()
			write_to_file(('static_configs/checked_int_' + exp_space[i]["name"] + '.txt'), exp_space[i]["default"])

		except:
			OSError
			
	
		for j in range(exp_space[i]["range"][0], exp_space[i]["range"][1] + 1):
			handle_data_type(exp_space, exp_space[i])
			
			
			try:
				output = open('/home/eugen/Project/Code/configs/config' + exp_space[i]["name"] + str(j), 'x')
				output.close()
			except:
				OSError
					
			output = open('/home/eugen/Project/Code/configs/config' + exp_space[i]["name"] + str(j), 'w')
			edit_config(output, exp_space[i])


	handle_data_type(exp_space, exp_space[i])

	output = open('/home/eugen/Project/configs/.config' + exp_space[i]["name"], 'w')
	edit_config(output, exp_space[i])
