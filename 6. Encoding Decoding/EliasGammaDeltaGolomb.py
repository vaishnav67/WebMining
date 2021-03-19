from math import log,ceil,floor,pow

log2 = lambda x: log(x,2)

def binary(x,l=1):
	fmt = '{0:0%db}' % l
	return fmt.format(x)

def unary(x):
	return (x-1)*'0'+'1'

def elias_generic(lencoding, x):
	if x == 0: return '0'
	l = 1+int(log2(x))
	a = x - 2**(int(log2(x)))
	k = int(log2(x))
	return lencoding(l) + binary(a,k)
	
def golomb(b, x):
	q = int((x) / b)
	r = int((x) % b)
	i = int(floor(log2(b)))
	d=pow(2,(i+1))-b
	if(r<d):
		return unary(q+1) + binary(r, i)
	else:
		return unary(q+1) + binary(int(r+d),i+1)

def elias_gamma(x):
	if(x==1):
		return "1"
	return elias_generic(unary, x)

def elias_delta(x):
	if(x==1):
		return "1"
	return elias_generic(elias_gamma,x)

def elias_gamma_dec(x):
	bit=0
	for i in x:
		if(i!='1'):
			bit+=1
		else:
			break
	bi=x
	bi=bi[bit:]
	try:
		bi=int(bi,2)
	except:
		bi=0
	return(bi)

def elias_delta_dec(x):
	if(x=='0' or x=='1'):
		return x
	bit=0
	for i in x:
		if(i!='1'):
			bit+=1
		else:
			break
	bi=x[bit:(2*bit)+1]
	try:
		bi=int(bi,2)
	except:
		bi=0
	p=x[-(bi-1):]
	p='1'+p
	p=int(p,2)
	return p

def golomb_dec(b, x):
	q=0
	for i in x:
		if(i!='1'):
			q+=1
		else:
			break
	i=floor(log2(b))
	d=pow(2,(i+1))-b
	try:
		r=int(x[q+1:q+1+i],2)
	except:
		r=0
	if(r>=d):
		r=int(x[q+1:q+1+(2*i)],2)
		r=r-d
	x=q*b+r
	return int(x)

print ("Encoding")
print ("    i: Elias Gamma: Elias Delta: Golomb(10)")
for i in range(2,21,2):
	print ("%5d: %-10s : %-10s : %-10s" %(i, elias_gamma(i),elias_delta(i), golomb(10,i)))
print("Decoding: Elias Gamma")
for i in range(2,21,2):
	print("%-10s : %-10s"%(elias_gamma(i),elias_gamma_dec(elias_gamma(i))))
print("Decoding: Elias Delta")
for i in range(2,21,2):
	print("%-10s : %-10s"%(elias_delta(i),elias_delta_dec(elias_delta(i))))
print("Decoding: Golomb(10)")
for i in range(2,21,2):
	print("%-10s : %-10s"%(golomb(10,i),golomb_dec(10,golomb(10,i))))
