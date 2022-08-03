import ray
import time

ray.init(address="auto")

@ray.remote
def f(i):
    time.sleep(1)
    return i

futures = [f.remote(i) for i in range(100)]
ray.get(futures)
print(ray.get(futures))
