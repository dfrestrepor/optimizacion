\* Planeación_producción_2 *\
Minimize
OBJ: 11000 producto_planta_1_1_1 + 11000 producto_planta_1_1_2
 + 11000 producto_planta_1_1_3 + 11000 producto_planta_1_1_4
 + 11400 producto_planta_1_2_1 + 11400 producto_planta_1_2_2
 + 11400 producto_planta_1_2_3 + 11400 producto_planta_1_2_4
 + 9800 producto_planta_1_3_1 + 9800 producto_planta_1_3_2
 + 9800 producto_planta_1_3_3 + 9800 producto_planta_1_3_4
 + 9800 producto_planta_1_4_1 + 9800 producto_planta_1_4_2
 + 9800 producto_planta_1_4_3 + 9800 producto_planta_1_4_4
 + 11700 producto_planta_2_1_1 + 11700 producto_planta_2_1_2
 + 11700 producto_planta_2_1_3 + 11700 producto_planta_2_1_4
 + 12200 producto_planta_2_2_1 + 12200 producto_planta_2_2_2
 + 12200 producto_planta_2_2_3 + 12200 producto_planta_2_2_4
 + 13400 producto_planta_2_3_1 + 13400 producto_planta_2_3_2
 + 13400 producto_planta_2_3_3 + 13400 producto_planta_2_3_4
 + 13400 producto_planta_2_4_1 + 13400 producto_planta_2_4_2
 + 13400 producto_planta_2_4_3 + 13400 producto_planta_2_4_4
Subject To
_C1: producto_planta_1_1_1 + producto_planta_2_1_1 >= 500
_C10: producto_planta_1_2_3 + producto_planta_2_2_3 >= 800
_C11: producto_planta_1_3_3 + producto_planta_2_3_3 >= 700
_C12: producto_planta_1_4_3 + producto_planta_2_4_3 >= 600
_C13: producto_planta_1_1_4 + producto_planta_2_1_4 >= 500
_C14: producto_planta_1_2_4 + producto_planta_2_2_4 >= 800
_C15: producto_planta_1_3_4 + producto_planta_2_3_4 >= 700
_C16: producto_planta_1_4_4 + producto_planta_2_4_4 >= 600
_C17: producto_planta_2_1_1 + producto_planta_2_2_1 + producto_planta_2_3_1
 + producto_planta_2_4_1 >= 2200
_C18: producto_planta_2_1_2 + producto_planta_2_2_2 + producto_planta_2_3_2
 + producto_planta_2_4_2 >= 1800
_C19: producto_planta_2_1_3 + producto_planta_2_2_3 + producto_planta_2_3_3
 + producto_planta_2_4_3 >= 1700
_C2: producto_planta_1_2_1 + producto_planta_2_2_1 >= 800
_C20: producto_planta_2_1_4 + producto_planta_2_2_4 + producto_planta_2_3_4
 + producto_planta_2_4_4 >= 2000
_C21: producto_planta_1_1_1 + producto_planta_1_2_1 + producto_planta_1_3_1
 + producto_planta_1_4_1 >= 2500
_C22: producto_planta_1_1_2 + producto_planta_1_2_2 + producto_planta_1_3_2
 + producto_planta_1_4_2 >= 3100
_C23: producto_planta_1_1_3 + producto_planta_1_2_3 + producto_planta_1_3_3
 + producto_planta_1_4_3 >= 2800
_C24: producto_planta_1_1_4 + producto_planta_1_2_4 + producto_planta_1_3_4
 + producto_planta_1_4_4 >= 2000
