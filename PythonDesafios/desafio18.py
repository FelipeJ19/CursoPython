from math import radians, sin, cos, tan
ang = int(input('Digite o angulo: '))
rad = radians(ang)
seno = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('{:.2f}'.format(seno))
print('{:.2f}'.format(cos))
print('{:.2f}'.format(tan))
