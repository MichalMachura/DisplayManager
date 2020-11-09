import cv2 as cv
import numpy as np
import threading as th
import queue
import time


class DisplayManager:
    
    def __init__(self,name='Display', interval=0.2, size=20, on_update=None):
        self.queue = queue.Queue(size)
        self.name = name
        self.end_flag = False
        self.interval = interval
        self.on_update = on_update
        
        self.thread = th.Thread(target=lambda: self.loop(), daemon=True)
        
        
        # print('thread before start')
        self.thread.start()
        print('thread started')
        # cv.namedWindow(self.name)
        
    # thread inside loop function
    def update(self):
        img = None
        flag = False
        # get last img
        while not self.queue.empty():
            img = self.queue.get()
            flag = True
        
        # display last img
        if flag:
            if self.on_update:
                img = self.on_update(img)
            
            cv.imshow(self.name, img)
            cv.waitKey(10)
        
    # thread loop function
    def loop(self):
        # loop while not end with given interval of refresh
        while not self.end_flag:
            self.update()
            time.sleep(self.interval)
    
    # call to put img on display queue 
    def show(self, img):
        self.queue.put(img)
    
    # call for end threading
    def finish(self):
        self.end_flag = True
        
        self.thread.join(5)
        print('thread finished')
    
