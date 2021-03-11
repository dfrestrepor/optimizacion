# Optimización
Repositiorio de optimización LP con python
## Instalación
pip install pulp
sudo apt-get install glpk-utils
sudo apt-get insall coinor-cbc
## Formulación problema 1 (en roceso de edición)
### Función Objetivo: con costo de la planta propia igual a 5
MINIMIZE

5*producto_planta_10_0 + 10*producto_planta_10_1 + 10*producto_planta_10_2 + 10*producto_planta_10_3 + 5*producto_planta_1_0 + 49*producto_planta_1_1 + 35*producto_planta_1_2 + 35*producto_planta_1_3 + 5*producto_planta_2_0 + 35*producto_planta_2_1 + 25*producto_planta_2_2 + 25*producto_planta_2_3 + 5*producto_planta_3_0 + 7*producto_planta_3_1 + 5*producto_planta_3_2 + 5*producto_planta_3_3 + 5*producto_planta_4_0 + 63*producto_planta_4_1 + 45*producto_planta_4_2 + 45*producto_planta_4_3 + 5*producto_planta_5_0 + 7*producto_planta_5_1 + 5*producto_planta_5_2 + 5*producto_planta_5_3 + 5*producto_planta_6_0 + 14*producto_planta_6_1 + 10*producto_planta_6_2 + 10*producto_planta_6_3 + 5*producto_planta_7_0 + 35*producto_planta_7_1 + 25*producto_planta_7_2 + 25*producto_planta_7_3 + 5*producto_planta_8_0 + 7*producto_planta_8_1 + 5*producto_planta_8_2 + 5*producto_planta_8_3 + 5*producto_planta_9_0 + 7*producto_planta_9_1 + 5*producto_planta_9_2 + 5*producto_planta_9_3 + 0

### Restricciones  
+ _C1: producto_planta_1_0 + producto_planta_1_1 + producto_planta_1_2 + producto_planta_1_3 >= 1800  
+ _C2: producto_planta_2_0 + producto_planta_2_1 + producto_planta_2_2 + producto_planta_2_3 >= 2000  
+ _C3: producto_planta_3_0 + producto_planta_3_1 + producto_planta_3_2 + producto_planta_3_3 >= 1200  
+ _C4: producto_planta_4_0 + producto_planta_4_1 + producto_planta_4_2 + producto_planta_4_3 >= 1700  
+ _C5: producto_planta_5_0 + producto_planta_5_1 + producto_planta_5_2 + producto_planta_5_3 >= 2100  
+ _C6: producto_planta_6_0 + producto_planta_6_1 + producto_planta_6_2 + producto_planta_6_3 >= 1800  
+ _C7: producto_planta_7_0 + producto_planta_7_1 + producto_planta_7_2 + producto_planta_7_3 >= 1250  
+ _C8: producto_planta_8_0 + producto_planta_8_1 + producto_planta_8_2 + producto_planta_8_3 >= 1900  
+ _C9: producto_planta_9_0 + producto_planta_9_1 + producto_planta_9_2 + producto_planta_9_3 >= 2500  
+ _C10: producto_planta_10_0 + producto_planta_10_1 + producto_planta_10_2 + producto_planta_10_3 >= 3000  
 
_C11: producto_planta_1_0 <= 11200
_C12: producto_planta_2_0 <= 13500
_C13: producto_planta_3_0 <= 9800
_C14: producto_planta_4_0 <= 14000
_C15: producto_planta_5_0 <= 18500
_C16: producto_planta_6_0 <= 17000
_C17: producto_planta_7_0 <= 11800
_C18: producto_planta_8_0 <= 14600
_C19: producto_planta_9_0 <= 21000
_C20: producto_planta_10_0 <= 25000
_C21: producto_planta_1_1 <= 5000
_C22: producto_planta_2_1 <= 6026.78571429
_C23: producto_planta_3_1 <= 4375
_C24: producto_planta_4_1 <= 6250
_C25: producto_planta_5_1 <= 8258.92857143
_C26: producto_planta_6_1 <= 7589.28571429
_C27: producto_planta_7_1 <= 5267.85714286
_C28: producto_planta_8_1 <= 6517.85714286
_C29: producto_planta_9_1 <= 9375
_C30: producto_planta_10_1 <= 11160.7142857
_C31: producto_planta_1_2 <= 7000
_C32: producto_planta_2_2 <= 8437.5
_C33: producto_planta_3_2 <= 6125
_C34: producto_planta_4_2 <= 8750
_C35: producto_planta_5_2 <= 11562.5
_C36: producto_planta_6_2 <= 10625
_C37: producto_planta_7_2 <= 7375
_C38: producto_planta_8_2 <= 9125
_C39: producto_planta_9_2 <= 13125
_C40: producto_planta_10_2 <= 15625
_C41: producto_planta_1_3 <= 8000
_C42: producto_planta_2_3 <= 9642.85714286
_C43: producto_planta_3_3 <= 7000
_C44: producto_planta_4_3 <= 10000
_C45: producto_planta_5_3 <= 13214.2857143
_C46: producto_planta_6_3 <= 12142.8571429
_C47: producto_planta_7_3 <= 8428.57142857
_C48: producto_planta_8_3 <= 10428.5714286
_C49: producto_planta_9_3 <= 15000
_C50: producto_planta_10_3 <= 17857.1428571

VARIABLES
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
