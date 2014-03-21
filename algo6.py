from algo5 import *

def updateProbabilities(stream, bandCount, band, observableTypeIndex):
    avgCount = 0
    stream.trainWindowCount += bandCount
    for j in range(0,bandCount):
      nelband = band[j][0]
      for k in range(1,nelband+1):
        avgCount += stream.probabilityArray[observableTypeIndex][band[j][k]]
      avgCount += 1
      if nelband == 0:
        nelband += 1
      avgCount /= nelband
      for k in range(1,nelband+1):
        stream.probabilityArray[observableTypeIndex][band[j][k]] = avgCount
      for k in range(1,nelband+1):
        stream.probabilityArray[observableTypeIndex][band[j][k]] /= stream.trainWindowCount
      avgCount = 0
    return stream

