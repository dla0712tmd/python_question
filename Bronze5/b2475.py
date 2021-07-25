a, b, c, d , e = map(int , input("고유번호를 입력해주세요").split())

f = (a ** 2) + (b ** 2) + (c ** 2) + (d ** 2) + (e ** 2)

print(f % 10)