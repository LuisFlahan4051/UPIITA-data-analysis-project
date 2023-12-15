import pandas as file_reader
import seaborn as graph
import matplotlib.pyplot as plot
from sympy import pprint, symbols, Matrix
from scipy.stats import norm, t

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

media_x = sigma_x1 / n
media_y = sigma_y1 / n
desviacion_estandar_x = (sxx / (n-1))**(1/2)

probabilidad_acumulativa = 0.95
alfa = 1 - probabilidad_acumulativa

z_sub_alfa = -norm.ppf(alfa)
z_sub_alfa_medios = -norm.ppf(alfa/2)

grados_libertad = n - 1
t_sub_alfa_g1 = -t.ppf(alfa, grados_libertad)
t_sub_alfa_medios_g1 = -t.ppf(alfa/2, grados_libertad)
t_sub_alfa_g2 = -t.ppf(alfa, grados_libertad-1)
t_sub_alfa_medios_g2 = -t.ppf(alfa/2, grados_libertad-1)

# Caso n>30
intervalo_confianza_media_inf = media_x - \
    (desviacion_estandar_x * z_sub_alfa_medios)/((n)**(1/2))
intervalo_confianza_media_sup = media_x + \
    (desviacion_estandar_x * z_sub_alfa_medios)/((n)**(1/2))

# Caso n<30
intervalo_confianza_media_inf_t = media_x - \
    (desviacion_estandar_x * t_sub_alfa_medios_g1)/((n)**(1/2))
intervalo_confianza_media_sup_t = media_x + \
    (desviacion_estandar_x * t_sub_alfa_medios_g1)/((n)**(1/2))

ssres = syy - (sxy**2)/sxx
sst = syy
desviacion_lineal = (ssres/(n-2))**(1/2)
b1 = sxy/sxx
intervalo_confianza_B_inf_t = b1 - \
    (t_sub_alfa_medios_g2 * desviacion_lineal)/(sxx**(1/2))
intervalo_confianza_B_sup_t = b1 + \
    (t_sub_alfa_medios_g2 * desviacion_lineal)/(sxx**(1/2))

x = xp = 2
b0 = media_y - b1 * media_x
y_gorro = b0 + b1 * xp
intervalo_prediccion_inf = y_gorro - t_sub_alfa_medios_g2 * \
    desviacion_lineal*(((1/n)+((xp - media_x)**2)/sxx)**(1/2))
intervalo_prediccion_sup = y_gorro + t_sub_alfa_medios_g2 * \
    desviacion_lineal*(((1/n)+((xp - media_x)**2)/sxx)**(1/2))

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

print("\nLa ecuación de la recta es: y = ", a1, " + ", b1, "x")
print("\nEl coeficiente de correlación es: ", r)

print("\n\nSxx = ", sxx, "\nSyy = ", syy, "\nSxy = ", sxy)
print("La media de x es: ", media_x)
print("La media de y es: ", media_y)
print("La desviación estándar de x es: ", desviacion_estandar_x)
print("SST = ", sst, "\nSSres = ",
      ssres, "\nDesviación respecto a la pendiente = ", desviacion_lineal, "\nb1 = ", b1, "\nb0 = ", b0)


print("\nProbabilidad acumulativa: ", probabilidad_acumulativa)
print("Alfa: ", alfa)
print("El valor Zsub_alfa: ", z_sub_alfa)
print("El valor Zsub_alfa/2: ", z_sub_alfa_medios)
print("El valor Tsub_alfa en (GDL = n-1): ", t_sub_alfa_g1)
print("El valor Tsub_alfa/2 en (GDL = n-1): ", t_sub_alfa_medios_g1)
print("El valor Tsub_alfa en (GDL = n-2): ", t_sub_alfa_g2)
print("El valor Tsub_alfa en (GDL = n-2): ", t_sub_alfa_medios_g2)
print("\nEl intervalo de confianza para la media (n>30) es: (",
      intervalo_confianza_media_inf, ", ", intervalo_confianza_media_sup, ")")
print("El intervalo de confianza para la media (n<30) es: (",
      intervalo_confianza_media_inf_t, ", ", intervalo_confianza_media_sup_t, ")")
