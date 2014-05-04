from algo2 import *
from algo1 import *

t = 0.111
trainstream = TCPstream(100,40,t)
trainstream = trainPhase(100,40,10,"kddTrain",t)
f = open('thresholdP','w')
f.write(str(trainstream.thresholdProbability))
f.close()
teststream = TCPstream(100,40,t)
teststream.probabilityArray = trainstream.probabilityArray
teststream = deploy(teststream,10,'kddNoAttack')

"""
data = teststream.stateArr
winNo = teststream.winNoArr
xs = repeat(range(len(winNo)), 2)
ys = repeat(data, 2)
xs = xs[1:]
ys = ys[:-1]
state = ["Normal","Attack"]
plt.xlabel("Window Number")
plt.ylabel("System State")
plt.plot(xs, ys)
plt.ylim(-0.5, 1.5)
plt.yticks([0,1],state)
plt.title("State transition graph")
plt.savefig("static/images/state_kddNoAttack.png")
"""