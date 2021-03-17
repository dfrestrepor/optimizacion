from pulp import *
import pandas as pd
import os



def  planning_produccion(productos, planta, costo, tiempo, capacidad, produccion_minima, demanda, mes, demanda_total):

    prob = LpProblem("Planeación_producción_2",LpMinimize)
    # diccionario de costos, por plnata y producto
    costos = makeDict([productos, planta], costo,0)
    # Posibles combinaciones de productos, plantas y mes de demanda
    combinaciones = [(c,b, j) for c in productos for b in planta for j in demanda ]
    
    # variable de decisión
    x = pulp.LpVariable.dicts("producto_planta", (productos, planta, demanda),
                            lowBound = 0,
                            cat = LpInteger)
    #función objetivo
    prob += lpSum([x[c][b][j]*costos[c][b] for (c,b,j) in combinaciones])
    
    # Restricciones de niveles mínimo de producción de cada planta (unidades/mes)
    for i in demanda:
        for b in planta:
            prob += lpSum([x[c][b][i] for c in productos]) >= produccion_minima[b-1]

    #Restricciones de niveles mínimo de demanda de producto por mes (unidades/mes)
    for c in demanda:
        prob.addConstraint(LpConstraint(
            e=lpSum(x[2][i][c] for i in planta),
            sense=LpConstraintGE,
            rhs=mes[c-1][1]))
    
    for c in demanda:
        prob.addConstraint(LpConstraint(
            e=lpSum(x[1][i][c] for i in planta),
            sense=LpConstraintGE,
            rhs=mes[c-1][0]))
    
    # Restricciones de capacidad máxima de producción mensual (minutos de mano de obra/unidad)
    for i in planta:
        for b in planta:
            prob += lpSum([x[1][b][i]*tiempo[b-1][0]]) + lpSum([x[2][b][i]*tiempo[b-1][1]])  <= capacidad[b-1]
    

    prob += lpSum([x[1][c][i]] for c in planta for i in planta) <= demanda_total[0]
    prob += lpSum([x[2][c][i]] for c in planta for i in planta) <= demanda_total[1]
    
    # Los datos del problema son exportado a archivo .lp
    prob.writeLP(BASE_DIR + "/output/punto2.lp")
    
    # Resolviendo el problema.
    prob.solve()
    
    # Imprimimos el estado del problema.
    print("Status: {}".format(LpStatus[prob.status]))
    variable = []
    # Imprimimos cada variable con su solución óptima.
    for v in prob.variables():
        variable.append([v.name, v.varValue])
        print("{0:} = {1:}".format(v.name, v.varValue))

        # Imprimimos el valor óptimo de la función objetivo
    print("Costo total de producción = {}".format(prob.objective.value()))

    variable.append(['Costo total de producción', prob.objective.value()])
    variable.append(['Status', LpStatus[prob.status]])
    return variable


if __name__ == '__main__':
    #obtener directorio base
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)).split('/')[:-1]
    BASE_DIR = '/'.join(BASE_DIR)
    #carga de datos
    data = pd.read_csv(BASE_DIR + '/input/punto2.csv')
    planta = data['planta'].tolist()
    productos = [1,2]
    demanda = data['demanda'].tolist()
    costo = data[['costo_p1', 'costo_p2']].values.T
    tiempo = data[['p1', 'p2']].astype(float).values
    mes = data[['demanda_p1', 'demanda_p2']].values
    capacidad = (data['capacidad'] * 60).tolist()
    produccion_minima = data['p_maxima'].tolist()
    demanda_total = [10400, 7700]
    #ejecución modelo optimización
    result=planning_produccion(productos, planta, costo, tiempo, capacidad, produccion_minima, demanda, mes, demanda_total)
    df = pd.DataFrame(result)
    df.to_csv(BASE_DIR + '/output/Resultado_punto2.csv', index=False)