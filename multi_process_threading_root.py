import multi_process_threading_config
import multiprocessing as mp

class multiprocess():
    def __init__(self):
        pass

    def Multiprocess_pool(self,course,course_data):#传参计算
        pool = mp.Pool(processes=multi_process_threading_config.core_number)
        multi_res = [pool.apply_async(course, (i,)) for i in course_data]#向线程池实时添加进程
        # 从迭代器中取出
        print([res.get() for res in multi_res])#输出进程结果
        return [res.get() for res in multi_res]

    def Multiprocess_queue(self,course,course_data):
        queue = mp.Queue()
        if course_data:
            queue_res=[mp.Process(target=course,args=(queue,count,)) for count in course_data]#同类 多次 传参计算
            [one_queue.start() for one_queue in queue_res]#批量开启进程
            [one_queue.join() for one_queue in queue_res]#批量添加进程
            all_queue=[queue.get() for count in range(len(course_data))]
            print([x for x in all_queue ])
            return [x for x in all_queue ]

        else:
            queue_res = [mp.Process(target=course, args=(queue,)) for count in range(multi_process_threading_config.core_number)]#非传参式运算
            [one_queue.start() for one_queue in queue_res]
            [one_queue.join() for one_queue in queue_res]
            all_queue = [queue.get() for count in range(len(course_data))]
            print([x for x in all_queue])
            return [x for x in all_queue]



'''
def thread_job(url):
	add_thread=td.Thread(target=get_page,args=(url,))
	#print(td.active_count())#查看所有激活线程数量
	#print(td.enumerate())  # 查看所有激活线程名称
	print(td.current_thread())
	add_thread.start()
	add_thread.join()
'''