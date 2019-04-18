"""
Solución del laboratorio
"""

from custom_functions import temperature_methods

nacional_list = []
hottest_tem_list = []

for i in range(3):
    departament = input("which is the departament?: ")
    departament_list = []
    for i in range(12):
        temperature = int(input("Please give me the {} temperature: ".format(i + 1)))
        departament_list.append(temperature)
    print(departament_list)

    z = temperature_methods.desviacion_estandar(departament_list)
    print("La desviacion estandar es: ", z)

    x = temperature_methods.calculate_prom(departament_list)
    print("El promedio es: ", x)
    nacional_list.append(x)

    y = temperature_methods.hottest_temperature(departament_list)
    print("La temperatura mas caliente: ", y)
    print("Esta en el mes: ", temperature_methods.pos_item(departament_list))
    hottest_tem_list.append(y)

print(                )

print("El promedio nacional es: ", temperature_methods.calculate_prom(nacional_list))
print("La temperatura del promedio del los 3 fue mas caliente: ",temperature_methods.hottest_temperature(nacional_list))
print("El promedio de la temperatura mas caliente es: ", temperature_methods.calculate_prom(hottest_tem_list))
print("La temperatura mas caliente en todo el año: ", temperature_methods.hottest_temperature(hottest_tem_list))