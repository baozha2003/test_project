from time import sleep, ctime
import threading


# 音乐
def muisc(func, loop):
    for i in range(loop):
        print("I was listening to %s! %s" % (func, ctime()))
        sleep(2)


# 电影
def movie(func, loop):
    for i in range(loop):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(2)


# 创建线程组
threads = []

# 创建线程组t1并添加到线程组
t1 = threading.Thread(target=muisc, args=("爱情", 2))
threads.append(t1)

# 创建线程组t2并添加到线程组
t2 = threading.Thread(target=movie, args=("阿凡达", 2))
threads.append(t2)

if __name__ == '__main__':
    # 启动线程组
    for t in threads:
        t.start()
    # 守护线程组
    for t in threads:
        t.join()
    print('all end:%s' % ctime())
