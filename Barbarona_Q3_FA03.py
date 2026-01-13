arr = [[4500, 5200, 4800, 5500, 5300],
       [4000, 4100, 3900, 4200, 4600],
       [6000, 5800, 5900, 6100, 6200]]
ma = max(arr[0])
mi = min(arr[0])
av = sum(arr[0]) / len(arr[0])
su = sum(arr[0])
maa = max(arr[1])
mii = min(arr[1])
avv = sum(arr[1]) / len(arr[1])
suu = sum(arr[1])
maaa = max(arr[2])
miii = min(arr[2])
avvv = sum(arr[2]) / len(arr[2])
suuu = sum(arr[2])
print(f"Friend 1 - Total Steps: {su} | Avarage Steps: {av} | Min Steps: {mi} | Max Steps: {ma}")
print(f"Friend 2 - Total Steps: {suu} | Avarage Steps: {avv} | Min Steps: {mii} | Max Steps: {maa}")
print(f"Friend 3 - Total Steps: {suuu} | Avarage Steps: {avvv} | Min Steps: {miii} | Max Steps: {maaa}")