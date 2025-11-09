import pandas as pd
import numpy as np

df = pd.read_csv("Titanic-Dataset.csv")


#Dropando colunas que eu não faço ideia do que sejam
df = df.drop(columns=['Cabin', 'Embarked'])

df = df.dropna()

df = df.drop_duplicates()

#print(df[:20])

#Agrupando sobrevivência por classe econômica em que cada passageiro está
#Hipótese 1: Passageiros de classes melhores tem maior taxa de sobrevivência

df_tamanho = df.groupby('Pclass')['PassengerId'].count()
print(df_tamanho)

df_classes = df.groupby('Pclass')['Survived'].sum()
print(df_classes)

percentual = df_classes/df_tamanho
print(percentual)
#Hipótese comprovada!


#Hipótese 2: Taxa de sobrevivência por idade (pessoas adultas tem mais chances de sobreviver)
# Definir os limites das faixas
df_copia = df

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, np.inf]
# Definir os nomes para cada faixa (um a menos que os limites)
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
# right=False faz com que a faixa '10-20' inclua idades de 10 até 19.99...
df_copia['Faixa_Etaria'] = pd.cut(df_copia['Age'], bins=bins, labels=labels, right=False)
# Vamos ver a taxa de sobrevivência por faixa
taxa_sobrevivencia = df_copia.groupby('Faixa_Etaria')['Survived'].mean()

print(taxa_sobrevivencia)
#Detalhe, não tinha ninguém entre 70 e 80 anos, e só uma pessoa com mais de 80 anos.
#Hipótese negada> Crianças entre 0-10 anos e pessoas +80 tiveram maior taxas de sobrevivência