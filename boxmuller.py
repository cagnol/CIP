from numpy import random, sqrt, log, sin, cos, pi, arange
from pylab import show,hist,subplot,figure

N = 10000
binwidth=0.5

U = random.rand(N)
V = random.rand(N)

X = sqrt(-2*log(U))*cos(2*pi*V)
Y = sqrt(-2*log(U))*sin(2*pi*V)

figure()

subplot(221) # North-West
hist(U,bins=arange(min(U),max(U)+binwidth,binwidth)) 

subplot(222) # North-East
hist(V,bins=arange(min(V),max(V)+binwidth,binwidth))

subplot(223) # South-West
hist(X,bins=arange(min(X),max(X)+binwidth,binwidth))

subplot(224) # South-East
hist(Y,bins=arange(min(Y),max(Y)+binwidth,binwidth))

show()
