import requests
f=open("dcnitro.txt",'a')
url = "https://api.discord.gx.games/v1/direct-fulfillment"
payload = {
    "partnerUserId": "5055333528a2a654db33f8ee014b72242726357b54dba9f348d54056b4e95c3d"
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 OPR/56.0.3051.99"
}
num=int(input("Enter the number of promos you want to generate: "))
k=num
count=0
while num!=0:
    count=count+1
    response = requests.post(url, json=payload, headers=headers)
    if str(response.status_code)=="200":
        print("Response Status:", response.status_code,"OK")
    else:
        print("Response Status:",response.status_code,"BAD")
    a=str(response.text)[10:-2]
    b="https://discord.com/billing/partner-promotions/1180231712274387115/"
    c=b+a
    print("generated: ",count)
    f.write(c+'\n')
    num=num-1
print("\n\n\nGenerated",k,"Free Trials Successfully")
f.close()
