from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position
from football_dictionaries.assignment_3 import players_by_country_and_position
# from pprint import pprint


result = players_as_dictionaries(SQUADS_DATA)
print(f'Assignment 1 result:{result}')

result1 = players_by_position(result)
print(f'Assignment 2 result:{result1}')

result2 = players_by_country_and_position(result1)
print(f'Assignment 3 result:{result2}')
