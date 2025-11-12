# Limpeza do Dataset Titanic

Este documento descreve o processo de limpeza e pré-processamento aplicado ao dataset do Titanic, implementado no script `clean_titanic.py`.

## Visão Geral do Dataset Original

O dataset `Titanic-Dataset.csv` contém 891 registros de passageiros do Titanic, com 12 colunas iniciais:
- `PassengerId`: ID único do passageiro
- `Survived`: Sobrevivência (0 = Não, 1 = Sim)
- `Pclass`: Classe do bilhete (1, 2, 3)
- `Name`: Nome completo
- `Sex`: Gênero
- `Age`: Idade
- `SibSp`: Número de irmãos/cônjuges a bordo
- `Parch`: Número de pais/filhos a bordo
- `Ticket`: Número do bilhete
- `Fare`: Tarifa paga
- `Cabin`: Número da cabine
- `Embarked`: Porto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton)

## Problemas Identificados

### Valores Ausentes
- `Age`: 177 valores ausentes (19.87%)
- `Cabin`: 687 valores ausentes (77.10%)
- `Embarked`: 2 valores ausentes (0.22%)

### Outros Problemas
- Dados categóricos não numéricos (`Sex`, `Embarked`)
- Possíveis outliers em `Fare` e `Age`
- Colunas irrelevantes para modelagem (`PassengerId`, `Ticket`, `Name`)
- Falta de features derivadas

## Estratégias de Limpeza Aplicadas

### 1. Tratamento de Valores Ausentes

#### Age
- **Estratégia**: Preenchimento com mediana
- **Justificativa**: A mediana é robusta a outliers, preservando a distribuição dos dados
- **Valor usado**: 28.0 anos

#### Cabin
- **Estratégia**: Preenchimento com 'Unknown'
- **Justificativa**: Alta cardinalidade (muitos valores únicos) torna imputação estatística inadequada
- **Alternativa considerada**: Criar coluna binária `Cabin_known` (0/1), mas optou-se por simplicidade

#### Embarked
- **Estratégia**: Preenchimento com moda
- **Justificativa**: Poucos valores ausentes, moda representa o valor mais provável
- **Valor usado**: 'S' (Southampton)

### 2. Ajuste de Tipos de Dados

#### Sex
- **Conversão**: De string para inteiro usando LabelEncoder
- **Mapeamento**: female → 0, male → 1

#### Embarked
- **Conversão**: De string para inteiro usando LabelEncoder
- **Mapeamento**: C → 0, Q → 1, S → 2

#### Survived e Pclass
- **Verificação**: Já estão como int64, adequados para modelagem

### 3. Feature Engineering

#### FamilySize
- **Cálculo**: `SibSp + Parch + 1`
- **Justificativa**: Representa o tamanho total da família a bordo, incluindo o passageiro
- **Tipo**: int64

#### Title
- **Extração**: Regex ` ([A-Za-z]+)\.` do campo `Name`
- **Agrupamento**: Títulos raros agrupados em categorias
  - Mr, Mrs, Miss, Master: Mantidos
  - Dr, Rev, Col, Major, Mlle, Countess, Ms, Lady, Jonkheer, Don, Dona, Mme, Capt, Sir: Agrupados como Officer, Royalty ou Rare
- **Conversão**: Para numérico usando LabelEncoder

### 4. Tratamento de Duplicatas e Outliers

#### Duplicatas
- **Verificação**: Nenhuma duplicata encontrada
- **Ação**: Nenhuma remoção necessária

#### Outliers
- **Análise**: Boxplots gerados para `Age` e `Fare`
- **Decisão**: Mantidos, pois podem ser informativos (ex.: bilhetes caros indicam status social)
- **Arquivo**: `outliers_analysis.png`

### 5. Limpeza de Colunas Irrelevantes

#### Colunas Removidas
- `PassengerId`: ID único, não contribui para padrões
- `Ticket`: Alta cardinalidade, pouco informativo
- `Name`: Dados textuais complexos, títulos já extraídos

## Resultado Final

### Dimensões
- **Original**: 891 linhas × 12 colunas
- **Final**: 891 linhas × 11 colunas

### Colunas Finais
1. `Survived` (int64)
2. `Pclass` (int64)
3. `Sex` (int64, encoded)
4. `Age` (float64, preenchido)
5. `SibSp` (int64)
6. `Parch` (int64)
7. `Fare` (float64)
8. `Cabin` (object, preenchido)
9. `Embarked` (int64, encoded)
10. `FamilySize` (int64, nova)
11. `Title` (int64, nova, encoded)

### Arquivos Gerados
- `titanic_cleaned.csv`: Dataset processado
- `outliers_analysis.png`: Visualização de outliers

## Considerações Finais

Este processo de limpeza prepara o dataset para análises posteriores ou modelagem preditiva. As decisões foram tomadas visando:
- Minimizar perda de informação
- Manter integridade estatística
- Facilitar uso em algoritmos de machine learning
- Documentar todas as transformações para reprodutibilidade

Para executar a limpeza, consulte o `README.md` para instruções de ambiente e execução.