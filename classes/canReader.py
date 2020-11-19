from threading import Thread
import can
try:
    import SimpleQueue 
except ImportError:
    from multiprocessing.queues import SimpleQueue



class CanReader(Thread):
    def __init__(self, channel):
        super().__init__(daemon=True)
        try:
        self._bus = can.interface.Bus(channel=channel)    
        except NotImplementedError:
            pass
        self._queues = {}

    def register(self, canid):
        if canid not in self._queues:
            self._queues[canid] = []
        queue = SimpleQueue()
        self._queues[canid].append(queue)        
        return queue

    def run(self):
        while True:
            msg = self._bus.recv()
            for q in self._queues[msg.arbitration_id]:
                q.put(msg)
                