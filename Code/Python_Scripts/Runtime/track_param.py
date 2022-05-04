import json
with open('/home/eugen/Project/Code/Parameters_lists_JSON/runtime_params.json') as parameters:
	runtime = json.loads(parameters.read())


def write_to_file(filepath, value, op):
	checked = open(filepath, op)
	checked.write(str(value))
	checked.write("\n")
	checked.close()

	
open('current_runtime_param.txt', 'w').close()
for param in runtime.keys():
	for i in runtime[param].keys():
		try:
			fp = open('dynamic_configs/checked_int_' + runtime[param][i]["name"] + '.txt', 'x')
			fp.close()
			write_to_file(('dynamic_configs/checked_int_' + runtime[param][i]["name"] + '.txt'), runtime[param][i]["default"])

		except:
			OSError
			
		parameter_pos = open('current_runtime_param.txt', 'a')
		parameter_pos.write(param + " " + runtime[param][i]["name"])
		parameter_pos.write("\n")
