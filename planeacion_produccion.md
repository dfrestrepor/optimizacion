# Planeación de la producción 1:
+ [Enunciado: ejercicio 1](https://s3.amazonaws.com/david.restrepo/optimizacion/Formulaci%C3%B3n.pdf)
+ [Datos](https://github.com/dfrestrepor/optimizacion/blob/main/input/punto1.csv)
+ [Código](https://github.com/dfrestrepor/optimizacion/blob/main/main/planeacion_produccion1.py)
+ [Resultados](https://github.com/dfrestrepor/optimizacion/blob/main/output/Resultado_punto1.csv)
## Formulación matemática: 
+ **Variable de decisión**  
<img src="https://render.githubusercontent.com/render/math?math=$X_{i,j}$" height="20">Donde Xi,j= cantidad de producto del producto **i** en la planta **j** para todo i= {1,...,10} y j = {0,1,2,3} donde cero es la planta propia.
  
+ **Función Objetivo**  
MINIMIZAR  
<img src="https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^{10}\sum_{j=0}^{3}C_{i,j}*X_{i,j}$" height="50">Donde **Ci,j** = Costo del producto i en la planta j.

+ **Restricciones**  
Restricciones de demanda:  
<img src="https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^{10}\sum_{j=0}^{3}X_{i,j}>=D_{i}$" height="50">Donde Di= demanda del producto i  
Restricción de capacidad planta propia:  
<img src="https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^{10}X_{i,0}<=P_{0}$" height="50">Donde P0= Capacidad de la planta propia  
Restricción de capacidad planta tercero:  
<img src="https://render.githubusercontent.com/render/math?math=$X_{i,j}<=P_{i,j}$" height="20">Para todo i={1,...,10} y j = {1,2,3}  
Restricción de no negatividad:  
<img src="https://render.githubusercontent.com/render/math?math=$X_{i,j}>=0$" height="20">Para todo i={1,...,10} y j = {0,1,2,3}  

## Formulación: Salida de la implementación con Python - [PuLP](https://pypi.org/project/PuLP/):
La notación es la siguiente: producto_planta_1_0, indica la cantidad de prodcuto del tipo 1 producido en la planta 0 donde cero es la planta propia y 1,2,3 las plantas de terceros.
### Función Objetivo:
```
MINIMIZE
1*producto_planta_10_0 + 10*producto_planta_10_1 + 10*producto_planta_10_2 + 10*producto_planta_10_3 + 1*producto_planta_1_0 + 49*producto_planta_1_1 + 35*producto_planta_1_2 + 7*producto_planta_1_3 + 1*producto_planta_2_0 + 35*producto_planta_2_1 + 25*producto_planta_2_2 + 5*producto_planta_2_3 + 1*producto_planta_3_0 + 7*producto_planta_3_1 + 5*producto_planta_3_2 + 1*producto_planta_3_3 + 1*producto_planta_4_0 + 63*producto_planta_4_1 + 45*producto_planta_4_2 + 9*producto_planta_4_3 + 1*producto_planta_5_0 + 7*producto_planta_5_1 + 5*producto_planta_5_2 + 1*producto_planta_5_3 + 1*producto_planta_6_0 + 14*producto_planta_6_1 + 10*producto_planta_6_2 + 2*producto_planta_6_3 + 1*producto_planta_7_0 + 35*producto_planta_7_1 + 25*producto_planta_7_2 + 5*producto_planta_7_3 + 1*producto_planta_8_0 + 7*producto_planta_8_1 + 5*producto_planta_8_2 + 1*producto_planta_8_3 + 1*producto_planta_9_0 + 7*producto_planta_9_1 + 5*producto_planta_9_2 + 1*producto_planta_9_3
```
### Restricciones de demanda
```
_C1: producto_planta_1_0 + producto_planta_1_1 + producto_planta_1_2
 + producto_planta_1_3 >= 1800
_C2: producto_planta_2_0 + producto_planta_2_1 + producto_planta_2_2
 + producto_planta_2_3 >= 2000
_C3: producto_planta_3_0 + producto_planta_3_1 + producto_planta_3_2
 + producto_planta_3_3 >= 1200
_C4: producto_planta_4_0 + producto_planta_4_1 + producto_planta_4_2
 + producto_planta_4_3 >= 1700
_C5: producto_planta_5_0 + producto_planta_5_1 + producto_planta_5_2
 + producto_planta_5_3 >= 2100
_C6: producto_planta_6_0 + producto_planta_6_1 + producto_planta_6_2
 + producto_planta_6_3 >= 1800
_C7: producto_planta_7_0 + producto_planta_7_1 + producto_planta_7_2
 + producto_planta_7_3 >= 1250
_C8: producto_planta_8_0 + producto_planta_8_1 + producto_planta_8_2
 + producto_planta_8_3 >= 1900
_C9: producto_planta_9_0 + producto_planta_9_1 + producto_planta_9_2
 + producto_planta_9_3 >= 2500
_C10: producto_planta_10_0 + producto_planta_10_1 + producto_planta_10_2
 + producto_planta_10_3 >= 3000
```
### Restricción de capacidad planta propia
```
_C11: 2.23214285714 producto_planta_10_0 + producto_planta_1_0
 + 1.20535714286 producto_planta_2_0 + 0.875 producto_planta_3_0
 + 1.25 producto_planta_4_0 + 1.65178571429 producto_planta_5_0
 + 1.51785714286 producto_planta_6_0 + 1.05357142857 producto_planta_7_0
 + 1.30357142857 producto_planta_8_0 + 1.875 producto_planta_9_0 <= 11200
 ```
 ### Restricción de capacidad planta terceros
 ```
_C12: producto_planta_1_1 <= 5000
_C13: producto_planta_2_1 <= 6026.78571429
_C14: producto_planta_3_1 <= 4375
_C15: producto_planta_4_1 <= 6250
_C16: producto_planta_5_1 <= 8258.92857143
_C17: producto_planta_6_1 <= 7589.28571429
_C18: producto_planta_7_1 <= 5267.85714286
_C19: producto_planta_8_1 <= 6517.85714286
_C20: producto_planta_9_1 <= 9375
_C21: producto_planta_10_1 <= 11160.7142857
_C22: producto_planta_1_2 <= 7000
_C23: producto_planta_2_2 <= 8437.5
_C24: producto_planta_3_2 <= 6125
_C25: producto_planta_4_2 <= 8750
_C26: producto_planta_5_2 <= 11562.5
_C27: producto_planta_6_2 <= 10625
_C28: producto_planta_7_2 <= 7375
_C29: producto_planta_8_2 <= 9125
_C30: producto_planta_9_2 <= 13125
_C31: producto_planta_10_2 <= 15625
_C32: producto_planta_1_3 <= 8000
_C33: producto_planta_2_3 <= 9642.85714286
_C34: producto_planta_3_3 <= 7000
_C35: producto_planta_4_3 <= 10000
_C36: producto_planta_5_3 <= 13214.2857143
_C37: producto_planta_6_3 <= 12142.8571429
_C38: producto_planta_7_3 <= 8428.57142857
_C39: producto_planta_8_3 <= 10428.5714286
_C40: producto_planta_9_3 <= 15000
_C41: producto_planta_10_3 <= 17857.1428571
 ```
 ### Restricciones de no negatividad
 ```
0 <= producto_planta_10_0 Integer
0 <= producto_planta_10_1 Integer
0 <= producto_planta_10_2 Integer
0 <= producto_planta_10_3 Integer
0 <= producto_planta_1_0 Integer
0 <= producto_planta_1_1 Integer
0 <= producto_planta_1_2 Integer
0 <= producto_planta_1_3 Integer
0 <= producto_planta_2_0 Integer
0 <= producto_planta_2_1 Integer
0 <= producto_planta_2_2 Integer
0 <= producto_planta_2_3 Integer
0 <= producto_planta_3_0 Integer
0 <= producto_planta_3_1 Integer
0 <= producto_planta_3_2 Integer
0 <= producto_planta_3_3 Integer
0 <= producto_planta_4_0 Integer
0 <= producto_planta_4_1 Integer
0 <= producto_planta_4_2 Integer
0 <= producto_planta_4_3 Integer
0 <= producto_planta_5_0 Integer
0 <= producto_planta_5_1 Integer
0 <= producto_planta_5_2 Integer
0 <= producto_planta_5_3 Integer
0 <= producto_planta_6_0 Integer
0 <= producto_planta_6_1 Integer
0 <= producto_planta_6_2 Integer
0 <= producto_planta_6_3 Integer
0 <= producto_planta_7_0 Integer
0 <= producto_planta_7_1 Integer
0 <= producto_planta_7_2 Integer
0 <= producto_planta_7_3 Integer
0 <= producto_planta_8_0 Integer
0 <= producto_planta_8_1 Integer
0 <= producto_planta_8_2 Integer
0 <= producto_planta_8_3 Integer
0 <= producto_planta_9_0 Integer
0 <= producto_planta_9_1 Integer
0 <= producto_planta_9_2 Integer
0 <= producto_planta_9_3 Integer
```
### Resultados
```
Result - Optimal solution found
Objective value:                31854.00000000
Enumerated nodes:               0
Total iterations:               0
Time (CPU seconds):             0.00
Time (Wallclock seconds):       0.00
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00
Status: Optimal
producto_planta_10_0 = 3000.0
producto_planta_10_1 = 0.0
producto_planta_10_2 = 0.0
producto_planta_10_3 = 0.0
producto_planta_1_0 = 1800.0
producto_planta_1_1 = 0.0
producto_planta_1_2 = 0.0
producto_planta_1_3 = 0.0
producto_planta_2_0 = 0.0
producto_planta_2_1 = 0.0
producto_planta_2_2 = 0.0
producto_planta_2_3 = 2000.0
producto_planta_3_0 = 0.0
producto_planta_3_1 = 0.0
producto_planta_3_2 = 0.0
producto_planta_3_3 = 1200.0
producto_planta_4_0 = 1700.0
producto_planta_4_1 = 0.0
producto_planta_4_2 = 0.0
producto_planta_4_3 = 0.0
producto_planta_5_0 = 0.0
producto_planta_5_1 = 0.0
producto_planta_5_2 = 0.0
producto_planta_5_3 = 2100.0
producto_planta_6_0 = 0.0
producto_planta_6_1 = 0.0
producto_planta_6_2 = 0.0
producto_planta_6_3 = 1800.0
producto_planta_7_0 = 549.0
producto_planta_7_1 = 0.0
producto_planta_7_2 = 0.0
producto_planta_7_3 = 701.0
producto_planta_8_0 = 0.0
producto_planta_8_1 = 0.0
producto_planta_8_2 = 0.0
producto_planta_8_3 = 1900.0
producto_planta_9_0 = 0.0
producto_planta_9_1 = 0.0
producto_planta_9_2 = 0.0
producto_planta_9_3 = 2500.0
Costo total de producción = 31854.0
```
### Conclusiones
+ Se llega a una solución óptima
+ El costo total de mínimo producción es de: 31.854.0
+ Los productos deben ser producidos entre las plantas 1 y 3 en las cantidades determinadas por la solución óptima
