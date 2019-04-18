

import statistics as stats

def calculate_prom(depart_list):
    temp_sum =0
    temp_count =len(depart_list)

    for prom in depart_list:
        temp_sum =temp_sum +prom

    final_prom =temp_sum /temp_count

    return final_prom

def pos_item(departament_list):
    hottest_tem =departament_list[0]
    pos_element = 0
    cont =1

    for hot in departament_list:
        if hot >hottest_tem:
            hottest_tem =hot
            pos_element =cont
        cont += 1

    return pos_element

def hottest_temperature(departament_list):
    hottest_tem =departament_list[0]

    for hot in departament_list:
        if hot >hottest_tem:
            hottest_tem =hot

    return hottest_tem

def desviacion_estandar(departament_list):
    desviacion = stats.pstdev(departament_list)

    return desviacion
