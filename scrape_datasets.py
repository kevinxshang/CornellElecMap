import requests

url = "https://portal.emcs.cornell.edu/api/datasources/proxy/5/csv"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://portal.emcs.cornell.edu",
    "Referer": "https://portal.emcs.cornell.edu/dashboard/script/portal.js?orgId=2&var-portal_group=ADWhiteHouse&kiosk=tv&from=1672549200000&to=1673845199000",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}

# Assuming the data sent in POST is URL-encoded form data; replace 'your_post_data_here' with actual data
data = "your_post_data_here"

response = requests.post(url, headers=headers, data=data)

# To save the file
with open("Exported Data.xlsx", "wb") as f:
    f.write(response.content)
