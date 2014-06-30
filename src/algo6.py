from algo5 import *

def updateProbabilities(stream, bandCount, band, observableTypeIndex):
    """
        This algorithm computes and updates the probability based on the events
    """
    #Intialize avgCount
    avgCount = 0
    #Update the train windowCount
    stream.trainWindowCount += bandCount
    for j in range(0,bandCount):
      #Intialise number of elements in the jth band
      nelband = band[j][0]
      #Determine the average count of the band
      for k in range(1,nelband):
        avgCount += stream.probabilityArray[observableTypeIndex][band[j][k]]
      avgCount += 1
      #Skip the iteration if number of elements in band is zero
      if nelband == 0:
        continue
      #Determina the avgerage Count
      avgCount /= nelband
      for k in range(1,nelband):
      #Store  average count in stream for later computation
        stream.probabilityArray[observableTypeIndex][band[j][k]] = avgCount
      #Compute probability of the particular group and band and store it in the stream
      for k in range(1,nelband):
        stream.probabilityArray[observableTypeIndex][band[j][k]] /= stream.trainWindowCount
      #Reset avg Count
      avgCount = 0
    return stream

