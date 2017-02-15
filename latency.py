import subprocess

pings = []
pings.append(['us-east-1', '75.101.163.105'])
pings.append(['us-east-2','52.14.64.0'])
pings.append(['us-west-1','52.52.63.252'])
pings.append(['us-west-2','52.36.0.2'])
pings.append(['us-gov-west-1','52.222.9.163'])
pings.append(['ca-central-1','52.60.50.0'])
pings.append(['eu-west-1','52.215.255.254'])
pings.append(['eu-central-1','35.156.63.252'])
pings.append(['eu-west-2','52.56.34.0'])
pings.append(['ap-northeast-1','46.51.255.254'])
pings.append(['ap-northeast-2','52.78.63.252'])
pings.append(['ap-southeast-1','46.51.216.14'])
pings.append(['ap-southeast-2','54.253.0.1'])
pings.append(['ap-south-1','35.154.63.252'])
pings.append(['sa-east-1','54.94.0.66'])

for region in pings:
	ping = subprocess.Popen(
	    ["ping", "-c", "3", region[1]],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	out, error = ping.communicate()
	region.append(out.split(' ')[-2].split('/')[1])

sorted_pings = sorted(pings, key = lambda x: float(x[2]))

counter = 1
for p in sorted_pings:
	print str(counter)+'. '+p[0]+' ['+p[1]+'] - '+p[2]
	counter = counter+1