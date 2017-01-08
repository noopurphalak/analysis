# Let make a histogram for for Population Estimation in 2015 for all 56 states.

population_index = 12
highest_population = 0
lowest_population = 0
population_data = []
state_index = 3
no_of_buckets = 10
bin_interval = 0
bucket_lower_limit = 0
bucket_upper_limit = 0
buckets = []


class Bucket(object):
    upper_limit = 0
    lower_limit = 0

    def __init__(self, upper_limit, lower_limit):
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.entries = []
        self.count = 0

    def add_element(self, element):
        if self.is_element_in_range(element):
            self.entries.append(element)
        else:
            raise ValueError('Element Not in range')

    def is_element_in_range(self, element):
        if element >= self.lower_limit and element < self.upper_limit:
            return True
        else:
            return False

    def update_count(self):
        self.count = len(self.entries)

f_obj = open('NST-EST2015-alldata.csv')
data = f_obj.readlines()
f_obj.close()

for record in data[1:]:
    record_data = record.split(',')
    if int(record_data[state_index]) != 0:
        population_data.append(int(record_data[population_index]))

highest_population = max(population_data)
lowest_population = min(population_data)

bin_interval = int((highest_population - lowest_population) / no_of_buckets) + 1

for b in range(1, no_of_buckets + 1):
    if b == 1:
        bucket_lower_limit = lowest_population
    else:
        bucket_lower_limit = bucket_upper_limit
    bucket_upper_limit = bucket_lower_limit + bin_interval
    buckets.append(Bucket(bucket_upper_limit, bucket_lower_limit))

for state_pop in population_data:
    for b in buckets:
        if b.is_element_in_range(state_pop):
            b.add_element(state_pop)
            b.update_count()
for b in buckets:
    print("Bucket(" + str(b.__dict__) + ")")
