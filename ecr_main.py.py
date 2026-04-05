#Ecuación de Compatibilidad Relacional 1.0
import math

#La Ecuación de Compatibilidad Relacional es un modelo matemático que nació desde la necesidad de saber si una relación
#es viable o no, para llevar a cabo este modelo, se necesita pensar en que los valores de las variables son de la rela-
#ción, no de uno solo de los individous, sabiendo esto, he planteado las siguientes variables
M = float(input("¿Cuál es la madurez de la relación? (0-10) "))
B = float(input("¿Cuál es el nivel de Compatibilidad actual de la relación? (0-10) "))
A = float (input("¿Cuál es el nivel de confianza y de resilencia actualmente construido en la relación? (0-10) "))
S = float (input("¿Cuál es el nivel de estabilidad (paz) que hay dentro de la relación? (0-10) "))
E = float (input("¿Cuál es el nivel de pasión/química que hay dentro de la relación? (0-10) "))

#Moduladores especiales:
C = float(input("Cuál es el nivel de reciprocidad y esfuerzo que hay dentro de la relación? (0-10) "))
I = float(input("Cuál es el nivel de impulsividad/riesgo dentro de la relación (toxicidad, engaños, etc)? (0-10) "))

#Este modelo funciona con las  siguientes formulas, las cuáles son formulas vistas comunmente en elementos físicos,
# pero las relaciones ser sistemas tan complejos, les queda al pelo estas formulas:

bloque_estructural = (M+B+(0.5*A)+S+(0.7*E))/4.2 #El denominador 4.2 representa la suma de los pesos de las variables
# estructurales, funcionando como un normalizador matematico

multplicador_de_eficiencia = math.sqrt(C/10) #La reciprocidad no se suma,se multiplica. Si la reciprocidad es cero,
# el NER se volverá cero, ya que si no existe reciprocidad, no existe relación.

colapso_cubico = 0.01 * (I**3) #Permite pequeños errores humanos (como las inseguridades), pero un índice de toxicidad
# alto crece al cubo, destruyendo la estructura de forma exponencial y mandando el sistema a números negativos

NER = (bloque_estructural * multplicador_de_eficiencia) - colapso_cubico #Número de Estabilidad Relacional
print (f"El NER de la relación es: {round(NER,2)}")

#Escala de Interpretación

#Cuando pense en este modelo matematico, lo hice con la visión de algo parecido del Número de Reynolds en la mecánica de
# fluidos, ya que iba a ser más fácil saber catalogar cuando una relación sería viable o no en la ECR. Por lo tanto,
# se utilizaron los siguientes parametros

print ("Diagnostico:")

if NER >= 8.0:
    print ("Interpretacion: Relación Altamente Sólida (Estructura Óptima)") #NER 8.0 - 10.0
elif NER >= 6.0:
    print ("Interpretación: Relación Viable con Buenas Bases (Requiere Mantenimiento)") #NER 6.0 - 7.9
elif NER >= 4.0:
    print ("Interpretación: Relación Inestable o Condicionada (Fallos Estructurales)") #NER 4.0 - 5.9
elif NER >= 2.0:
    print ("Interpretación: Alta Probabilidad de Conflicto (Peligro de cedencia)") #NER 2.0 - 3-9
else:
    print ("Interpretación: Relación Claramente Tóxica (Colapso Inminente)") #NER < 2.0

#Condición de Frontera:

#Si la compatibilidad presente es menor a 4, el sistema sufre de vectores divergentes (proyectos de vida opuestos).
#Estructuralmente, colapsará a largo plazo independientemente del puntaje final

if B < 4:
    print ("ALERTA DE CIZALLAMIENTO: Proyectos de Vida Opuestos, Riesgo de Colapso a Largo Plazo.")