# Timer For Podcast

import time

times = [10*60,    10*60,   25*60,          5*60]
names = ["Warmup", "Intro", "Main Section", "Outro"]

startTime = time.time()

timeElap = startTime-startTime
for t,n in zip(times, names):
    print(n)
    reported = False
    while (timeElap) < t:
        timeElap = (time.time() - startTime)
        if timeElap%60 < .01 and not reported:
            print(str(int(timeElap/60))+'/'+str(int(t/60)))
            reported = True
        if timeElap%60 > .01 and reported:
            reported = False
    timeElap = startTime-startTime
    startTime = time.time()
