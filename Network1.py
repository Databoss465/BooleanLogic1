import matplotlib.pyplot as plt
import numpy as np
import random
import statistics

#Defines a function to simulate Boolean Logic Netwok
def sim():
	"""Simulates the Network and returns a list of the network state at each timestep"""

	t = 0

	GF = 1
	rtk = 0
	ras = 0
	raf = 0
	mekerk = 0
	pi3k = 0
	pip3 = 0
	akt = 0
	TF = 0

	trial = [[1,0,0,0,0,0,0,0,0]]
	
	while TF == 0:
		t += 1
		val = []
		val.append(1)

		x = random.randint(0, 7)
		if x == 0:
			rtk = GF

		elif x == 1:
			ras = rtk

		elif x == 2:
			pi3k = rtk or ras

		elif x == 3:
			raf = ras

		elif x == 4:
			mekerk = raf

		elif x == 5:
			pip3 = pi3k

		elif x == 6:
			akt = pip3

		elif x == 7:
			TF = mekerk and akt

		val.append(rtk)
		val.append(ras)
		val.append(raf)
		val.append(pi3k)
		val.append(pip3)
		val.append(akt)
		val.append(mekerk)
		val.append(TF)

		trial.append(val)
	
	return trial

#Define a function to run the simulation several times and create a uniform dataset
T = 0

def runsim(n):
	"""Runs the simulation n times and returns a dictionary of trial number against the data from each simulation upto the time of longest run"""
	
	dat = {}
	simlen = []
	
	for x in range(n):
		dat[x] = sim()
		simlen.append(len(dat[x]))
	
	global T
	T = max(simlen)
	index = list(dat.keys())

	for i in index:
		d = dat[i]
		while len(d) < T:
			d.append(d[-1])

	return dat

#Define a function to get the mean state of each node at every timestep
def getmean(dic):
	"""Takes the required data set and gives a list of mean states at each timestep, for every marker"""
	
	t = 0
	arr_GF = []
	arr_rtk = []
	arr_ras = []
	arr_raf = []
	arr_pi3k = []
	arr_pip3 = []
	arr_akt = []
	arr_mekerk = []
	arr_TF = []

	while t < T:
		
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][0])
		m = statistics.mean(a)
		arr_GF.append(m)

		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][1])
		m = statistics.mean(a)
		arr_rtk.append(m)

		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][2])
		m = statistics.mean(a)
		arr_ras.append(m)
		
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][3])
		m = statistics.mean(a)
		arr_raf.append(m)
		
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][4])
		m = statistics.mean(a)
		arr_pi3k.append(m)
	
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][5])
		m = statistics.mean(a)
		arr_pip3.append(m)
		
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][6])
		m = statistics.mean(a)
		arr_akt.append(m)
		
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][7])
		m = statistics.mean(a)
		arr_mekerk.append(m)
		
		a=[]
		for i in list(dic.keys()):
			a.append(dic[i][t][8])
		m = statistics.mean(a)
		arr_TF.append(m)
		t += 1
	
	return [arr_GF, arr_rtk, arr_ras, arr_raf, arr_pi3k, arr_pip3, arr_akt, arr_mekerk, arr_TF]

#Run the functions and obtains the graph
Z = getmean(runsim(10000))

#Dataset for Y-Axis
yGF = Z[0]
yRTK = Z[1]
yRAS = Z[2]
yRAF = Z[3]
yPI3K = Z[4]
yPIP3 = Z[5]
yAKT = Z[6]
yMEKERK = Z[7]
yTF = Z[8]

#Data for X-Axis
x = []
for i in range(T):
	x.append(i)

#Plotting
plt.title('Network 1')
plt.xlabel('Time')
plt.ylabel('Node Activity')
plt.grid()
plt.plot(x, yGF, label ='GF', color='red')
plt.plot(x, yRTK, label ='RTK', color='orange')
plt.plot(x, yRAS, label ='RAS', color='yellow')
plt.plot(x, yRAF, label ='RAF', color='green')
plt.plot(x, yPI3K, label ='PI3K', color='blue')
plt.plot(x, yPIP3, label ='PIP3', color='purple')
plt.plot(x, yAKT, label ='AKT', color='brown')
plt.plot(x, yMEKERK, label ='MEK/ERK', color='cyan')
plt.plot(x, yTF, label ='TF', color='black')
plt.legend()
plt.show()
