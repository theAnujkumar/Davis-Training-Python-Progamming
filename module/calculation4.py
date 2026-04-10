# to import specific content only

# syntax :- from modulename import content1

#  to call function
#syntax :- functionname(parameter)

# to import entire module
#import modulename
# import NumericCalculation

from NumericCalculation import calculateAddition


# functionname(parameters)
print("sum of",5,"and",4,"is:",calculateAddition(4,5))

# to call function
# modulename.functionname(parameter)

# NumericCalculation.calculateAddition(4,5)
# print("sum of",5,"and",4,"is:",NumericCalculation.calculateAddition(4,5))

m=10
n=5
#print("difference of",m,"and",n,"is:",NumericCalculation.calculateDifference(m,n))