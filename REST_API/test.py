import requests   #if its not there install using sudo pip install requests

BASE='http://127.0.0.1:5000/'   #Base url

data=[
    {'likes':100,'views':50,'name':'title1'},
    {'likes':1000,'views':5000,'name':'title2'},
    {'likes':20,'views':50,'name':'title3'},
]

for i in range(len(data)):
     response= requests.put(BASE+'video/'+str(i), data[i])
     print(response.json())

input()

# response = requests.delete(BASE+'video/1')
# print(response)

# input()

# response = requests.get(BASE+'video/1')
# print(response.json())


# response = requests.put(BASE+'video/1',{'name':'tv','likes':10,'views':100})   #calling the api get from main.py
# print(response.json())   #will give op -> {'data': 'Hello World'}

# input()  #on hitting enter will execute and we will be able to see response


# response = requests.put(BASE+'video/1',{'name':'tv','likes':10,'views':100})   #calling the api get from main.py
# print(response.json())

# # response = requests.get(BASE+'video/1')
# # print(response.json())

# # response = requests.post(BASE+'helloworld')
# # print(response.json())