def determineOptimalBands(A,N,K):

  J = []
  Js = []
  upper = 0
  lower = 0
  nelements = 0
  I = []
  Is = []
  band = [[] for _ in range(K)]
  
  As = sorted(A,reverse=True)
  
  for i in range(N-1):
    J.append(As[i] - As[i+1])

  temp = sorted(J,reverse=True)
  for i in range(K-1):
    Js.append(temp[i])
    
  for i in Js:
    I.append(J.index(i))
    
  Is = sorted(I)
  
  for i in range(K-1):
    upper = Is[i]
    nelements = upper - lower + 1
    band[i].append(nelements)
    for j in range(lower,lower+nelements):
      band[i].append(A.index(As[j]))
    lower = upper + 1
  
  print band  
  
  #old_i=i
  #temp = []
  #print band
  #for i in band:
   # for j in i:
    #  temp.append(j)
  #temp_set = set(temp)
  #temp = []
  #for i in range(len(temp_set)):
  #  temp.append(temp_set.pop())
  #for i in temp:
  #  band[old_i][K] = i
  #  K = K+1
  return band
  
A = [500,291,271,36,222,111,1211,3,1,31,1]
bandgroup = [[-1 for _ in range(5)] for _ in range(10)]
bandgroup = determineOptimalBands(A,10,5)
#print bandgroup