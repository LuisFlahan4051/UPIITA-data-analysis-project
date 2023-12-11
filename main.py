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

excel_data = excel_data.sort_values(by='Precio de Pepsi', ascending=True)
precios_pepsi = excel_data['Precio de Pepsi']
ventas_pepsi = excel_data['Ventas de Pepsi']

excel_data = excel_data.sort_values(by='Precio de Coca-Cola', ascending=True)
precios_coca = excel_data['Precio de Coca-Cola']
ventas_coca = excel_data['Ventas de Coca-Cola']

# Create a visualization

fig, axes = plot.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Primer subgráfico
graph.barplot(
    x=precios_pepsi,
    y=ventas_pepsi,
    label="Pepsi",
    color="skyblue",
    ax=axes[0],
)
axes[0].set_title('Subgráfico 1')

# Segundo subgráfico
graph.barplot(
    x=precios_coca,
    y=ventas_coca,
    label="Coca-Cola",
    color="salmon",
    ax=axes[1],
)
axes[1].set_title('Subgráfico 2')

# Ajustes de diseño (opcional)
plot.tight_layout()

# Mostrar los subgráficos
plot.show()
