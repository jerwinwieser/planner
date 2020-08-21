
import json

f = open('dataset.json',) 
  
data = json.load(f)

names = [data[i]['name'] for i in range(len(data))]
age = [data[i]['person_age'] for i in range(len(data))]
print(names, age)

f.close()