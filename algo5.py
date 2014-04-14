from algo8 import *

def determineOptimalBands(arrayA,windowSize,bandCount):
  jumpCount = zeros(windowSize)
  sortedJumps = zeros(bandCount-1)
  upper = 0
  lower = 0
  nelements = 0
  indexArray = zeros(bandCount-1)
  band = zeros(bandCount*windowSize).reshape(bandCount, windowSize) - 1

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
    k += 1
    temp = sortedA[lower:lower+nelements]
    arrayAPos = argsort(arrayA)
    tempPos = searchsorted(arrayA[arrayAPos],temp,sorter=None)
    for x in arrayAPos[tempPos]:
      band[i][k] = x
      k += 1
    lower = upper + 1

  arrayAPosReversed = arrayAPos[::-1]
  for x in range(0,windowSize+1-bandCount):
    band[i+1][x] = arrayAPosReversed[bandCount]
    bandCount += 1
  return band.astype(int32)