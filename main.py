import pandas as file_reader
import seaborn as graph
import matplotlib.pyplot as plot
from sympy import pprint, symbols, Matrix

# Apply the default theme
graph.set_theme()

# Read an excel file
excel_data = file_reader.read_excel('database.xlsx', sheet_name='Hoja1')
print('---------------- Excel data ----------------')
print(excel_data)

# Normal equations
sym_n, sym_a, sym_b, sym_sigma_x, sym_sigma_y, sym_sigma_xy, sym_sigma_xx, sym_sigma_yy = symbols(
    'n a b sigma_x sigma_y sigma_xy sigma_xx sigma_yy')

A = Matrix([[sym_n, sym_sigma_x], [sym_sigma_x, sym_sigma_xx]])
R = Matrix([[sym_sigma_y], [sym_sigma_xy]])
V = Matrix([[sym_a], [sym_b]])

print(' -------------- Normal equations (Matrix Form) -----------------')
pprint(A, use_unicode=True)
pprint(V, use_unicode=True)
print('=')
pprint(R, use_unicode=True)

#  ------------------- Case for pepsi -------------------
ventas_pepsi = excel_data['Ventas de Pepsi']
precios_pepsi = excel_data['Precio de Pepsi']

x1 = precios_pepsi
y1 = ventas_pepsi
x1_cuadrado = x1 * x1
y1_cuadrado = y1 * y1
x1_y1 = x1 * y1
sigma_x1 = x1.sum()
sigma_y1 = y1.sum()
sigma_x1_cuadrado = x1_cuadrado.sum()
sigma_y1_cuadrado = y1_cuadrado.sum()
sigma_x1_y1 = x1_y1.sum()

n = len(x1)

sxx = sigma_x1_cuadrado - (sigma_x1 * sigma_x1)/n

syy = sigma_y1_cuadrado - (sigma_y1 * sigma_y1)/n

sxy = sigma_x1_y1 - (sigma_x1 * sigma_y1)/n

r = sxy / ((sxx * syy)**(1/2))


print('\n --------------------- Solution (Pepsi) ---------------------')
pprint(V, use_unicode=True)
print('=')
Res = A.inv() * R
pprint(Res, use_unicode=True)
print('=')

A_eval = A.subs([(sym_n, n), (sym_sigma_x, sigma_x1),
                 (sym_sigma_xx, sigma_x1_cuadrado)])
R_eval = R.subs([(sym_sigma_y, sigma_y1), (sym_sigma_xy, sigma_x1_y1)])
Res_eval = A_eval.inv() * R_eval
pprint(Res_eval, use_unicode=True)

a1 = Res_eval[0]
b1 = Res_eval[1]
print("\nSxx = ", sxx, "\nSyy = ", syy, "\nSxy = ", sxy)
print("\nEl coeficiente de correlación es: ", r)
print("\nLa ecuación de la recta es: y = ", a1, " + ", b1, "x")

# ----------------------- Case for coca-cola -----------------------
precios_coca = excel_data['Precio de Coca-Cola']
ventas_coca = excel_data['Ventas de Coca-Cola']

x2 = precios_coca
y2 = ventas_coca
x2_cuadrado = x2 * x2
y2_cuadrado = y2 * y2
x2_y2 = x2 * y2
sigma_x2 = x2.sum()
sigma_y2 = y2.sum()
sigma_x2_cuadrado = x2_cuadrado.sum()
sigma_y2_cuadrado = y2_cuadrado.sum()
sigma_x2_y2 = x2_y2.sum()

n2 = len(x2)

sxx2 = sigma_x2_cuadrado - (sigma_x2 * sigma_x2)/n2

syy2 = sigma_y2_cuadrado - (sigma_y2 * sigma_y2)/n2

sxy2 = sigma_x2_y2 - (sigma_x2 * sigma_y2)/n2

r2 = sxy2 / ((sxx2 * syy2)**(1/2))

print('\n --------------------- Solution (Coca-Cola) ---------------------')
pprint(V, use_unicode=True)
print('=')
Res = A.inv() * R
pprint(Res, use_unicode=True)
print('=')

A_eval = A.subs([(sym_n, n2), (sym_sigma_x, sigma_x2),
                 (sym_sigma_xx, sigma_x2_cuadrado)])
R_eval = R.subs([(sym_sigma_y, sigma_y2), (sym_sigma_xy, sigma_x2_y2)])
Res_eval = A_eval.inv() * R_eval
pprint(Res_eval, use_unicode=True)

a2 = Res_eval[0]
b2 = Res_eval[1]
print("\nSxx = ", sxx2, "\nSyy = ", syy2, "\nSxy = ", sxy2)
print("\nEl coeficiente de correlación es: ", r2)
print("\nLa ecuación de la recta es: y = ", a2, " + ", b2, "x")

# Create a visualization
# Primer grafico
graph.lmplot(
    x="Precio de Pepsi",
    y="Ventas de Pepsi",
    data=excel_data,
    palette="muted",
    height=5,
    scatter_kws={"s": 50, "alpha": 1},

)

# Segundo grafico
graph.lmplot(
    x="Precio de Coca-Cola",
    y="Ventas de Coca-Cola",
    data=excel_data,
    palette="muted",
    height=5,
    scatter_kws={"s": 50, "alpha": 1},
)

# Mostrar los subgráficos
# plot.show()
