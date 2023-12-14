import seaborn as sns
import pandas as file_reader
import seaborn as graph
import matplotlib.pyplot as plot

# Apply the default theme
sns.set_theme()

# Read an excel file
excel_data = file_reader.read_excel('database.xlsx', sheet_name='Hoja1')
# This way we can sort the data by a column
# excel_data.sort_values(by=columnas[0], inplace=True)


print(excel_data)

ventas_pepsi = excel_data['Ventas de Pepsi']
precios_pepsi = excel_data['Precio de Pepsi']

x1 = precios_pepsi
y1 = ventas_pepsi
x1_cuadrado = x1 * x1
y1_cuadrado = y1 * y1
x1_y1 = x1 * y1

precios_coca = excel_data['Precio de Coca-Cola']
ventas_coca = excel_data['Ventas de Coca-Cola']

x2 = precios_coca
y2 = ventas_coca
x2_cuadrado = x2 * x2
y2_cuadrado = y2 * y2
x2_y2 = x2 * y2

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
