# import pandas as pd
#
# class RideAnalyzer():
#     def __init__(self):
#         self.df = pd.read_csv("data_file.csv")
#
#     def get_top_riders(self, n):
#         # top_riders = (self.df.groupby("user_id")["distance_km"].sum().reset_index().sort_values(by="distance_km", ascending=False).head(n))
#         top_riders = (self.df.groupby("user_id")["distance_km"]).sum().reset_index().sort_values(by=["distance_km"], ascending=False).head(n)
#         print(top_riders)
#
#
# ride_obj = RideAnalyzer()
# ride_obj.get_top_riders(1)

from collections import Counter
import re


class Animal(object):
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def animal_name(self):
        print(self.animal_name)

class Dog(Animal):
    def __init__(self, animal_sound):
        Animal.__init__(self, 'dog')
        self.animal_sound = animal_sound
    def animal_dog(self):
        print(self.animal_name, self.animal_sound,  "subclass call")

# class Cat(Animal): 
#     def animal_cat(self, sound):


# obj_animal = Dog('Bark')
# obj_animal.animal_dog()



def own_decorator(func):
    def wrapper(*args, **kwargs):
        print("function before calling")
        result = func(*args, **kwargs)
        sq_result = result**2
        print(f"the add result is {result} and the square of the result is {sq_result}")
    return wrapper

@own_decorator
def add(a,b,c):
    return (a+b+c)

add(1,2,3)



class Animal():
    def __init__(self, name):
        self.name = name
        # self.print_name()

    # def print_name(self):
    #     print(f"main class print {self.name}")



class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound
        super().__init__("dog")
        print(f"{self.name} sounds like {self.sound}")


class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound
        super().__init__("cat")
        print(f"{self.name} sounds like {self.sound}")

# dog_obj = Dog("Bark")
# cat_obj = Cat("Meow")
# dog_obj.dog_method('Bark')



list_sortt = [4, 2, 9, 1, 7]
# sort_lisd = list_sortt.sort
# print("new lists sort", sort_lisd)
print(sorted(list_sortt, reverse=False))
# for i in range(len(list_sortt)):
#     for j in range(len(list_sortt) - 1):
#         if list_sortt[j] > list_sortt[j + 1]:
#             list_sortt[j], list_sortt[j + 1] = list_sortt[j + 1], list_sortt[j]
# print(list_sortt)

tup_list = [("Hari", 90), ("Krishna", 85), ("Arjun", 95)]

for i in range(len(tup_list)):
     for j in range(len(tup_list)-1):
         if tup_list[j][1]>tup_list[j+1][1]:
             tup_list[j], tup_list[j+1] = tup_list[j+1], tup_list[j]

print(tup_list)



# import json

# with open('examp.json','r+') as fd:
#     # data = json.load(fd)
#     string_data = fd.read()
#     jsonn_data = json.loads(string_data)
#     jsonn_data['role'] = "Software Engineer"
#     jsonn_data['skills'].append('AI')

# print(jsonn_data)

# with open('examp.json', 'w') as fd2:
#     json.dump(jsonn_data, fd2)
# print(jsonn_data)


# print(type(data))


un_list = [4, 2, 7, 2, 1, 4, 9, 7, 4, 5 ,6]
unique_list = []
dup_ele = []

for n in un_list:
    found = False
    for u in unique_list:
        if u==n:
            found = True
            dup_ele.append(n)
            break
    if not found:
        unique_list.append(n)

print(unique_list)
print(dup_ele)

for i in range(len(unique_list)):
    for j in range(len(unique_list)-1):
        if unique_list[j] > unique_list[j+1]:
            unique_list[j], unique_list[j+1] = unique_list[j+1], unique_list[j]

print("new list",unique_list)

occ_list = [4, 2, 7, 2, 1, 4, 9, 7,'Hari','Hari', 4, 4 ,4, 7, 7, 7, 7, 2, 2, 2, 2]

count_occ = Counter(occ_list)
print(count_occ)



class Car():
    def __init__(self, name):
        self.name = name
    
    def car_name_print(self):
        print(f"the call in the parent class {self.name}")

    

class ModelName(Car):
    def __init__(self, model):
        self.model = model
        self.sound = 'burburburburbur'
        super().__init__('Toyota')

    def model_name(self):
        print(f"child class {self.model}, from parent class car brand is {self.name}")

    def car_sound(self):
        print(f"Car sounds like {self.sound}")

class AnotherModel():
    def __init__(self, sound_name):
        self.sound = sound_name

    def car_sound(self):
        print(f"car sound in different class {self.sound}")

obj_model = ModelName("Supra")
obj_anmodel = AnotherModel("vroomvroomvroom")
obj_anmodel.car_sound()
obj_model.car_sound()
obj_model.model_name()



txt = "the cabs are not worth booking and own vehicle is more comfortable"

txt_list = txt.split()

re_txt_list = []

for i in range(len(txt_list)):
    re_txt_list.append(txt_list[i][::-1])

print(re_txt_list)

rev_txt = " ".join(re_txt_list)
print(rev_txt)

simple_sent = "there are 11 players in the team. the team has 4 bowlers and 4 batsman. The four batsman are a1, a2,a3,a4. The four bowlers are b1,b2,b3,b4. This team is well balanced. This team can win the cup"

patterns = r"\w+"
words = re.findall(patterns, simple_sent.lower())
count = Counter(words)
print(count)


# import re

text = "The system test passed successfully."
pattern = "test"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())



un_list = [4, 2, 7, 2, 1, 4, 9, 7, 4, 5 ,6]
unq_listsss = []
dup_elem = []
for i in un_list:
    if i not in unq_listsss:
        unq_listsss.append(i)
    else:
        dup_elem.append(i)

print(unq_listsss)


list_comp = [x for x in range(0,5) if x%2 == 0] 

print(list_comp, 'comprehension list')


result_lambs = lambda x,y: x*x*y
print(result_lambs(5,2))


items = ['500 gm', '100 kgs', '160 kgs', '600gm']

total_gm = 0

for item in items:
    num = int(''.join([x for x in item if x.isdigit()]))

    print(num)

    if "kgs" in item.lower():
        total_gm += num * 1000
    else:
        total_gm += num 

print("Total in grams:", total_gm)
print("Total in kg:", total_gm/1000)