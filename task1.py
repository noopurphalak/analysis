f_obj = open('NST-EST2015-alldata.csv')
data = f_obj.readlines()
f_obj.close()

state_index = 3
state_name_index = 4
population_index = 12
state_data = []

print('Loading data')
for record in data[1:]:
    record_data = record.split(',')
    if int(record_data[state_index]) in range(1, 57):
        state_data.append({'name': record_data[state_name_index], 'population': int(record_data[population_index])})
print('Loading data complete!!!')

print('Sorting data according to Population in 2015')
state_data = sorted(state_data, key=lambda st_data: (st_data['population']), reverse=True)
print('Sorting data complete, Here are the States according to Decreasing Population:')
for state_record in state_data:
    print(state_record)
