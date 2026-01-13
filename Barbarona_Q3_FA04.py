arr = [[4500, 5200, 4800, 5000, 5300],
       [4000, 4100, 3900, 4200, 4600],
       [6000, 5800, 5900, 6100, 6200]]
arrts = []
n = max(arr[0])
nn = max(arr[1])
nnn = max(arr[2])
arrts.append(n)
arrts.append(nn)
arrts.append(nnn)
ma = max(arrts)
mi = min(arrts)
dif = ma - mi
print("The highest steps is:", ma)
print("The difference between the highest and lowest steps is:", dif)
