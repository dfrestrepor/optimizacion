from pulp import *
import pandas as pd
import os


def planning_production(data, planta,productos, demanda, capacidad, costo ):

    productos = data[productos].tolist()
    demanda = data[demanda].tolist()
    capacidad = data[capacidad].values
    costo = data[costo].values
    planta = range(planta)
    prob = LpProblem("Planeación de la producción",LpMinimize)

    # Variables
    x = pulp.LpVariable.dicts("producto_planta", (productos, planta), lowBound = 0, cat = LpInteger)

    # Posibles combinaciones de productos y plantas
    combinaciones = [(c,b) for c in productos for b in planta]

    # Función objetivo
    prob += lpSum([x[c][b]*costo[c-1][b] for (c,b) in combinaciones])

    # Restricciones de demanda semanal
    for c in productos:
        prob += lpSum([x[c][i]] for i in planta) >= demanda[c-1]

    # Restricción  de capacidad de la planta propía
    prob += lpSum(x[i][0]*capacidad[i-1][0]/capacidad[0][0]  for i in productos) <= capacidad[0][0]

    #Restricciones de capacidad de planta de terceros
    for c in productos:
        prob += lpSum([x[c][1]]) <= capacidad[c-1][1]
        prob += lpSum([x[c][2]]) <= capacidad[c-1][2]
        prob += lpSum([x[c][3]]) <= capacidad[c-1][3]

    # Los datos del problema son exportado a archivo .lp
    prob.writeLP(BASE_DIR + "/output/punto1.lp")
    # Resolviendo el problema
    prob.solve()

    # Imprimimos el estado del problema.
    print("Status: {}".format(LpStatus[prob.status]))

    # Imprimimos cada variable con su solución óptima.
    variable = []
    for v in prob.variables():
        variable.append([v.name, v.varValue])
        print("{0:} = {1:}".format(v.name, v.varValue))

    # Imprimimos el valor óptimo de la función objetivo
    print("Costo total de producción = {}".format(prob.objective.value()))

    variable.append(['Costo total de producción', prob.objective.value()])
    variable.append(['Status', LpStatus[prob.status]])
    return variable

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_csv(BASE_DIR + '/datos/punto1.csv', sep='~', decimal=',')
    # Costo propio como valor constante default = 1
    COSTO_PROPIO = 1
    CAPACIDAD = ['capacidad_propia', 'empresa1', 'empresa2', 'empresa3']
    COSTOS = ['costo_propio', 'costo1', 'costo2', 'costo3']
    DEMANDA = 'demanda'
    data['costo_propio'] = data.costo_propio * COSTO_PROPIO
    result = planning_production(data, 4,'producto', DEMANDA, CAPACIDAD, COSTOS )
    df= pd.DataFrame(result)
    df.to_csv(BASE_DIR + '/output/Resultado_punto1.csv', index=False)