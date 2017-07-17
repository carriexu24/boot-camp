import numpy

#def mySolve
#try to solve the equation Ax=b using linalg.solve
#if can, verify the equation
#if can't, tell the user that the equation can't be solved
def mySolve(A, b):
    try:
        x = numpy.linalg.solve(A, b)

        #verify the equation
        if numpy.dot(A, x).all() == b.all():
            print "The equation is verified."
        else:
            print "The equation can't be verified."

    except numpy.linalg.linalg.LinAlgError:
        print "The equation can not be solved."



# Problem 1 A.

# define a 10 * 10 array A
A = []
for i in range(10):
    myline = []
    for j in range(10):
        myline.append(10*i+j+1)
    A.append(myline)
A = numpy.array(A)

#define array v
v = []
for i in range(10):
    v.append(i+1)
v = numpy.array(v)

#define array b
b = 10*[1]
b = numpy.array(b)

#compute Av
print numpy.dot(A, v)

#solve Ax=b and Ax=v
mySolve(A, b)
mySolve(A, v)



#Problem 1 B.

#build a 10 * 10 array R(e)
R = numpy.random.rand(10, 10)
R = numpy.array(R)

#solve (A+R)x=b and (A+R)x=v and verify the solutions
mySolve(A+R, b)
mySolve(A+R, v)



#Problem 1 C.

#solve (A+R)x=b, calculate Ax and compare the result to b
x = numpy.linalg.solve(A+R, b)
print numpy.dot(A, x)
print abs(list(numpy.dot(A, x)) - b)

#solve (A+R)x=v, calculate Ax and compare the result to v
y = numpy.linalg.solve(A+R, v)
print numpy.dot(A, y)
print abs(list(numpy.dot(A, y)) - v)
