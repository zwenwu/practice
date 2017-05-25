import threading   #引入线程
import time
 
condition = threading.Condition()  #条件变量
books = 0
 
class Writer(threading.Thread):
    '''写着'''
    ix = [0] # 生产者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self, ix=0):
        super().__init__()
        self.ix[0] += 1
        self.setName('写者' + str(self.ix[0]))
 
    def run(self):
        global condition, books
        
        while True:
            if condition.acquire():
                if books < 16:
                    books += 1;
                    print("{}：我努力写了1本书，现在书籍总数量 {}".format(self.getName(), books))
                    condition.notify()
                else:
                    print("{}：库存充足(16)。让我休息会儿，现在书籍总数量 {}".format(self.getName(), books))
                    condition.wait();
                condition.release()
                time.sleep(2)


class Reader(threading.Thread):
    '''读者'''
    ix = [0] 

    def __init__(self):
        super().__init__()
        self.ix[0] += 1
        self.setName('读者' + str(self.ix[0]))
 
    def run(self):
        global condition, books
        
        while True:
            if condition.acquire():
                if books > 0:
                    books -= 1
                    print("{}：我借了了1本书看，现在书籍数量 {}".format(self.getName(), books))
                    condition.notify()
                else:
                    print("{}：只剩下0本书，我停止借书。现在书籍数量 {}".format(self.getName(), books))
                    condition.wait();
                condition.release()
                time.sleep(1)



if __name__ == "__main__":
    for i in range(10):
        p = Writer()
        p.start()
 
    for i in range(10):
        c = Reader()
        c.start()