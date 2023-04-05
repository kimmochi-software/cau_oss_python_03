# +와 -는 함수로 정의한다
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

# arithmetic_ops 함수를 호출하며 수행한다.
# arithmetic_ops는 연산에 관한 함수로, 내부에서 사용자에게 정수 2개를 입력받은 뒤
# 전달받은 매개함수로 정수를 전달한다
def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

# while문을 이용하여 반복 수행한다.
while True:
    op = input("input operation:")
    if op == "end":
        print("Exit program")
        break
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add)
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda x, y: x*y) # 익명함수(lambda) 사용
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda x, y: x/y) # 익명함수(lambda) 사용
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda x, y: x%y) # 익명함수(lambda) 사용
    else:
        print("Invalid operation")
        continue
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력
