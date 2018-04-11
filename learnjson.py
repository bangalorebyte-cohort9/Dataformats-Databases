#!/usr/bin/env python3

import json

data = {
  	'name' : 'ACME',
	'shares': 100,
	'price':542.23
}

#Reading data back
with open('data.json','r') as f:
	data = json.load(f)
print(type(data))

#Writing JSON data to file
with open('data1.json','w') as f:
	json.dump(data,f)


db['dataset']['column_names'] = 2000

#Encode Python Dictionary Data Structure to JSON String
json_str = json.dumps(data) 

#print('Json String encoded (python dict) ', json_str)
print(type(json_str))


#Decode JSON string back to Python Dictionary 
data = json.loads(json_str)

#print('Decode(json str) ', data)
#print(type(data))
#print(data['name'],data['shares'],data['price'])

#Writing JSON data to file
#with open('data.json','w') as f:
#	json.dump(data,f)


#print(data)
