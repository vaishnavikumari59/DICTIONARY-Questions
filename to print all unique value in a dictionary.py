d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
print("Original List",d1)
u_value = set( val for dic in d1 for val in dic.values())
print('Unique Values:',u_value)