print("El intervalo de confianza para B es: (",
      intervalo_confianza_B_inf_t, ", ", intervalo_confianza_B_sup_t, ")")
print("El intervalo de predicción es: (",
      intervalo_prediccion_inf, ", ", intervalo_prediccion_sup, ")")


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

media_x2 = sigma_x2 / n2
media_y2 = sigma_y2 / n2
desviacion_estandar_x2 = (sxx2 / (n2-1))**(1/2)

# Caso n>30
intervalo_confianza_media_inf2 = media_x2 - \
    (desviacion_estandar_x2 * z_sub_alfa_medios)/((n2)**(1/2))
intervalo_confianza_media_sup2 = media_x2 + \
    (desviacion_estandar_x2 * z_sub_alfa_medios)/((n2)**(1/2))

# Caso n<30
intervalo_confianza_media_inf_t2 = media_x2 - \
    (desviacion_estandar_x2 * t_sub_alfa_medios_g1)/((n2)**(1/2))
intervalo_confianza_media_sup_t2 = media_x2 + \
    (desviacion_estandar_x2 * t_sub_alfa_medios_g1)/((n2)**(1/2))

ssres2 = syy2 - (sxy2**2)/sxx2
sst2 = syy2
desviacion_lineal2 = (ssres2/(n2-2))**(1/2)
b1_2 = sxy2/sxx2
intervalo_confianza_B_inf_t2 = b1_2 - \
    (t_sub_alfa_medios_g2 * desviacion_lineal2)/(sxx2**(1/2))
intervalo_confianza_B_sup_t2 = b1_2 + \
    (t_sub_alfa_medios_g2 * desviacion_lineal2)/(sxx2**(1/2))

x2 = xp2 = 2
b0_2 = media_y2 - b1_2 * media_x2
y_gorro2 = b0_2 + b1_2 * xp2
intervalo_prediccion_inf2 = y_gorro2 - t_sub_alfa_medios_g2 * \
    desviacion_lineal2*(((1/n2)+((xp2 - media_x2)**2)/sxx2)**(1/2))
intervalo_prediccion_sup2 = y_gorro2 + t_sub_alfa_medios_g2 * \
    desviacion_lineal2*(((1/n2)+((xp2 - media_x2)**2)/sxx2)**(1/2))

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

print("\nLa ecuación de la recta es: y = ", a2, " + ", b2, "x")
print("\nEl coeficiente de correlación es: ", r2)

print("\n\nSxx = ", sxx2, "\nSyy = ", syy2, "\nSxy = ", sxy2)
print("La media de x es: ", media_x2)
print("La media de y es: ", media_y2)
print("La desviación estándar de x es: ", desviacion_estandar_x2)
print("SST = ", sst2, "\nSSres = ",
      ssres2, "\nDesviación respecto a la pendiente = ", desviacion_lineal2, "\nb1 = ", b1_2, "\nb0 = ", b0_2)


print("\nProbabilidad acumulativa: ", probabilidad_acumulativa)
print("Alfa: ", alfa)
print("El valor Zsub_alfa: ", z_sub_alfa)
print("El valor Zsub_alfa/2: ", z_sub_alfa_medios)
print("El valor Tsub_alfa en (GDL = n-1): ", t_sub_alfa_g1)
print("El valor Tsub_alfa/2 en (GDL = n-1): ", t_sub_alfa_medios_g1)
print("El valor Tsub_alfa en (GDL = n-2): ", t_sub_alfa_g2)
print("El valor Tsub_alfa en (GDL = n-2): ", t_sub_alfa_medios_g2)

print("\nEl intervalo de confianza para la media (n>30) es: (",
      intervalo_confianza_media_inf2, ", ", intervalo_confianza_media_sup2, ")")
print("El intervalo de confianza para la media (n<30) es: (",
      intervalo_confianza_media_inf_t2, ", ", intervalo_confianza_media_sup_t2, ")")
print("El intervalo de confianza para B es: (",
      intervalo_confianza_B_inf_t2, ", ", intervalo_confianza_B_sup_t2, ")")
print("El intervalo de predicción es: (",
      intervalo_prediccion_inf2, ", ", intervalo_prediccion_sup2, ")")

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
plot.show()
