from numpy import *

def determineOptimalBands(arrayA,windowSize,bandCount):
  jumpCount = zeros(windowSize)
  sortedJumps = zeros(bandCount-1)
  upper = 0
  lower = 0
  nelements = 0
  indexArray = zeros(bandCount-1)
  band = zeros(bandCount*windowSize).reshape(bandCount, windowSize) - 1
  finalK = -1

  sortedA = sorted(arrayA,reverse=True)
  for i in range(windowSize-1):
    jumpCount[i] = sortedA[i] - sortedA[i+1]
  temp = sorted(jumpCount,reverse=True)
  for i in range(bandCount-1):
    sortedJumps[i] = temp[i]

  jumpCountPos = argsort(jumpCount)
  sortedJumpsPos = searchsorted(jumpCount[jumpCountPos], sortedJumps)
  indexArray = jumpCountPos[sortedJumpsPos]

  for i in range(bandCount-1):
    upper = indexArray[i]
    nelements = upper - lower + 1
    k = 0
    band[i][k] = nelements
    temp = sortedA[lower:lower+nelements]
    arrayAPos = argsort(arrayA)
    tempPos = searchsorted(arrayA[arrayAPos],temp,sorter=None)
    for x in arrayAPos[tempPos]:
      band[i][k] = x
      k += 1
      finalK += 1
    lower += nelements

  arrayAPosReversed = arrayAPos[::-1]
  k=0
  for x in range(finalK+1,windowSize+1):
    band[i+1][k] = arrayAPosReversed[x]
    k += 1
  return band.astype(int32)