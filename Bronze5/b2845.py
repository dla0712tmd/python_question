l , p = map(int, input("1m*2당 사람수와 넓이를 입력: ").split())
a, b, c, d, e = map(int, input("다섯개의 신문기사의 넓이를 입력: ").split())

den = l * p

print(a - den , b - den, c - den, d - den, e - den)
