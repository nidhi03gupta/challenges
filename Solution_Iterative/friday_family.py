import sys, random

def generate_random_groups(employee_list):
	"""
	Uses employees in employee_list to create random groups
	:param employee_list: list of employees who needs to become part of a group
	:return:a list with sub-list of employees
	"""
	output_list = []
	updated_employee_list = employee_list
	for i in range(len(employee_list)/5):
		# randomly create a group of size random_list_size
		random_list = random.sample(updated_employee_list, 5)

		# Ignoring the employees that are already picked
		updated_employee_list = [item for item in updated_employee_list if item not in random_list]

		# append newly created group "random_list" to output_list
		output_list.append(random_list)

	len_updated_list = len(updated_employee_list)

	if len_updated_list > 0 and len_updated_list < 3:
		updated_employee_list.append(output_list[0][-1])
		output_list[0].pop()
		updated_employee_list.append(output_list[0][-1])
		output_list[0].pop()

	if len_updated_list > 0:
		# create a new list for remaining employee and append that list to output_list
		output_list.append(updated_employee_list)

	# return the final output_list
	return output_list

def read_input_file(inputfile):
	"""
	Reads the input file that contains all the employees in the company with one employee per line
	:param inputfile: fully qualified path to input file
	:type inputfile: string
	"""
	employee_list = []
	try:
		# open and read the content of input file
		with open(inputfile, 'rb') as f:
			# Skipping the header line in input file
			first_line = f.readline()
			# append each line of input file as new item to employee_list
			for employee in f:
				if not employee.isspace():
					employee_list.append(employee.strip(' '))
	except IOError:
		print "Error: can\'t find file or read data"
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise

	# create employee groups only if there are more than 5 employee in the company
	if len(employee_list) > 5:
		print employee_list
		# call generate_random_groups method that returns random groups
		random_groups = generate_random_groups(employee_list)
		count = 1
		for group in random_groups:
			print 'Group' + str(count) + ':\n' + ''.join(group)
			count+=1
			if len(group) < 3:
				print ('group size is: ' + str(len(group)))
				print ('group size validation fails')
				sys.exit()
	else:
		 print ('Total number of employee in company is less than or equal to 5. Distribution of employee into multiple groups will not be done.')
		 print ('Below is the only group that can be created:')
		 print ''.join(employee_list)

# Script execution starts below
try:
	# if first argument passed to python script is generate_random_groups then read_input_file method will be called
	if (sys.argv[1] == 'generate_random_groups'):
		read_input_file(sys.argv[2])

	# if first argument passed to python script is add_new_member then new employee will be appended to employee file
	elif (sys.argv[1] == 'add_new_member'):
		with open(sys.argv[2], "a") as employeefile:
			employeefile.write('\n' + sys.argv[3])
	else:
		print 'Please provide expected input arguments.'
except:
	print "Unexpected error:", sys.exc_info()[0]
	raise
