import numpy
import copy

def determineOptimalBands(A,N,K):
  J = [-1 for _ in range(N-1)]
  Js = [-1 for _ in range(K-1)]
  As = sorted(A,reverse=True)
  for i in range(N-1):
    J[i] = As[i] - As[i+1]
  temp = sorted(J,reverse=True)
  for i in range(K-1):
    Js[i] = temp[i]
  temp_set = set(Js)
  I = [i for i,item in enumerate(J) if item in temp_set]
  Is = sorted(I)
  band = [[-1 for _ in range(K)] for _ in range(N)]
  lower = 0
  for i in range(K-1):
    upper = Is[i]
    nelements = upper - lower + 1
    k = 0
    band[i][k] = nelements
    k = k+1
    for i in range(lower,lower+nelements):
      temp[i] = As[i]
    temp_set = set(temp)
    band[i][k] = [j for j,item in enumerate(A) if item in temp_set]
    k = k+1
    lower = upper + 1
  old_i=i
  temp = []
  for i in band:
    for j in i:
      temp.append(j)
  temp_set = set(temp)
  temp = []
  for i in range(len(temp_set)):
    temp.append(temp_set.pop())
  for i in temp:
    band[old_i][K] = i
    K = K+1
  return band
  
A = [500,291,271,36,222,111,1211,3,1,31,1]
bandgroup = [[-1 for _ in range(5)] for _ in range(10)]
bandgroup = determineOptimalBands(A,10,5)
print bandgroup
