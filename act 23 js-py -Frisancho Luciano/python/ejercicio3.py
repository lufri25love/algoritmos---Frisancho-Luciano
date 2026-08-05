"""
Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = [&quot;Boca&quot;, &quot;River&quot;, &quot;Racing&quot;] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8).
"""

def ordenar(equipos, puntos, dg):
    for i in range(len(equipos)):
        for j in range(i + 1, len(equipos)):
            if puntos[j] > puntos[i] or (puntos[j] == puntos[i] and dg[j] > dg[i]):
                equipos[i], equipos[j] = equipos[j], equipos[i]
                puntos[i], puntos[j] = puntos[j], puntos[i]
                dg[i], dg[j] = dg[j], dg[i]

equipos = ["Boca", "River", "Racing"]
puntos = [12, 15, 12]
dg = [8, 5, 10]

ordenar(equipos, puntos, dg)
for i in range(len(equipos)):
    print(i + 1, equipos[i], puntos[i], "pts", "DG", dg[i])