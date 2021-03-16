import math
width = float(input('Insert the width of the wall in meters: '))
height = float(input('Insert the height of the wall in meters: '))
area = width * height
print(f'Total wall area: {area:.2f} m²')
ink = int(input('Insert how many m² each can of paint can paint: '))
print(f'Total cans of paint needed to paint the wall is {math.ceil(area / ink)}')
