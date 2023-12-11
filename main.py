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

# Create a visualization
graph.histplot(
    data=excel_data['Ventas de Pepsi'],
    bins=5,
    label="Ventas de Pepsi",
    color="skyblue",
)
graph.histplot(
    data=excel_data['Ventas de Coca-Cola'],
    bins=5,
    label="Ventas de Coca-Cola",
    color="salmon",
)

plot.title('Histograma de Ventas Pepsi y Coca-Cola')
plot.xlabel('Cantidad de Ventas')
plot.ylabel('Frecuencia')
plot.legend()  # Mostrar leyenda

# This run the visualization on the screen
plot.show()
