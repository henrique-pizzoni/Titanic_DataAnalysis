import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import os

# Carregar dados
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Titanic-Dataset.csv'))
print("Dimensões originais:", df.shape)

# 1. Análise Exploratória Inicial
print("\nPrimeiras 5 linhas:")
print(df.head())

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nInformações sobre tipos de dados e valores nulos:")
print(df.info())

# 2. Tratamento de Valores Ausentes
print("\nValores nulos antes do tratamento:")
print(df.isnull().sum())

# Age: Preencher com mediana, pois é robusta a outliers
df['Age'] = df['Age'].fillna(df['Age'].median())

# Cabin: Preencher com 'Unknown' devido à alta cardinalidade e muitos nulos
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Embarked: Preencher com a moda
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("\nValores nulos após tratamento:")
print(df.isnull().sum())

# 3. Ajuste de Tipos de Dados
# Converter Sex e Embarked para numérico usando LabelEncoder
le = LabelEncoder()
#df['Sex'] = le.fit_transform(df['Sex'])
#df['Embarked'] = le.fit_transform(df['Embarked'])

#Decidimos não transformar essas colunas em numéricas neste ponto para preservar interpretabilidade.

# Verificar Survived e Pclass (devem ser int)
#print("\nTipos de dados após ajustes:")
#print(df.dtypes)

#Não é necessário ajuste adicional, pois já estão em int64.


# 4. Feature Engineering
# Criar FamilySize
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Extrair títulos de Name
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# Agrupar títulos raros
title_mapping = {
    "Mr": "Mr",
    "Mrs": "Mrs",
    "Miss": "Miss",
    "Master": "Master",
    "Dr": "Officer",
    "Rev": "Officer",
    "Col": "Officer",
    "Major": "Officer",
    "Mlle": "Miss",
    "Countess": "Royalty",
    "Ms": "Mrs",
    "Lady": "Royalty",
    "Jonkheer": "Royalty",
    "Don": "Royalty",
    "Dona": "Royalty",
    "Mme": "Mrs",
    "Capt": "Officer",
    "Sir": "Royalty"
}
df['Title'] = df['Title'].map(title_mapping).fillna('Rare')

# Converter Title para numérico
#df['Title'] = le.fit_transform(df['Title'])

#

# 5. Tratamento de Duplicatas e Outliers
# Remover duplicatas
initial_shape = df.shape
df.drop_duplicates(inplace=True)
print(f"\nDuplicatas removidas: {initial_shape[0] - df.shape[0]}")

'''
# Analisar outliers em Fare e Age com boxplots
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.boxplot(df['Age'])
plt.title('Boxplot de Age')
plt.ylabel('Age')

plt.subplot(1, 2, 2)
plt.boxplot(df['Fare'])
plt.title('Boxplot de Fare')
plt.ylabel('Fare')

plt.tight_layout()
plt.savefig('outliers_analysis.png')
plt.show()
'''

# 6. Limpeza de Colunas Irrelevantes
# Remover PassengerId, Ticket, Name
df.drop(['PassengerId', 'Ticket', 'Name'], axis=1, inplace=True)

# 7. Exportação do Dataset Limpo
df.to_csv('titanic_cleaned.csv', index=False)

print("\nDimensões finais:", df.shape)
print("\nColunas restantes:")
print(df.columns.tolist())

# Resumo final
print("\n--- RESUMO FINAL ---")
print(f"Dimensões antes: {initial_shape}")
print(f"Dimensões depois: {df.shape}")
print("Colunas alteradas/removidas:")
print("- Age: Preenchido com mediana")
print("- Cabin: Preenchido com 'Unknown'")
print("- Embarked: Preenchido com moda")
#print("- Sex: Convertido para numérico (LabelEncoder)")
#print("- Embarked: Convertido para numérico (LabelEncoder)")
print("- Title: Extraído de Name")
print("- FamilySize: Criado a partir de SibSp + Parch + 1")
print("- PassengerId, Ticket, Name: Removidos")
print("Estratégias para valores nulos:")
print("- Age: Mediana (robusta a outliers)")
print("- Cabin: 'Unknown' (alta cardinalidade)")
print("- Embarked: Moda (valor mais frequente)")