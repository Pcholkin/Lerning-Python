import math

x=(float(input(f'Enter degrees')))
print(f'it {math.radians(x)} radians')

y=(float(input(f'Enter radians')))
print(f'it {math.degrees(y)} degrees')

# Вроде тоже рабочий вариант чтобы узнать градусы

z=(float(input(f'Enter radian')))
print(f'it {z*57.2957795} degrees')

r=(float(input(f'Enter degrees')))
print(r * (math.pi/180))     