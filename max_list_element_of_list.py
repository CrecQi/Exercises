#Input a list contains some lists and output the largest SUM with continual list-elements
#Please run it in terminal

from sys import argv
script, list_file = argv

lists = open(list_file)   
lists_len = len(lists)
SUM = 0
single_amount = 0

def SUM_ALL(a,b):
	return a+b

amount_list = []

for i in range(0,lists_len):
	list_i = lists.pop(0)
	list_in_lists_len = len(list_i)

	for loop in range(0,list_in_lists_len):
		single_amount = single_amount + list_i[loop]
	amount_list.append(single_amount)

print "The amount_list is %s" %amount_list

#Sum up all the elements in the amount_list and
#append it to the results_list
results_list = amount_list  				    
for i in range(0,len(amount_list)-1):		
	SUM = SUM + amount_list[i]
results_list.append(SUM)

for i in range(0,len(amount_list)-2):
	for loop in range(i+2,len(amount_list)+1):
		temp_list = amount_list[i:loop]
		SUM = reduce(SUM_ALL, temp_list)		#Sum all elements in temp_list
		results_list.append(SUM)


print max(results_list)

