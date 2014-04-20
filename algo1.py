from algo8 import *
from parser import *
def deploy(stream, awc, filename):
  a=0.0
  f = open('thresholdP','r')
  thresholdP =float(f.read())
  f.close()
  inputTraffic = parse(filename)
  windowCount = inputTraffic.size/stream.windowSize
  for i in range(windowCount):
    p = determineProbability(inputTraffic[i*100:(i*100)+100], stream)
    if ( p > thresholdP):
      a+=1
    else:
      a-=1
    if a>=awc:
      print "attack"
    else:
      print "normal"
  print a

teststream = TCPstream(100,40)
deploy(teststream,5,'op_flag1')