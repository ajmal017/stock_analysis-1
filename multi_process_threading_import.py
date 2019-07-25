#Multiprocess_pool(self, course, course_data)
#用于简单计算，传参分别为调用def方法，和方法参数（只可以参入一个参数），可批量开启，简单速度快,
# multiprocessing.Pool不能直接用multiprocessing.Queue进行通信，只能通过共享内存，或者用multiprocessing.Manager()进行进程间通信。

#Multiprocess_queue(self,course,course_count,course_data)
#用于复杂计算，传参分别为def方法，线程数目，方法参数（只可以参入一个参数），
# multiprocessing.Process 可以直接用multiprocesssing.Queue等进行通信