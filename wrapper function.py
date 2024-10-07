import time
n=10000000


def wrapper(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start_time = time.time()* 1000
        func(*args,**kwargs)
        end_time = time.time() * 1000
        diff = end_time - start_time

        print(f"execution time for n = {n} is \n {diff} mili sec")
    return(wrapper)

@wrapper_fn
def testfn(n):
    for i in range(0,n):
        res = i*10


testfn(n)