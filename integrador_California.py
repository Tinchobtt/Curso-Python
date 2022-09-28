import pandas as pd

archivo = pd.read_excel('california_housing_train.xlsx')

casas = 0
filtro = (archivo['longitude'] >= -120) & (archivo['longitude'] <= -118)

 