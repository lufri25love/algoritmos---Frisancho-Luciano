"""
Ejercicio 5: Gestión de Triaje en Guardia Médica (Prioridad)
Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
(Crítico).
Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
[[&quot;Paciente&quot;, Prioridad], ...]. Crear la función atender_siguiente(cola_espera) que seleccione
al próximo paciente en ser atendido.
Requisitos:
● Buscar al paciente que posea la prioridad más alta (mayor número).
● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
la guardia (criterio FIFO).
● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
indicando su nombre y nivel de urgencia.
Ejemplo de Entrada: [[&quot;Carlos&quot;, 1], [&quot;Ana&quot;, 3], [&quot;Roberto&quot;, 2], [&quot;Lucía&quot;, 3]] Salida
Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
la siguiente será Lucía (Nivel 3).
"""

def atender_siguiente(cola):
    mayor = 0
    posicion = 0
    for i in range(len(cola)):
        if cola[i][1] > mayor:
            mayor = cola[i][1]
            posicion = i
    paciente = cola.pop(posicion)
    return "Se atiende al paciente " + paciente[0] + " (Nivel " + str(paciente[1]) + ")"
cola = []

cantidad = int(input("Ingrese la cantidad de pacientes : "))

for i in range(cantidad):
    nombre = input("Nombre del paciente : ")
    prioridad = int(input("Prioridad (1-3) del paciente : "))
    cola.append([nombre, prioridad])

print(atender_siguiente(cola))