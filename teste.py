import requests

url = 'https://w3schools.com/python/demopage2.php'

#use the 'cookies' parameter to send cookies to the server:
x = requests.get(url, cookies = {"favcolor": "Red"})

print(x.text)