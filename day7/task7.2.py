def log_call(func):
    def wrapper(*args,**kwargs):
        print("function name: ",func.__name__)
        print("arguments: ",args)
        return func(*args,**kwargs)
    return wrapper
@log_call
def add(a,b):
    return a+b
print(add(10,20))
@log_call
def multiply(a,b):
    return a*b
print(multiply(2,5))
@log_call
def greet(name):
    print("hello",name)
greet("asla")