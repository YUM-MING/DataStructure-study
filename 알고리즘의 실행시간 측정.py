from bisect import insort
import time

myBag = []
start = time.time()
insort(myBag, '축구공')

end = time.time()
print("실행시간 = ", end-start)
