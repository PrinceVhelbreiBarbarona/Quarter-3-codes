
arr = [[4500, 5200, 4800, 5000, 5300],
       [4000, 4100, 3900, 4200, 4600],
       [6000, 5800, 5900, 6100, 6200]]
days = []
mo = [row[0] for row in arr]
te = [row[1] for row in arr]
we = [row[2] for row in arr]
th = [row[3] for row in arr]
fr = [row[4] for row in arr]
mon = sum(mo)
tue = sum(te)
wed = sum(we)
thu = sum(th)
fri = sum(fr)
days.extend([mon, tue, wed, thu, fri])
active_day = max(days)
print("Monday Total Steps:", mon)
print("Tuesday Total Steps:", tue)
print("Wednesday Total Steps:", wed)
print("Thursday Total Steps:", thu)
print("Friday Total Steps:", fri)
print("The most active day has total steps of:", active_day)