#1
import time
a = []
for x in range(10000):
    a.append(x)
print 'Sequential Search\n'

def seqSearch(alist, data):
    start = time.clock()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == data:
            found = True
        else:
            pos = pos+1
    stop = time.clock()

    return found, pos, stop-start
print ('Search 25')
for i in range(10):
    print i+1, ('%3s, %d, kecepatan eksekusi: %10.10f' %seqSearch(a,25))
print ('Search 5555')
for i in range(10):
    print i+1, ('%3s, %d, kecepatan eksekusi: %10.10f' %seqSearch(a,5555))

#2
import time
a = []
for x in range(10000):
    a.append(x)
print 'Sequential Search (Sorting)\n'

def sortSeqSearch(alist, data):
    start = time.clock()
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == data:
            found = True
        else:
            if alist[pos] > data:
                stop = True
            else:
                pos = pos+1
    end = time.clock()

    return found, pos, end-start

for i in range(10):
    print i+1, ('%3s, %d, kecepatan eksekusi = %10.10f' %sortSeqSearch(a,255))

#3
import time
a = []
for x in range(10000):
    a.append(x)
print 'Binary Search\n'

def binSearch(alist, data):
    start = time.clock()
    first = 0
    last = len(alist)-1
    found = False
    while first < last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == data:
            found = True
        else:
            if data < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    end = time.clock()

    return found, end-start

for i in range(10):
    print i+1, ('%2s, kecepatan eksekusi = %10.10f' %binSearch(a,9995))

#4
import time
a = []
for x in range(10000):
    a.append(x)
print 'Binary Search (Recursive)\n'

def binSearchRec(alist, data):
    start = time.clock()
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == data:
            return True
        else:
            if data < alist[midpoint]:
                return binSearch(alist[:midpoint], data)
            else:
                return binSearch(alist[midpoint+1:], data)
    stop = time.clock()
    return stop-start

for i in range(10):
    print i+1, ('%2s, kecepatan eksekusi = %10.10f' %binSearchRec(a,55))
print '\n Data dalam list:\n'
print a
