def call_counter(func):
    def wrap(*args, **kwargs):
        wrap.counter += 1
        return func(*args, **kwargs)
    wrap.counter = 0
    return wrap


@call_counter
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(20):
    print("fib:",fib(i), fib.counter)

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo = call_counter(fibo)
for i in range(20):
    print("fibo:",fibo(i), fibo.counter)


class BetterDecor:
    def __init__(self, func):
        self.counter = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)

@BetterDecor
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@BetterDecor
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

fib(20)
fact(100)
print(fib.counter)
print(fact.counter)


def argdecor(x,y,z):
    a = x + y + z
    def wrap(func):
        def wrapped_f(*args, **kwargs):
            print('the real args are',x,y,z)
            print('remember the old a:', a)
            return func(*args, **kwargs)
        return wrapped_f
    return wrap

def greeting_decor(mesg):
    def wrap(func):
        def wrapped_f(*args, **kwargs):
            print(mesg, 'sir')
            return func(*args, **kwargs)
        return wrapped_f
    return wrap

print("======================")

@greeting_decor('Good Evening')
def greet():
    pass

greet()

# it can implemented this way
def greeter():
    pass

greeter = greeting_decor('Good Morning')(greeter)
greeter()



class BetterTimerDecor:
    def __init__(self, counter, current_time):
        self.counter = 0
        self.current_time = current_time

    def __call__(self, func):
        def wrap(*args, **kwargs):
            self.counter += 1
            return func(*args, **kwargs)
        wrap.wrapper = self
        return wrap


import time

@BetterTimerDecor(0,time.time())
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(30))
print(fib.wrapper.counter)
print(fib.wrapper.current_time)


# app.route

class funmapper:
    def __init__(self):
        self.funcdict = {}
    
    def route(self, pattern):
        def wrap(func):
            self.funcdict[pattern] = func
            return func
        return wrap

    def namecall(self, name, *args, **kwargs):
        if name in self.funcdict:
            self.funcdict[name](*args, **kwargs)

app = funmapper()

@app.route('/')
def hello():
    print('Hello World')

app.namecall('/')
print(hello)