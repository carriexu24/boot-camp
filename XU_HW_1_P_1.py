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



#Result

#[ 385  935 1485 2035 2585 3135 3685 4235 4785 5335]

#The equation can not be solved.
#The equation can not be solved.



#Problem 1 B.

#build a 10 * 10 array R(e)
R = numpy.random.rand(10, 10)
R = numpy.array(R)

#solve (A+R)x=b and (A+R)x=v and verify the solutions
mySolve(A+R, b)
mySolve(A+R, v)



#Result

#The equation is verified.
#The equation is verified.



#Problem 1 C.

#solve (A+R)x=b, calculate Ax and compare the result to b
x = numpy.linalg.solve(A+R, b)
print numpy.dot(A, x)
print abs(list(numpy.dot(A, x)) - b)

#solve (A+R)x=v, calculate Ax and compare the result to v
y = numpy.linalg.solve(A+R, v)
print numpy.dot(A, y)
print abs(list(numpy.dot(A, y)) - v)



#Result

#[ 1.01911641  1.01690601  1.01469561  1.01248521  1.01027481  1.00806442
#  1.00585402  1.00364362  1.00143322  0.99922282]

#[ 0.01911641  0.01690601  0.01469561  0.01248521  0.01027481  0.00806442
#  0.00585402  0.00364362  0.00143322  0.00077718]


#[ 0.96437364  1.96186951  2.95936538  3.95686124  4.95435711  5.95185298
#  6.94934884  7.94684471  8.94434058  9.94183645]

#[ 0.03562636  0.03813049  0.04063462  0.04313876  0.04564289  0.04814702
#  0.05065116  0.05315529  0.05565942  0.05816355]

#the errors are quite small, so this noise idea is a good one to answer the question