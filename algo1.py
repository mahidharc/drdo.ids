from algo2 import *

def deploy(stream, InputTraffic, awc):
  a=0.0
  for i in range(stream.windowCount):
    for j in range(0,6):
      p = determineProbability(stream.windowCount, stream)
    if ( p < stream.thresholdProbability):
      a+=1
    else:
      a-=1
    if a>=awc:
      return attack