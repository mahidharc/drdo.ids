from algo6 import *
def TCPtrain(stream,trafficFlow,sizeW,bandC):
    #TODO : figure out how to populate stream.c[i]
    for i in range(6):
        band=determineOptimalBands(stream.probabilityArray[i],sizeW,bandC)
        stream=updateProbabilities(stream,bandC,bandC,i)






