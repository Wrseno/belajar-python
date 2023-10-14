C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9) / 5) * x + 32 , C))
print(F)
[102.56, 97.7, 99.14, 100.4, 100.03999999999999]
C = list(map(lambda x: (float(5) / 9) * (x - 32), F))
print(C)