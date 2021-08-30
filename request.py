import requests

url='http://localhost:5000/predict_api'
r=requests.post(url,json={'Weight':790, 'Volume':1000})

print(r.json())