import threading

class ThreadWithResult(threading.Thread):
  def __init__(self, *args, **kwargs):
    super(ThreadWithResult, self).__init__(*args, **kwargs)
    self.result = None

  def run(self):
    if self._target is not None:
      self.result = self._target(*self._args, **self._kwargs)

def suma(a, b):
  return a + b

t = ThreadWithResult(target=suma, args=(3, 4))
t.start()
t.join()
print(t.result) # 7