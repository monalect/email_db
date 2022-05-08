import requests
r = requests.post("http://localhost:5000/",
                 data = {
                     "email":"chuck@gmail.com",
                     "captcha" : "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
                 })

print(r.status_code)
print(r.text)
