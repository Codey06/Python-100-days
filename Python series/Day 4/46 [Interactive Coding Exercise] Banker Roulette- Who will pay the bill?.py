import random
names_string=["Mustaf","Ben","Angela","Michael","Mohamed","Ahmed"]
names=names_string.split(",")
num_items=len(names)

random_choice=random.randint(0,num_items-1)
print(names[random_choice])