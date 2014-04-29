#!/usr/bin/python2
from flask.helpers import url_for
from flask.templating import render_template
from flask import request
from flask import Flask
from algo2 import *
from algo1 import *
import os
app=Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/startTesting')
def startTesting():
    return render_template("startTesting.html")

@app.route('/design')
def design():
    return render_template("design.html")

@app.route('/drivecollection')
def drivecollection():
    return render_template("drivecollection.html")

@app.route('/flowchart')
def flowchart():
    return render_template("flowchart.html")

@app.route('/howitworks')
def howitworks():
    return render_template("howitworks.html")

@app.route('/howitworks1')
def howitworks1():
    return render_template("howitworks1.html")

@app.route('/hReq')
def hReq():
    return render_template("hReq.html")

@app.route('/sReq')
def sReq():
    return render_template("sReq.html")

@app.route('/navi')
def navi():
    return render_template("navi.html")

@app.route('/results')
def results():
    return render_template("results.html")

@app.route('/show1')
def show1():
    return render_template("show1.html")

@app.route('/show2')
def show2():
    return render_template("show2.html")

@app.route('/show3')
def show3():
    return render_template("show3.html")

@app.route('/show5')
def show5():
    return render_template("show5.html")

@app.route('/show6')
def show6():
    return render_template("show6.html")

@app.route('/show7')
def show7():
    return render_template("show7.html")

@app.route('/show8')
def show8():
    return render_template("show8.html")

@app.route('/whatisit')
def whatisit():
    return render_template("whatisit.html")

@app.route('/whatisit1')
def whatisit1():
    return render_template("whatisit1.html")

@app.route('/darpaAttack')
@app.route('/darpaAttack/<train>/<test>')
def darpa():
    trainstream = TCPstream(100,40,0.088)
    trainstream = trainPhase(100,40,10,'darpatrain',0.088)
    f = open('thresholdP','w')
    f.write(str(trainstream.thresholdProbability))
    f.close()
    teststream = TCPstream(100,40,0.088)
    teststream.probabilityArray = trainstream.probabilityArray
    teststream = deploy(teststream,10,'darpaattack')
    return render_template("darpaattack.html",train=trainstream,test=teststream)

@app.route('/darpaNoAttack')
@app.route('/darpaNoAttack/<train>/<test>')
def darpano():
    trainstream = TCPstream(100,40,0.088)
    trainstream = trainPhase(100,40,10,'darpatrain',0.088)
    f = open('thresholdP','w')
    f.write(str(trainstream.thresholdProbability))
    f.close()
    teststream = TCPstream(100,40,0.088)
    teststream.probabilityArray = trainstream.probabilityArray
    teststream = deploy(teststream,10,'darpanoattack')
    return render_template("darpanoattack.html",train=trainstream,test=teststream)

@app.route('/kddAttack')
@app.route('/kddAttack/<train>/<test>')
def kdd():
    trainstream = TCPstream(100,40,0.111)
    trainstream = trainPhase(100,40,10,'kddTrain',0.111)
    f = open('thresholdP','w')
    f.write(str(trainstream.thresholdProbability))
    f.close()
    teststream = TCPstream(100,40,0.111)
    teststream.probabilityArray = trainstream.probabilityArray
    teststream = deploy(teststream,10,'kddAttack')
    return render_template("kdd.html",train=trainstream,test=teststream)

@app.route('/kddNoAttack')
@app.route('/kddNoAttack/<train>/<test>')
def kddno():
    trainstream = TCPstream(100,40,0.088)
    trainstream = trainPhase(100,40,10,'kddTrain',0.088)
    f = open('thresholdP','w')
    f.write(str(trainstream.thresholdProbability))
    f.close()
    teststream = TCPstream(100,40,0.088)
    teststream.probabilityArray = trainstream.probabilityArray
    teststream = deploy(teststream,10,'kddNoAttack')
    return render_template("kddno.html",train=trainstream,test=teststream)

if __name__ == "__main__":
    trainstream = teststream = TCPstream(100,40,0.0)
    app.run()

""" Template for each page
@app.route('')
def ():
    return render_template(".html")
"""
