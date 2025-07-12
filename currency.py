import requests


api="3fe916c2fe954eb589bd86df"
c_1=input("enter currency convert from : ").upper()
c_2=input("enter currency convert to  : ").upper()
amount=input("enter amount to convert : ")

base_url=f"https://v6.exchangerate-api.com/v6/3fe916c2fe954eb589bd86df/pair"

response = requests.get(f"{base_url}/{c_1}/{c_2}/{amount}")


if response.status_code==200:
    data=response.json()
    # print(data)
    converted_amount=data['conversion_result']
    print(f"{amount} {c_1} is equal to {converted_amount} {c_2}")
else:       
    print("Error in conversion")