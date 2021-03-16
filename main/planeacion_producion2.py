from pulp import *
import pandas as pd
# https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99
# https://github.com/ekhoda/optimization-tutorial/
# https://relopezbriega.github.io/blog/2017/01/18/problemas-de-optimizacion-con-python/#:~:text=El%20objetivo%20de%20la%20programaci%C3%B3n,est%C3%A1n%20sujetas%20a%20restricciones%20lineales.
# https://ichi.pro/es/programacion-lineal-usando-python-38164786352096
data = pd.read_csv('/home/david/PycharmProjects/estadistica_avanzada/optimizacion/punto2.csv', sep='~', decimal=',')

prob = LpProblem("Planeación de la producción 2",LpMinimize)

planta = list(data['planta'])
productos = [1,2]
demanda = list(data['demanda'])
costo = [list(data['costo_p1']),
        list(data['costo_p2'])]
tiempo = [
list(data['p1'].astype(float)),
        list(data['p2'].astype(float))
]
mes = [list(data['demanda_p1']),
        list(data['demanda_p2'])]

capacidad = list(data['capacidad']*60)
produccion_maxima = list(data['p_maxima'])
costos = makeDict([productos, planta], costo,0)

# Posibles combinaciones de productos y plantas
combinaciones = [(c,b, j) for c in productos for b in planta for j in demanda ]

# creamos diccionario x que contendrá la candidad de producto generado por planta
x = pulp.LpVariable.dicts("producto_planta", (productos, planta, demanda),
                        lowBound = 0,
                        cat = LpInteger)

prob += lpSum([x[c][b][j]*costos[c][b] for (c,b,j) in combinaciones])

# restricciones de capacidad de producto por planta
for i in demanda:
    for b in planta:
        prob += lpSum([x[c][b][i] for c in productos]) >= produccion_maxima[b-1]

# demanda por mes con balanceo de inventario, producto 1
#prob += lpSum([x[1][c][1] for c in planta]) >= mes[0][0]

for c in planta[1:]:
    prob.addConstraint(LpConstraint(
        e=lpSum(x[2][i][c] for i in planta),
        sense=LpConstraintGE,
        rhs=mes[1][c-1]))

# inv balance for first period
prob.addConstraint(LpConstraint(
    e=lpSum(x[2][i][1] for i in planta),
    sense=LpConstraintGE,
    rhs=mes[1][0]))

for c in planta[1:]:
    prob.addConstraint(LpConstraint(
        e=lpSum(x[1][i][c] for i in planta),
        sense=LpConstraintGE,
        rhs=mes[0][c-1]))

# inv balance for first period
prob.addConstraint(LpConstraint(
    e=lpSum(x[1][i][1] for i in planta),
    sense=LpConstraintGE,
    rhs=mes[0][0]))


"""
prob += lpSum([x[1][c][2]] for c in planta) + (lpSum([x[1][c][1]- lpSum(mes[0][0]) for c in planta]) ) >= mes[0][1]
prob += lpSum([x[1][c][3]-(x[1][c][2]) for c in planta]) +mes[0][1] >= mes[0][2]
prob += lpSum([x[1][c][4]-(x[1][c][3]) for c in planta]) +mes[0][2] >= mes[0][3]
prob += lpSum([x[1][c][4] for c in planta]) + [lpSum([x[1][c][3] for c in planta])] <= mes[0][3]

prob += lpSum([x[1][c][3] for c in planta]) -lpSum([x[1][c][2] for c in planta]) >= mes[0][2]
prob += lpSum([x[1][c][4] for c in planta]) -lpSum([x[1][c][3] for c in planta]) >= mes[0][3]

# demanda por mes con balanceo de inventario, producto 2

prob += lpSum([x[2][c][1] for c in planta]) >= mes[1][0]
prob += lpSum([x[2][c][2] for c in planta]) -lpSum([x[2][c][1] for c in planta]) >= mes[1][1]
prob += lpSum([x[2][c][3] for c in planta]) -lpSum([x[2][c][2] for c in planta]) >= mes[1][2]
prob += lpSum([x[2][c][4] for c in planta]) -lpSum([x[2][c][3] for c in planta]) >= mes[1][3]

for i in productos:
    for b in range(len(mes[0])):
        prob += lpSum([x[i][c][b+1] for c in planta]) >= mes[i-1][b]
"""
# capacidad de pprodicion
for i in planta:
    for b in planta:
        prob += lpSum([x[1][b][i]*tiempo[0][b-1]]) + lpSum([x[2][b][i]*tiempo[1][b-1]])  <= capacidad[b-1]

demanda_total = [10400, 7700]
prob += lpSum([x[1][c][i]] for c in planta for i in planta) <= demanda_total[0]
prob += lpSum([x[2][c][i]] for c in planta for i in planta) <= demanda_total[1]

# Los datos del problema son exportado a archivo .lp
prob.writeLP("problemaDeTransporte.lp")

# Resolviendo el problema.
prob.solve()

# Imprimimos el estado del problema.
print("Status: {}".format(LpStatus[prob.status]))

# Imprimimos cada variable con su solución óptima.
for v in prob.variables():
    print("{0:} = {1:}".format(v.name, v.varValue))

# Imprimimos el valor óptimo de la función objetivo
print("Costo total de transporte = {}".format(prob.objective.value()))


