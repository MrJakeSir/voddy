from urllib.request import Request, urlopen
from threading import Thread
from random import choice


def main(thread:int):
	url = 'https://blocksmash.io/?invite=844853'

	req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
	while True:
		proxy = choice([
			'169.239.92.81:8080',
			'217.150.54.253:8080',
			'47.75.90.57:80',
			'220.163.129.150:808',
			'219.91.186.105:8080',
			'45.71.115.35:999',
			'46.5.252.52:8080',
			'94.180.72.40:3128',
			'91.107.6.115:53281',
			'94.143.48.241:8080',
			'93.76.51.226:8080',
			'190.83.125.13:999',
			'191.241.48.132:3128',
			'190.144.4.190:999',
			'195.239.217.102:8080',
			'191.243.217.1:53281',
			'217.8.51.202:8080',
			'193.200.151.69:48241',
			'106.45.105.61:3256',
			'103.4.164.205:8080',
			'103.9.188.229:36984',
			'105.112.142.210:8080',
			'103.88.127.178:8080',
			'103.30.115.172:80',
			'104.248.90.212:80',
			'110.39.174.189:8080',
			'95.188.145.182:8080',
			'46.209.207.153:8080',
			'27.43.190.141:9999',
			'51.210.106.217:443',
			'45.230.169.129:999',
			'95.9.194.13:56726',
			'47.90.132.228:8008',
			'91.93.73.226:7070',
			'170.0.87.201:999',
			'168.119.153.224:3128',
			'165.232.66.88:8118',
			'45.70.15.2:8080',
			'169.57.219.244:80',
			'217.8.51.197:8080',
			'47.90.132.228:81',
			'223.241.77.206:3256',
			'223.241.77.233:3256',
			'222.74.202.244:80',
			'45.71.185.140:999',
			'46.52.148.90:8080',
			'94.181.48.95:1256',
			'91.193.253.188:23500',
			'94.199.2.235:8080',
			'95.111.236.28:3128',
			'190.83.125.19:999',
			'192.119.203.124:48678',
			'190.171.168.90:999',
			'195.9.112.58:8080',
			'220.149.25.33:80',
			'191.243.218.245:53281',
			'218.60.8.99:3129',
			'193.232.252.38:8080',
			'109.167.207.72:8080',
			'103.5.232.145:8080',
			'104.211.157.219:80',
			'105.28.114.169:30032',
			'103.99.10.17:84',
			'103.36.100.248:8000',
			'106.14.193.235:8080',
			'95.216.194.46:1081',
			'46.44.0.126:80',
			'27.76.177.228:6666',
			'51.222.21.92:32768',
			'45.233.65.41:999',
			'50.206.25.104:80',
			'92.204.129.161:80',
			'170.79.85.224:55443',
			'168.228.150.5:47507',
			'170.254.224.7:55443',
			'46.229.67.198:47437',
			'221.6.201.74:9999',
			'47.98.179.39:8080',
			'23.107.176.102:32180',
			'223.27.194.66:80',
			'223.214.223.252:3256',
			'46.209.207.158:8080',
			'47.56.9.58:3128',
			'94.23.91.209:80',
			'91.89.89.12:8080',
			'94.228.192.197:8087',
			'95.208.208.233:8080',
			'190.85.115.78:3128',
			'192.162.192.148:55443',
			'190.217.1.33:32192',
			'109.70.189.70:56408',
			'103.78.254.78:80',
			'105.208.44.183:53480',
			'106.14.121.167:8080',
			'103.99.8.102:83',
			'103.47.93.206:51618',
		])

		try:
			req.set_proxy(host=proxy, type='https')

			response = urlopen(req)
			print(f'Done thread {thread}')

		except Exception as e:
			exc = f'{type(e).__name__} : {e}'
			print(exc)
c = 0
threads = []
for _ in range(100):
	c += 1
	t1 = Thread(target=main, args=(c,))
	t1.start()
	threads.append(t1)

for thread in threads:
	thread.join()
