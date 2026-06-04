import time 
def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        end_time=time.time()
        result=func(*args,**kwargs)
        print(f"time taken: ",{end_time-start_time})
        return result
    return wrapper
@timer
def count_number():
    for i in range(10000000):
         pass
count_number()
