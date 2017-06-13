import sys, random

def generate_random_groups(employee_list, output_list=[]):
	"""
	Uses employees in employee_list to recursively create random groups
	:param employee_list: list of employees who needs to become part of a group
	:param output_list: list of employee groups, initial default value is an empty list
	:return:a list with sub-list of employees
	"""

	# default size of each random group that will be created is 5
	random_list_size = 5

	# if number of employee in employee list is less than or equal to 7 then allowed size of groups will be 3, 4
	if len(employee_list) <= 7:
		random_list_size = 3

	# randomly create a group of size random_list_size
	random_list = random.sample(employee_list, random_list_size)

	# create another list "updated_employee_list" that has employees: employee_list - random_list
	updated_employee_list = [item for item in employee_list if item not in random_list]

	# append newly created group "random_list" to output_list
	output_list.append(random_list)

	len_updated_list = len(updated_employee_list)

	# if there are more than 5 employee in the updated_employee_list, then recursively call generate_random_groups
	if len_updated_list > 5:
		generate_random_groups(updated_employee_list, output_list)

	# if number of employees in updated_employee_list is between 0 and 5, then simply append those employees to output_list
	elif len_updated_list > 0 and len_updated_list <= 5:
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
		 print ('Total number of employee in company is less than 5. Distribution of employee into multiple groups will not be done.')
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
