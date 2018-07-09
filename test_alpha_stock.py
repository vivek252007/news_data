https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=5EG68BRFQ101O0VL


import json
import requests
import datetime
rsp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=5EG68BRFQ101O0VL')
fin_data = json.loads(rsp.content)
fin_data["Time Series (1min)"]
a = fin_data["Time Series (1min)"].keys()
date = datetime.datetime.strptime(str(a[0]), "%Y-%m-%d %H:%M:%S")
for i in a:
	day = datetime.datetime.strptime(str(i), "%Y-%m-%d %H:%M:%S")
	if date<day:
		date=day

stock_price = str(fin_data["Time Series (1min)"][str(date)]['4. close'])
