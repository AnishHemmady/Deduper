import timeit

num_of_maps = 1000
setup = '''
import random
from deduper import Deduper
num_of_maps = 1000
dedup_me = [{"name": "anish", "val": 12}, {"name": "rahul", "val": 17}, {"name": "anish", "val": 12},
            {"name": "anish", "val": 12}, {"name": "rahul", "val": 17}, {"name": "rahulp", "val": 19}]
big_list = [random.choice(dedup_me) for _ in range(0, num_of_maps)]
'''
number = 1000
t = timeit.Timer(stmt='list(Deduper.async_dedup_data(big_list,lambda x: (x.get("name"),x.get("val"))))', setup=setup)
avg_time = t.timeit(number)
single_run_time = avg_time/number
print(f'Time it took to run {number} of times having {num_of_maps} of dicts in list: {avg_time}')
print(f'Time it took to run 1 time having {num_of_maps} of dicts in list: {single_run_time}')


