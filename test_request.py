import requests
r = requests.post("http://localhost:5000/",
                 data = {
                     "email":"chuck@gmail.com",
                     "captcha" : "10000000-aaaa-bbbb-cccc-000000000001"
                 })

print(r.status_code)
print(r.text)
