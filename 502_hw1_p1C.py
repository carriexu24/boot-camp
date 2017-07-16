import numpy

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

#build a 10 * 10 array R(e)
R = numpy.random.rand(10, 10)
R = numpy.array(R)

#solve (A+R)x=b, calculate Ax and compare the result to b
x = numpy.linalg.solve(A+R, b)
print numpy.dot(A, x)
print abs(list(numpy.dot(A, x)) - b)

#solve (A+R)x=v, calculate Ax and compare the result to v
y = numpy.linalg.solve(A+R, v)
print numpy.dot(A, y)
print abs(list(numpy.dot(A, y)) - v)
