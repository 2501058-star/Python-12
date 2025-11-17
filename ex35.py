a = {100, 200, 300, 400, 500}
a.intersection_update({400, 500, 600, 700, 800})
print(a)

a = {100, 200, 300, 400, 500} 
a.difference_update({400, 500, 600, 700, 800})
print(a)

a = {100, 200, 300, 400, 500} 
a.symmetric_difference_update({400, 500, 600, 700, 800})
print(a)