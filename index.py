def prime_factors(num):
	f=[]
	nms=[]
	while num>1:
		ds=False
		n=2
		while not ds:
			if num%n==0:
				ds=True
			else:
				n+=1
		nms+=[num]
		num//=n
		f+=[n]
	return [f,nms]
def NWD(a,b):
	af=prime_factors(a)[0]
	bf=prime_factors(b)[0]
	o=1
	of=[]
	for ani in range(len(af)-1,-1,-1):
		an=af[ani]
		if an in bf:
			af.remove(an)
			bf.remove(an)
			o*=an
			of+=[an]
	if of==[]:of=[1]
	return o,of
def NWW(a,b):
	return (a*b)//NWD(a,b)[0],
def log_factors(n):
	f=prime_factors(n)
	so=""
	bl=len(str(f[1][0]))
	for fn in f[1]:
		if len(str(fn))>bl:bl=len(str(fn))
	f[1]+=[1]
	f[0]+=[""]
	for fni in range(0,len(f[1])):
		so+=f"{str(f[1][fni]).rjust(bl)} | {f[0][fni]}\n"
	return so
def log_func(f,p):
	if f.__name__=="NWD":
		calc=""
		dl=[]
		l=NWD(p[0],p[1])[1]
		for k in l:
			if k not in dl:
				calc+=f"{k}^{l.count(k)}*"
				dl+=[k]
		calc=calc.replace("^1*","*")
		print(f"\nNWD of {p[0]} and {p[1]}:\n\n{log_factors(p[0])}\n{log_factors(p[1])}\nNWD({p[0]},{p[1]})={calc[:-1]}={NWD(p[0],p[1])[0]}\n")
	elif f.__name__=="prime_factors":
		dl=[]
		calc=""
		l=prime_factors(p[0])[0]
		for k in l:
			if k not in dl:
				calc+=f"{k}^{l.count(k)}*"
				dl+=[k]
		calc=calc.replace("^1*","*")
		print(f"Prime factors of {p[0]}:\n\n{log_factors(p[0])}\n{p[0]}={calc[:-1]}\n")
log_func(NWD,(4096,4097))
print("\n"*10)
log_func(prime_factors,(4096+1,))