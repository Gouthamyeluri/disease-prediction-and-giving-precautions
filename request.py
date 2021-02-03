import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':'itching', 'sales_in_first_month':'skin_rash', 'sales_in_second_month':'nodal_skin_eruptions'})

print(r.json())