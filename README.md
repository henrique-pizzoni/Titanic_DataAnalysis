# Titanic_DataAnalysis

Este projeto contém uma análise e limpeza do dataset do Titanic, utilizando Python com bibliotecas como pandas, numpy e scikit-learn.

## Descrição

O dataset original (`Titanic-Dataset.csv`) contém informações sobre passageiros do Titanic. O script `clean_titanic.py` realiza pré-processamento completo, incluindo tratamento de valores ausentes, engenharia de features, remoção de outliers e exportação de um dataset limpo (`titanic_cleaned.csv`).

## Instalação

### 1. Clonagem do Repositório
```bash
git clone https://github.com/henrique-pizzoni/Titanic_DataAnalysis.git
cd Titanic_DataAnalysis
```

### 2. Configuração do Ambiente Virtual (venv)

#### Criar um Ambiente Virtual
```bash
python -m venv .venv
```

#### Ativar o Ambiente Virtual
- **Windows (PowerShell)**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Linux/Mac**:
  ```bash
  source .venv/bin/activate
  ```

#### Desativar o Ambiente Virtual
```bash
deactivate
```

### 3. Instalação de Dependências
Com o ambiente virtual ativado, instale as dependências listadas em `requirements.txt`:
```bash
pip install -r requirements.txt
```

As dependências incluem:
- pandas
- numpy
- matplotlib
- scikit-learn

## Uso

### Executar o Script de Limpeza
Com o ambiente virtual ativado e as dependências instaladas:
```bash
python clean_titanic.py
```

O script irá:
- Carregar o dataset `Titanic-Dataset.csv`.
- Realizar análise exploratória inicial.
- Tratar valores ausentes (Age com mediana, Cabin com 'Unknown', Embarked com moda).
- Ajustar tipos de dados (converter Sex e Embarked para numérico).
- Criar novas features (FamilySize e Title).
- Remover duplicatas e analisar outliers (via boxplots salvos em `outliers_analysis.png`).
- Remover colunas irrelevantes (PassengerId, Ticket, Name).
- Exportar o dataset limpo como `titanic_cleaned.csv`.

### Saída
- `titanic_cleaned.csv`: Dataset processado, pronto para análise ou modelagem.
- `outliers_analysis.png`: Gráficos de boxplot para Age e Fare.
- Resumo no console com dimensões, alterações e estratégias adotadas.

## Estrutura do Projeto
```
Titanic_DataAnalysis/
├── .gitignore
├── README.md
├── requirements.txt
├── Titanic-Dataset.csv
├── clean_titanic.py
├── titanic_cleaned.csv (gerado)
├── outliers_analysis.png (gerado)
└── .venv/ (ambiente virtual, ignorado pelo .gitignore)
```

## Licença
Este projeto é para fins educacionais.