_C25: 0.9 producto_planta_1_1_1 + 0.6 producto_planta_2_1_1 <= 115200
_C26: 1.1 producto_planta_1_2_1 + 0.8 producto_planta_2_2_1 <= 172800
_C27: 1.2 producto_planta_1_3_1 + 0.9 producto_planta_2_3_1 <= 150000
_C28: 0.9 producto_planta_1_4_1 + 0.8 producto_planta_2_4_1 <= 138000
_C29: 0.9 producto_planta_1_1_2 + 0.6 producto_planta_2_1_2 <= 115200
_C3: producto_planta_1_3_1 + producto_planta_2_3_1 >= 700
_C30: 1.1 producto_planta_1_2_2 + 0.8 producto_planta_2_2_2 <= 172800
_C31: 1.2 producto_planta_1_3_2 + 0.9 producto_planta_2_3_2 <= 150000
_C32: 0.9 producto_planta_1_4_2 + 0.8 producto_planta_2_4_2 <= 138000
_C33: 0.9 producto_planta_1_1_3 + 0.6 producto_planta_2_1_3 <= 115200
_C34: 1.1 producto_planta_1_2_3 + 0.8 producto_planta_2_2_3 <= 172800
_C35: 1.2 producto_planta_1_3_3 + 0.9 producto_planta_2_3_3 <= 150000
_C36: 0.9 producto_planta_1_4_3 + 0.8 producto_planta_2_4_3 <= 138000
_C37: 0.9 producto_planta_1_1_4 + 0.6 producto_planta_2_1_4 <= 115200
_C38: 1.1 producto_planta_1_2_4 + 0.8 producto_planta_2_2_4 <= 172800
_C39: 1.2 producto_planta_1_3_4 + 0.9 producto_planta_2_3_4 <= 150000
_C4: producto_planta_1_4_1 + producto_planta_2_4_1 >= 600
_C40: 0.9 producto_planta_1_4_4 + 0.8 producto_planta_2_4_4 <= 138000
_C41: producto_planta_1_1_1 + producto_planta_1_1_2 + producto_planta_1_1_3
 + producto_planta_1_1_4 + producto_planta_1_2_1 + producto_planta_1_2_2
 + producto_planta_1_2_3 + producto_planta_1_2_4 + producto_planta_1_3_1
 + producto_planta_1_3_2 + producto_planta_1_3_3 + producto_planta_1_3_4
 + producto_planta_1_4_1 + producto_planta_1_4_2 + producto_planta_1_4_3
 + producto_planta_1_4_4 <= 10400
_C42: producto_planta_2_1_1 + producto_planta_2_1_2 + producto_planta_2_1_3
 + producto_planta_2_1_4 + producto_planta_2_2_1 + producto_planta_2_2_2
 + producto_planta_2_2_3 + producto_planta_2_2_4 + producto_planta_2_3_1
 + producto_planta_2_3_2 + producto_planta_2_3_3 + producto_planta_2_3_4
 + producto_planta_2_4_1 + producto_planta_2_4_2 + producto_planta_2_4_3
 + producto_planta_2_4_4 <= 7700
_C5: producto_planta_1_1_2 + producto_planta_2_1_2 >= 500
_C6: producto_planta_1_2_2 + producto_planta_2_2_2 >= 800
_C7: producto_planta_1_3_2 + producto_planta_2_3_2 >= 700
_C8: producto_planta_1_4_2 + producto_planta_2_4_2 >= 600
_C9: producto_planta_1_1_3 + producto_planta_2_1_3 >= 500
Bounds
0 <= producto_planta_1_1_1
0 <= producto_planta_1_1_2
0 <= producto_planta_1_1_3
0 <= producto_planta_1_1_4
0 <= producto_planta_1_2_1
0 <= producto_planta_1_2_2
0 <= producto_planta_1_2_3
0 <= producto_planta_1_2_4
0 <= producto_planta_1_3_1
0 <= producto_planta_1_3_2
0 <= producto_planta_1_3_3
0 <= producto_planta_1_3_4
0 <= producto_planta_1_4_1
0 <= producto_planta_1_4_2
0 <= producto_planta_1_4_3
0 <= producto_planta_1_4_4
0 <= producto_planta_2_1_1
0 <= producto_planta_2_1_2
0 <= producto_planta_2_1_3
0 <= producto_planta_2_1_4
0 <= producto_planta_2_2_1
0 <= producto_planta_2_2_2
0 <= producto_planta_2_2_3
0 <= producto_planta_2_2_4
0 <= producto_planta_2_3_1
0 <= producto_planta_2_3_2
0 <= producto_planta_2_3_3
0 <= producto_planta_2_3_4
0 <= producto_planta_2_4_1
0 <= producto_planta_2_4_2
0 <= producto_planta_2_4_3
0 <= producto_planta_2_4_4
Generals
producto_planta_1_1_1
producto_planta_1_1_2
producto_planta_1_1_3
producto_planta_1_1_4
producto_planta_1_2_1
producto_planta_1_2_2
producto_planta_1_2_3
producto_planta_1_2_4
producto_planta_1_3_1
producto_planta_1_3_2
producto_planta_1_3_3
producto_planta_1_3_4
producto_planta_1_4_1
producto_planta_1_4_2
producto_planta_1_4_3
producto_planta_1_4_4
producto_planta_2_1_1
producto_planta_2_1_2
producto_planta_2_1_3
producto_planta_2_1_4
producto_planta_2_2_1
producto_planta_2_2_2
producto_planta_2_2_3
producto_planta_2_2_4
producto_planta_2_3_1
producto_planta_2_3_2
producto_planta_2_3_3
producto_planta_2_3_4
producto_planta_2_4_1
producto_planta_2_4_2
producto_planta_2_4_3
producto_planta_2_4_4
End
