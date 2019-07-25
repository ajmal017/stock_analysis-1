import multi_process_threading_root
import multiprocessing as mp

import time

def job2(a):
    a=a+1

    return str(a)


def job(q,x):
    res=0
    for i in range(x):
        res=i

    q.put(res)




if __name__=='__main__':
    #multicore(jobs)
    #

    #multiprocess_root.multiprocess().Multiprocess_pool(job,10)
    multi_process_threading_root.multiprocess().Multiprocess_queue(job,  [99,55,666,7,7,8,987,654])
    multi_process_threading_root.multiprocess().Multiprocess_pool(job2, [12, 42, 5, 7, 4, 6, 4])
