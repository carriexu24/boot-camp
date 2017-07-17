import time
import numpy

#define Eliminate
def Eliminate(A, b):
    m = len(A[0])
    n = len(A)

    #for each column of A
    for i in range(m):

        #if the pivot == 0, then return an error
        if A[i][i] == 0:
            print "A failure has happened."
            return StandardError

        #calculate the scaler, and do eliminations
        for t in range(i+1, n):
            scaler = A[t][i] / A[i][i]
            for r in range(m):
                A[t][r] = A[t][r] - scaler * A[i][r]
            b[t] = b[t] - scaler * b[i]

        #print the results of each elimination
        #when do Problem 2 B., these two operations should be ignored
        #print A
        #print b

    return (A, b)



#Problem 2 A.

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



#Result

#[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, -10, -20, -30, -40, -50, -60, -70, -80, -90], [0, -20, -40, -60, -80, -100, -120, -140, -160, -180], [0, -30, -60, -90, -120, -150, -180, -210, -240, -270], [0, -40, -80, -120, -160, -200, -240, -280, -320, -360], [0, -50, -100, -150, -200, -250, -300, -350, -400, -450], [0, -60, -120, -180, -240, -300, -360, -420, -480, -540], [0, -70, -140, -210, -280, -350, -420, -490, -560, -630], [0, -80, -160, -240, -320, -400, -480, -560, -640, -720], [0, -90, -180, -270, -360, -450, -540, -630, -720, -810]]
#[1, -10, -20, -30, -40, -50, -60, -70, -80, -90]

#[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, -10, -20, -30, -40, -50, -60, -70, -80, -90], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#[1, -10, 0, 0, 0, 0, 0, 0, 0, 0]

#A failure has happened.
#<type 'exceptions.StandardError'>


#[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, -10, -20, -30, -40, -50, -60, -70, -80, -90], [0, -20, -40, -60, -80, -100, -120, -140, -160, -180], [0, -30, -60, -90, -120, -150, -180, -210, -240, -270], [0, -40, -80, -120, -160, -200, -240, -280, -320, -360], [0, -50, -100, -150, -200, -250, -300, -350, -400, -450], [0, -60, -120, -180, -240, -300, -360, -420, -480, -540], [0, -70, -140, -210, -280, -350, -420, -490, -560, -630], [0, -80, -160, -240, -320, -400, -480, -560, -640, -720], [0, -90, -180, -270, -360, -450, -540, -630, -720, -810]]
#[1, -9, -18, -27, -36, -45, -54, -63, -72, -81]

#[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, -10, -20, -30, -40, -50, -60, -70, -80, -90], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#[1, -9, 0, 0, 0, 0, 0, 0, 0, 0]

#A failure has happened.
#<type 'exceptions.StandardError'>




#Problem 2 B.

#list of matrix size n
#I make smaller n because my code is too slow
n = [100, 200, 300, 400, 500, 600]

#list of time using linalg.solve
timeL = []

#list of time using Eliminate.py
timeE = []

#for each size
for i in n:

    #build a n * n R(e)
    R = numpy.random.rand(i, i)

    #build w
    w = i * [1]

    #record the time using linalg.solve
    time1 = time.clock()
    x = numpy.linalg.solve(R, w)
    time2 = time.clock()
    timeL.append(time2 - time1)

    #record the time using Eliminate.py
    time3 = time.clock()
    Eliminate(R, w)
    time4 = time.clock()
    timeE.append(time4 - time3)

print timeL
print timeE



#Result

#[0.010867999999999989, 0.0011779999999999013, 0.005190999999999946, 0.001782999999999646, 0.005336999999997261, 0.008749000000008778]

#[0.9150769999999999, 3.285552, 10.484211, 20.696708, 39.315771, 71.077506]

