import numpy
k = map(int,raw_input().split())
a,b = [],[]
for i in xrange(k[0]):
    a.append(map(int,raw_input().split()))
for i in xrange(k[0]):
    b.append(map(int,raw_input().split()))
A,B = numpy.array(a),numpy.array(b)
print numpy.add(A,B)
print numpy.subtract(A,B)
print numpy.multiply(A,B)
print numpy.divide(A,B)
print numpy.mod(A,B)
print numpy.power(A,B)
