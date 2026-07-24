## 2026-07-23 - Tâche 2.1



### Objectif



Télécharger le dataset Online Retail depuis UCI et le sauvegarder localement.



### Ce que j'ai appris


J'ai appris à utiliser `ucimlrepo` pour récupérer un dataset depuis le UCI Machine Learning Repository. J'ai aussi appris qu'un dataset brut doit être sauvegardé dans `data/raw/`.



### Ce que j'ai codé



J'ai créé le script `src/data/download\_online\_retail.py`. Ce script télécharge le dataset Online Retail avec `fetch\_ucirepo(id=352)` puis le sauvegarde dans `data/raw/online\_retail\_raw.csv`.



### Erreurs rencontrées



Aucune erreur bloquante pour l'instant.


### Solution



Le fichier CSV est ignoré par Git grâce à `.gitignore`, car les datasets volumineux ne doivent pas forcément être versionnés.



### Prochaine étape



Valider la tâche 2.1 avant de passer à la tâche 2.2.


## 2026-07-23 - Tâche 2.2

### Objectif

Comprendre les colonnes du dataset Online Retail avant de commencer le nettoyage.

### Ce que j'ai appris

J'ai appris à utiliser `head()`, `info()`, `describe()` et `isna().sum()` pour observer un dataset avec Pandas.

J'ai aussi appris la différence entre `online_retail.data.features` et `online_retail.data.original` avec `ucimlrepo`. Dans ce projet, il faut utiliser `original` pour garder toutes les colonnes du dataset, notamment `InvoiceNo` et `StockCode`.

### Ce que j'ai codé

J'ai corrigé le script `src/data/download_online_retail.py` pour sauvegarder le dataset complet avec 8 colonnes.

J'ai aussi créé `docs/data_dictionary.md` pour expliquer chaque colonne en français.

### Erreurs rencontrées

Au début, le fichier CSV ne contenait que 6 colonnes au lieu de 8, car le script utilisait `online_retail.data.features`.

### Solution

J'ai remplacé :

```python
df = online_retail.data.features


## 2026-07-23 - Tâche 2.3

### Objectif 

Nettoyer le dataset Online retail pour garder uniquement les transactions valides 

### Ce que j'ai appris 

J'ai appris à identifier les valeurs manquantes , les quantités invalides , les prix invalides et les  factures annulées . ainsi ajouter une colonne calculé 

### Ce que j'ai coder 

j'ai creer le script : data\online_retail_clean.py 

le scrpt : 
- lit 'data\raw\online_retail_raw.csv 
- compte les problèmes de qualité
- supprime les lignes sans `CustomerID`
- garde seulement `Quantity > 0`
- garde seulement `UnitPrice > 0`
- retire les factures dont `InvoiceNo` commence par `C`
- convertit `InvoiceDate` en date
- convertit `CustomerID` en entier
- crée `TotalPrice = Quantity * UnitPrice`
- sauvegarde `data/processed/online_retail_clean.csv`

### Erreurs rencontrées

Au début, le script nettoyait les données en mémoire mais ne créait pas le fichier de sortie, car la ligne `clean_df.to_csv(output_path, index=False)` manquait.

### Solution

J'ai ajouté :

```python
clean_df.to_csv(output_path, index=False)
avant les messages finaux du script.
Résultats
Lignes avant nettoyage : 541909
CustomerID manquants : 135080
Quantity <= 0 : 10624
UnitPrice <= 0 : 2517
Factures annulées : 9288
Lignes après nettoyage : 397884
Lignes supprimées : 144025
Factures annulées restantes : 0


## 2026-07-23 - Tâche 3.1

### Objectif

Calculer les KPIs globaux du dataset Online Retail nettoyé.

### Ce que j'ai appris

J'ai appris ce qu'est un KPI et comment calculer des indicateurs business avec Pandas. J'ai aussi appris la différence entre un script Python réutilisable et un notebook d'exploration.

### Ce que j'ai codé

J'ai créé `src/analysis/kpis.py` avec une fonction `calculate_global_kpis`.

J'ai aussi créé `notebooks/02_eda_kpis.ipynb` pour afficher les KPIs dans un notebook.

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

Les KPIs sont calculés à partir du dataset nettoyé `data/processed/online_retail_clean.csv`.

### Résultats

Les KPIs calculés sont :
- chiffre d'affaires total ;
- nombre de factures ;
- nombre de clients ;
- nombre de produits ;
- nombre de pays ;
- panier moyen.

## 2026-07-24 - Tâche 3.2

### Objectif

Analyser l'évolution des ventes dans le temps.

### Ce que j'ai appris

J'ai appris à convertir une colonne en date avec `pd.to_datetime`, à utiliser `.dt` pour extraire des informations temporelles et à regrouper les ventes par mois avec `groupby`.

### Ce que j'ai codé

J'ai créé `src/analysis/time_analysis.py`.

Le script :
- lit `data/processed/online_retail_clean.csv`
- convertit `InvoiceDate` en date
- crée les colonnes `Year`, `Month`, `Day`, `Hour` et `YearMonth`
- calcule le chiffre d'affaires mensuel
- calcule le nombre de factures mensuel
- sauvegarde `data/processed/monthly_sales.csv`

J'ai aussi créé `notebooks/03_time_analysis.ipynb` avec un graphique des ventes mensuelles.

### Erreurs rencontrées

Au début, le script affichait `KeyError: 'YearMonth'`, car la colonne `YearMonth` n'était pas créée avant le `groupby`.

### Solution

J'ai ajouté :

```python
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)