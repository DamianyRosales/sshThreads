from threading import Thread

class Pool():
    instances = []

    def add(self, func, *args):
        a = []
        for i in args: a.append(i)
        
        self.instances.append(
             Thread(target=func, args=a)
        )
    
    def delete(self, func):
        self.instances.remove(func)
 
    def is_running(self, x):
        return self.instances[x].is_alive()
    
    def initialize(self):
        for i in self.instances: i.start()

    def finish(self):
        for i in self.instances: i.join()

    def start(self, x):
        self.instances[x].start()

    def join(self, x):
        self.instances[x].join()

