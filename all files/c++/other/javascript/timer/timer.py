import time

milliseconds = time.ctime()
seconds = time.time()
while True:
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    time.sleep(1.5)
    print(milliseconds, " since start")