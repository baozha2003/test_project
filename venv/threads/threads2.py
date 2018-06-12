from time import ctime, sleep
import threading


def super_player(file_, time):
    for i in range(2):
        print('start playing: %s! %s' % (file_, ctime()))
        sleep(time)


# 播放文件与播放时长
lists = {'爱情.mp3': 3, '阿凡达.mp4': 5, '我和你.mp3': 4}

threads = []
files = range(len(lists))

for file_, time in lists.items():
    t = threading.Thread(target=super_player, args=(file_, time))
    threads.append(t)

if __name__ == '__main__':
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

    print('end:%s' % ctime())
