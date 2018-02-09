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


def getNeighbors(trainingFeatures, testFeatures, k=3):
        for x,tesData in enumerate(testData):
          mindistance=100
          for y,trData in enumerate(trainingData):
               euclidean_distance = math.sqrt(((testFeatures[0][0] - trainingFeatures[0][0])**2) + ((testFeatures[0][1] - trainingFeatures[0][1])**2))
               neighbors = (int(euclidean_distance))
        return neighbors
               
for i,group in enumerate(testData) :
    print"Test Data is: ", group
    print'Prediction Label is: ', getNeighbors(trainingFeatures, testFeatures, k=3)
    print'\n'
