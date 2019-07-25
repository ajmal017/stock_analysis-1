import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    import time
    time.sleep(5)
    q.put(res)    #queue

if __name__=='__main__':
    queue = mp.Queue()
    a=[1,2]
    a[0] = mp.Process(target=job,args=(queue,))
    a[1] = mp.Process(target=job,args=(queue,))
    a[0].start()
    a[1].start()
    a[0].join()
    a[1].join()
    res1 = queue.get()
    res2 = queue.get()
    print(res1)
    print(res2)
    print(res1+res2)