import pandas as pd
import datashader as ds
from datashader import transfer_functions as tf
from datashader.utils import export_image
import numpy as np

# Cargar el DataFrame desde un archivo CSV
df = pd.read_csv('Universo/plotDataSet.csv')

# Convertir las columnas a valores numéricos si no lo son
df['id'] = pd.to_numeric(df['id'], errors='coerce')
df['OnesNumber'] = pd.to_numeric(df['OnesNumber'], errors='coerce')
df['ZeroesNumber'] = pd.to_numeric(df['ZeroesNumber'], errors='coerce')

# Crear las imágenes individuales
canvas = ds.Canvas(plot_width=800, plot_height=400)

# Unos (en azul)
agg_ones = canvas.points(df, 'id', 'OnesNumber')
img_ones = tf.shade(agg_ones, cmap=["blue"], how='eq_hist')
export_image(img_ones, filename='ones_image')

# Ceros (en rojo)
agg_zeros = canvas.points(df, 'id', 'ZeroesNumber')
img_zeros = tf.shade(agg_zeros, cmap=["red"], how='eq_hist')
export_image(img_zeros, filename='zeros_image')

# Crear imágenes logarítmicas
df['log_OnesNumber'] = np.log10(df['OnesNumber'] + 1)  # Evitar log(0)
df['log_ZeroesNumber'] = np.log10(df['ZeroesNumber'] + 1)

# Unos logarítmicos (en azul)
agg_log_ones = canvas.points(df, 'id', 'log_OnesNumber')
img_log_ones = tf.shade(agg_log_ones, cmap=["blue"], how='eq_hist')
export_image(img_log_ones, filename='log_ones_image')

# Ceros logarítmicos (en rojo)
agg_log_zeros = canvas.points(df, 'id', 'log_ZeroesNumber')
img_log_zeros = tf.shade(agg_log_zeros, cmap=["red"], how='eq_hist')
export_image(img_log_zeros, filename='log_zeros_image')

print("Imágenes generadas.")
