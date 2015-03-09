import numpy as np


a = np.array([[0,0,0],[0.5,0,0],[0.5,1,1]])
N=3

#A = beta∙M + (1-beta) [1/N]NxN

beta = 0.7
a = beta*a
print a

c = np.array([[0.1],[0.1],[0.1]])
b = np.array([[1],[1],[1]])


m = np.matrix(a)
n = np.matrix(b)
#p = np.matrix(c)

p = (1-beta)/N

#Random Teleports: Tax each page a fraction (1-beta) of its score and redistribute evenly to avoid spider traps and dead ends.
k= m*n
k = k+p

print k,"\r\n\r\n"

#Iterate over method till the matrix settles. Markov Processes: For graphs that satisfy certain conditions, 
#the stationary distribution is unique and eventually will be reached no matter what the initial probability distribution at time t = 0
for i in range(100):
	k = m*k
	k = k+p
	print k,"\r\n\r\n"

'''

a = 0.38778971
b = 0.21481063
c = 0.39739966

print 0.575*a + 0.15*c 
print b

print 0.475*a + .05*c 

print (0.9*b + 0.475*a)

print 0.95*c

print b + .575*a 
print c'''