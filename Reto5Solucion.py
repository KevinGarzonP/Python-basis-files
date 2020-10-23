# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 08:54:19 2020

@author: KevinProg
"""

#Para usar los DataFrames
import pandas as pd

#Función para hallar el promedio por continente de la razón entre el total de contagiados por covid y el total de camas disponibles
def caso_who(ruta_archivo_csv: str)-> dict:
    #Validación de la extensión del archivo csv
    if ruta_archivo_csv[-3:] == "csv":
        #Validación de la lectura del archivo
        try:
            df = pd.read_csv(ruta_archivo_csv)
        except:
            return("Error al leer el archivo de datos.")
        #Eliminación de las columnas innecesarias de la matrix
        df.drop(["iso_code", "total_deaths", "new_deaths", "new_deaths_smoothed", "new_cases_smoothed_per_million", "total_deaths_per_million", "new_deaths_per_million", "new_deaths_smoothed_per_million", "new_tests", "total_tests", "total_tests_per_thousand", "new_tests_per_thousand", "new_tests_smoothed", "new_tests_smoothed_per_thousand", "tests_per_case", "positive_rate", "tests_units", "stringency_index", "population_density", "median_age", "aged_65_older", "aged_70_older", "gdp_per_capita", "extreme_poverty", "cardiovasc_death_rate", "diabetes_prevalence", "female_smokers", "male_smokers", "handwashing_facilities", "life_expectancy", "human_development_index"], axis=1, inplace = True)
        #Formula de la razón entre contagiados y camas por país
        df["razon"] = (df["total_cases_per_million"] * df["population"]/1000000) / (df["hospital_beds_per_thousand"] * df["population"]/1000)
        #Cambio del formato de fecha (que está mal en el archivo csv)
        df["date"] = pd.to_datetime(df["date"], infer_datetime_format = True)
        #Reorganización de la matrix en promedio por continente
        respuesta = df.groupby(["date", "continent"])["razon"].mean().unstack()
        #Conversión de la matriz (DataFrame) a diccionario como pide el requerimiento
        final = respuesta.to_dict()
    else:
        return("Extensión inválida.")
    return(final)

#Prueba de la Función
print(caso_who("owid-covid-data.csv"))

