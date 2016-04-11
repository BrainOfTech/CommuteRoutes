#This file has utilities for testing the correlation of a dataset along two axes by performing a regression.
#Last edited by (S)am on 4-10-16

#math library used for sqrt function
import math

#computeCorrelation
#takes a list of x,y pairs (a list of [x,y]'s)
#	where x and y are in a consistent floating point representation
#and returns a correlation coefficient rho (Pearson's Correlation Coefficient)
#where rho takes values between -1 and 1
#and the greater |rho|, the stronger the correlation
#(Note that this tests for a linear correlation.)
def computeCorrelation(xyList):
	#deal with edge case of an empty list, or list with only one pair (breaks division)
	if len(xyList) <= 2:
		return 1
	#compute muX, the mean of the x values
	muX = sum([pair[0] for pair in xyList])/float(len(xyList))
	#compute sigmaX, the deviation in x (sqrt of the variance)
	varX = sum([(pair[0]-muX)*(pair[0]-muX) for pair in xyList])/float(len(xyList))
	sigmaX = math.sqrt(varX)
	#compute muY, the mean of the y values
	muY = sum([pair[1] for pair in xyList])/float(len(xyList))
	#compute sigmaY, the deviation in y
	varY = sum([(pair[1]-muY)*(pair[1]-muY) for pair in xyList])/float(len(xyList))
	sigmaY = math.sqrt(varY)
	#compute the covariance of x and y
	cov = sum([(pair[0]-muX)*(pair[1]-muY) for pair in xyList])/float(len(xyList))
	#compute the correlation coefficient rho = cov/(sigmaX * sigmaY)
	if sigmaX * sigmaX * sigmaY * sigmaY > 0.0: #if the division is defined
		rho = cov/(sigmaX * sigmaY)
	else:
		rho = 0.0
	return rho

#correlationIsSignificant
#takes a correlation coefficient and number of samples
#and returns a boolean indicating whether the correlation is significant at the .05 level.
#Note that this computation is based on a heuristic function that is close enough for practical purposes.
def correlationIsSignificant(rho, numberOfSamples):
	if numberOfSamples <= 2:
		return false
	return abs(rho) > (3.0 / (2.0 * pow(numberOfSamples, 1.0/3.0) + pow(numberOfSamples, 1.0/2.7)))

#computeCorrelationIsSignificant
#is a syntactic simplification that combines the functions computeCorrelation and correlationIsSignificant.
#It takes a list of pairs and returns a boolean indicating whether their correlation has significance.
def computeCorrelationIsSignificant(xyList):
	return correlationIsSignificant(computeCorrelation(xyList), len(xyList))
