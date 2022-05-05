import threading
def worker(count):
    print("Este es el %s thread " % count)
    return
threads = list()
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
