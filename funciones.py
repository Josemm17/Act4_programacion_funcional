# a) FUNCIÓN PARA CARGAR UN ARCHIVO COMO DATAFRAME

def cargar_dataset(archivo):
    import pandas as pd
    import os
    
    extension=os.path.splitext(archivo)[1].lower()

    if extension==".csv":
        df=pd.read_csv(archivo)
        return(df)

    elif extension==".xlsx":
        df=pd.read_excel(archivo)
        return(df)
    
    elif extension==".json":
        df=pd.read_json(archivo)
        return(df)
        
    elif extension==".html":
        df=pd.read_html(archivo)
        return(df)
    else:

            raise ValueError(f"Formato de archivo no soportado: {extension}")
################################################################################


# b) FUNCIÓN PARA SUSTITUIR VALORES NULOS CON FFILL

def sustitución_ffill(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cualitativas = cualitativas_con_nulos.fillna(method="ffill")
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
################################################################################


# c) FUNCIÓN PARA SUSTITUIR VALORES NULOS CON BFILL

def sustitución_bfill(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cualitativas = cualitativas_con_nulos.fillna(method="bfill")
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
################################################################################


# d) FUNCIÓN PARA SUSTITUIR VALORES NULOS CON UN STRING 
 
def sustitución_string(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cualitativas = cualitativas_con_nulos.fillna("Sin registro")
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos) 
################################################################################


# e) FUNCIÓN PARA SUSTITIUR VALORES NULOS CON EL PROMEDIO

def sustitución_promedio(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.mean(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
################################################################################


# f) FUNCIÓN PARA SUSTITUIR VALORES NULOS CON LA MEDIANA

def sustitución_mediana(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.median(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
################################################################################


# g) FUNCIÓN PARA SUSTITUIR VALORES NULOS CON UN VALOR CONSTANTE

def sustitución_constante(dataframe):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(10)
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
################################################################################


# i) FUNCIÓN PARA IDENTIFICAR VALORES NULOS POR COLUMNA Y POR DATAFRAME

def cuenta_valores_nulos(dataframe):
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()
    
    return("Valores nulos por columna:", valores_nulos_cols,
            "Valores nulos por dataframe: ", valores_nulos_df)
################################################################################
