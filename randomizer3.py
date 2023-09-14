import random
import sys
from living_things import *

categories = [ amphibians, birds, fish, invet_terr, invet_fresh, invet_marine, mammals, plants, reptials]

for _ in range(50):
    selected_categories = random.sample(categories, 3)
    
    for category in selected_categories:
        item = random.choice(category)
        sys.stdout.write(item + ' ')
    
    print()  # This will print a newline character


