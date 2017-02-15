import psutil
conns = []
for c in psutil.net_connections():
	if c.laddr and c.raddr:
		x = []
		(lip, lport) = c.laddr
		(rip, rport) = c.raddr
		x.append(c.pid)
		x.append(lip + '@' + str(lport))
		x.append(rip + '@' + str(rport))
		x.append(c.status)
		for p in conns:
			if c.pid == p[0][0]:
				p.append(x)
				break
		else:
			new_p = []
			new_p.append(x)
			conns.append(new_p)
conns.sort(key=len, reverse=True)
print '"pid", "laddr", "raddr", "status"'
for p in conns:
	for c in p:
		print '"'+str(c[0])+'","'+c[1]+'","'+c[2]+'","'+c[3]+'"'

#print psutil.net_connections()
