import time

def decorator_1(given_function):
    def caltime(*arg1, **args2):
        boshlangan = time.time()
        response = given_function(*arg1, **args2)
        tugagan = time.time()
        oraliq = tugagan - boshlangan
        print(f"{given_function.__name__} call executed in {oraliq:.6f} sec")
        return response
    return caltime
