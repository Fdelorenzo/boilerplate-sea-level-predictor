import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importación de los datos oficiales desde el archivo CSV
    df = pd.read_csv("epa-sea-level.csv")

    # Extraemos las columnas principales para el gráfico base
    x_data = df["Year"]
    y_data = df["CSIRO Adjusted Sea Level"]

    # 2. Configuración del diagrama de dispersión inicial
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x_data, y_data, color="blue", s=15, label="Data")

    # 3. Primera línea de mejor ajuste (Datos completos desde 1880 hasta 2050)
    regress_all = linregress(x_data, y_data)
    
    # Generamos la secuencia de años completa para la proyección
    years_all = pd.Series([year for year in range(1880, 2051)])
    fit_all = regress_all.slope * years_all + regress_all.intercept
    ax.plot(years_all, fit_all, color="red", linestyle="--", label="Fit: 1880-2050")

    # 4. Segunda línea de mejor ajuste (Datos modernos desde el año 2000 hasta 2050)
    df_modern = df[df["Year"] >= 2000]
    x_modern = df_modern["Year"]
    y_modern = df_modern["CSIRO Adjusted Sea Level"]
    
    regress_modern = linregress(x_modern, y_modern)
    
    # Generamos la secuencia de años para la tendencia reciente
    years_modern = pd.Series([year for year in range(2000, 2051)])
    fit_modern = regress_modern.slope * years_modern + regress_modern.intercept
    ax.plot(years_modern, fit_modern, color="green", linestyle="-.", label="Fit: 2000-2050")

    # 5. Configuración estricta de etiquetas y título requeridos usando el objeto ax
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_xlim(1870, 2060)
    ax.legend()

    # Guardar la imagen y retornar los ejes para que test_module.py lea los títulos correctamente
    fig.savefig("sea_level_plot.png")
    return plt.gca()
