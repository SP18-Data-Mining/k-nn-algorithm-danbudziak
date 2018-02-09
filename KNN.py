#Danny Budziak
#Project 1
#February 8, 2018
#K-Nearest-Neighbors
import math

dataObjectCount = 0
testData = []
trainingData = []
trainingFeatures = []
testFeatures = []
trainingLabels = []

with open('fruit_data_with_colors.txt','r') as tsv:
	for line in tsv : 
		if dataObjectCount % 5 == 0 :
			# Ignoring the first row - containing header info
			if dataObjectCount != 0 :
				testData.append(line.strip().split('\t'))
		else :
			trainingData.append(line.strip().split('\t'))
		dataObjectCount = dataObjectCount + 1

for line in trainingData :
	dataObject = []
	dataObject.append(float(line[5]))
	dataObject.append(float(line[6]))
	trainingLabels.append(line[0])
	trainingFeatures.append(dataObject)


for line in testData :
	dataObject = []
	dataObject.append(float(line[5]))
	dataObject.append(float(line[6]))
	testFeatures.append(dataObject)

def euclideanDistance(x1, x2, leng):
	distance = 0 
	for x in range(leng):
		distance += pow((x1[0] - x2[0]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingFeatures, testFeatures, k=3):
	distance = []
	neighbors = []
	length = len(testFeatures) - 1
	for i,group in enumerate(trainingData) :
		dist = euclideanDistance(testFeatures[0], trainingFeatures[0], length)
		distance.append((dist))
	for x in range (k) :
		neighbors.append(trainingLabels[0])
	return neighbors

for i,group in enumerate(testData) :
    print"Test Data is: ", group
    print'Prediction Label is: ', getNeighbors(trainingFeatures, testFeatures, k=3)
    print'\n'

