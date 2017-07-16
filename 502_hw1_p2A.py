import numpy

#define Eliminate
def Eliminate(A, b):
    m = len(A[0])
    n = len(A)

    #A should be a square matrix
    if m != n:
        print "You should input a n*n A."
        return StandardError

    #for each column of A
    for i in range(m):

        #set the location of the pivot
        j = i

        #if the pivot == 0, then move to the next row
        while A[j][i] == 0:
            j += 1

            #if in every row the pivot == 0, return an error
            if j == n:
                print "This equation can't be solved."
                return StandardError

        #if the pivot has been moved, change the rows
        if j > i:
            myline = A[i]
            A[i] = A[j]
            A[j] = myline

        #calculate the scaler, and do eliminations
        for t in range(i+1, n):
            scaler = A[t][i] / A[i][i]
            for r in range(m):
                A[t][r] = A[t][r] - scaler * A[i][r]
            b[t] = b[t] - scaler * b[i]

        #print the results of each elimination
        print A
        print b

    return (A, b)

#define A
A = []
for i in range(10):
    myline = []
    for j in range(10):
        myline.append(10*i+j+1)
    A.append(myline)

#define v
v = []
for i in range(10):
    v.append(i+1)

#define b
b = 10*[1]

#build a 10 * 10 R(e)
R = numpy.random.rand(10, 10)

#make copies
A1 = [row[:] for row in A]
A2 = [row[:] for row in A]
v1 = v[:]
b1 = b[:]

print Eliminate(A1, b1)
print Eliminate(A2, v1)

