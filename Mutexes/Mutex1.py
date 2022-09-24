from threading import Semaphore, Thread
import threading
import pytube

mutex = threading.Lock()

def get_video(url):
    video = pytube.YouTube(url)
    video.streams.first().download('./videos')

class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        mutex.acquire()
        get_video(self.url)
        mutex.release()

urls = ["https://www.youtube.com/watch?v=0bZ0hkiIKt0&ab_channel=shtinky", "https://www.youtube.com/watch?v=TtSJmJQfJhg&ab_channel=PepePeepo", "https://www.youtube.com/watch?v=KvxB3Yg5JBQ&ab_channel=PepePeepo", "https://www.youtube.com/watch?v=PvITInUmBJA&ab_channel=SuperSonicWoody", "https://www.youtube.com/watch?v=Y5W8ZbG7zTk&ab_channel=PMEPlus%28Pac-ManEntertainmentPlus%29", "https://www.youtube.com/watch?v=rXlZbn8o7rA&ab_channel=Sessiz", "https://www.youtube.com/watch?v=b0mWsyXYTEI&ab_channel=Angry4Bots", "https://www.youtube.com/watch?v=PpDsiSz6zVk&ab_channel=EliteFull", "https://www.youtube.com/watch?v=sNIdDO-X2ZM&ab_channel=devine", "https://www.youtube.com/watch?v=mOvpWmzceIg&ab_channel=devine"]

threads_semaphore = [Hilo(urls[0]), Hilo(urls[1]), Hilo(urls[2]), Hilo(urls[3]), Hilo(urls[4]), Hilo(urls[5]), Hilo(urls[6]), Hilo(urls[7]), Hilo(urls[8]), Hilo(urls[9])]

for t in threads_semaphore:
    t.start()