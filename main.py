import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

kwargsAcceptFun(ism="Jasur", yosh=25, student_id="230220", vazifasi="Student")

result = typeBasedTransformer(
    yosh=25, 
    ism="Sarvar", 
    haqiqat=True, 
    raqamlar=[1, 2, 3], 
    malumotlar={"ism": "Sarvar", "yosh": 25}
)
print(result)

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()
