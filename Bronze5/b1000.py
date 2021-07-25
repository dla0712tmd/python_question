#map과 split을 사용하면 자료형을 숫자로 변환한 후 여러 숫자를 한번에 입력할 수 있음
a, b = map(int , input("더할 두 수를 입력해주세요: ").split())

print(a + b)
