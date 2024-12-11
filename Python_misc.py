
A = [0, 1, 3, 4, 5]

def missing_int(int_list): 
    
    range_list = range(0, max(int_list)+1)
    for i in range_list: 
        if i not in int_list:
            missing_n = i
    
    print(missing_n)
    return missing_n
    
missing_int(A)   



microsoft = [] 
for i in employee_info[0][1]: 
    if Company == 'Microsoft':
        microsoft.append(employee_info[0][1][i])

Google = [] 
for i in employee_info: 
    if Company == 'Google':
        microsoft.append(i)

overlapped_employees = []
for i in microsoft: 
    if i in Google:
        overlapped_employees.append(i)

