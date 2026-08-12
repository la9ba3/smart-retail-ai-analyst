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

## 2026-07-24 - Tâche 3.3

### Objectif

Identifier les meilleurs produits et les principaux pays en chiffre d'affaires.

### Ce que j'ai appris

J'ai appris à utiliser `groupby` pour regrouper les ventes par produit et par pays. J'ai aussi appris à trier les résultats avec `sort_values`, à garder les 10 premiers résultats avec `head(10)` et à créer des graphiques en barres horizontales avec Matplotlib.

### Ce que j'ai codé

J'ai créé `src/analysis/top_products_countries.py`.

Le script calcule :
- les 10 produits générant le plus de chiffre d'affaires ;
- les 10 produits les plus vendus en quantité ;
- les 10 pays générant le plus de chiffre d'affaires.

J'ai aussi créé `notebooks/04_top_products_countries.ipynb` avec les tableaux et graphiques correspondants.

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

Les analyses utilisent le dataset nettoyé `data/processed/online_retail_clean.csv`.

### Résultats

Les fichiers générés localement sont :
- `data/processed/top_products_by_revenue.csv`
- `data/processed/top_products_by_quantity.csv`
- `data/processed/top_countries_by_revenue.csv`

Ces fichiers ne sont pas envoyés sur GitHub car `data/processed/` est ignoré.

### Prochaine étape

Valider la tâche 3.3 avant de passer à la construction de la table client.

## 2026-08-05 - Tâche 4.1

### Objectif

Construire une table client à partir du dataset transactionnel nettoyé.

### Ce que j'ai appris

J'ai appris à passer d'une table de transactions à une table client avec `groupby`. J'ai compris que chaque ligne de la nouvelle table représente un client unique.

### Ce que j'ai codé

J'ai créé `src/ml/customer_features.py`.

Le script :
- lit `data/processed/online_retail_clean.csv`
- convertit `InvoiceDate` en date
- regroupe les lignes par `CustomerID`
- calcule la dernière date d'achat
- calcule le nombre de factures différentes
- calcule la quantité totale achetée
- calcule le montant total dépensé
- choisit le pays le plus fréquent du client
- sauvegarde `data/processed/customer_features.csv`

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

La table client est créée avec `groupby("CustomerID")` et plusieurs agrégations Pandas.

### Résultats

Le fichier `customer_features.csv` contient une ligne par client avec les colonnes :
- `CustomerID`
- `last_purchase_date`
- `frequency`
- `total_quantity`
- `total_spent`
- `country`

### Prochaine étape

Valider la tâche 4.1 avant de passer au scoring RFM.

## 2026-08-07 - Tâche 4.2

### Objectif

Créer un scoring RFM pour segmenter les clients selon leur récence, leur fréquence d'achat et leur montant dépensé.

### Ce que j'ai appris

J'ai appris que le RFM signifie Recency, Frequency et Monetary. J'ai compris que la récence mesure depuis combien de jours un client n'a pas acheté, que la fréquence mesure le nombre d'achats et que le montant mesure la dépense totale.

J'ai aussi appris à utiliser `pd.qcut` pour transformer des valeurs numériques en scores de 1 à 5, et `apply(..., axis=1)` pour attribuer un segment à chaque client.

### Ce que j'ai codé

J'ai créé `src/ml/rfm_scoring.py`.

Le script :
- lit `data/processed/customer_features.csv`
- calcule `recency`
- reprend `frequency`
- calcule `monetary`
- crée `recency_score`, `frequency_score` et `monetary_score`
- crée `rfm_score`
- attribue un segment client
- sauvegarde `data/processed/customer_rfm.csv`

J'ai aussi créé `notebooks/05_rfm_scoring.ipynb` avec un graphique des segments clients.

### Erreurs rencontrées

Le notebook affichait `KeyError: 'segment'`, car certains noms de colonnes contenaient des espaces cachés, par exemple `" segment"` au lieu de `"segment"`.

### Solution

J'ai nettoyé les noms de colonnes avec :

```python
df.columns = df.columns.str.strip()

## 2026-08-08 - Tâche 4.3

### Objectif

Segmenter automatiquement les clients avec KMeans à partir des variables RFM.

### Ce que j'ai appris

J'ai appris que KMeans regroupe automatiquement les clients qui se ressemblent. J'ai compris pourquoi il faut standardiser les variables avec `StandardScaler`, car `recency`, `frequency` et `monetary` n'ont pas la même échelle.

J'ai aussi appris la méthode du coude pour choisir un nombre raisonnable de clusters et l'importance d'interpréter les clusters avec une lecture business.

### Ce que j'ai codé

J'ai créé `src/ml/kmeans_segmentation.py`.

Le script :
- lit `data/processed/customer_rfm.csv`
- sélectionne `recency`, `frequency` et `monetary`
- standardise les variables avec `StandardScaler`
- teste plusieurs valeurs de K
- entraîne un modèle KMeans avec 4 clusters
- ajoute une colonne `cluster`
- crée un résumé des clusters
- sauvegarde `customer_segments.csv`, `kmeans_elbow_scores.csv` et `kmeans_cluster_summary.csv`

J'ai aussi créé `notebooks/06_kmeans_segmentation.ipynb` avec :
- un graphique de la méthode du coude
- un graphique du nombre de clients par cluster
- une interprétation business des clusters

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

La segmentation utilise les variables RFM standardisées afin que KMeans ne soit pas dominé par la variable `monetary`.

### Résultats

Les clusters observés sont :
- Cluster 2 : VIP / Champions
- Cluster 0 : High Value Loyal Customers
- Cluster 3 : Regular / Potential Customers
- Cluster 1 : Dormant / Low Engagement Customers

### Prochaine étape

Valider la tâche 4.3 avant de passer à l'API FastAPI minimale.

## 2026-08-08 - Tâche 5.1

### Objectif

Créer une API minimale avec FastAPI et vérifier qu'elle répond correctement.

### Ce que j'ai appris

J'ai appris qu'une API permet à deux programmes de communiquer. J'ai compris qu'un endpoint est une adresse précise de l'API, comme `/health`, et que `GET` sert à récupérer une information.

J'ai aussi appris que FastAPI génère automatiquement une documentation Swagger disponible sur `/docs`.

### Ce que j'ai codé

J'ai créé `backend/main.py`.

Le fichier :
- crée une application FastAPI
- définit le titre, la description et la version de l'API
- ajoute un endpoint `GET /health`
- retourne une réponse JSON avec le statut du service

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

Le serveur est lancé avec `uvicorn backend.main:app --reload`.

### Résultats

L'endpoint `/health` retourne :

```json
{
  "status": "ok",
  "service": "smart-retail-ai-analyst-api",
  "version": "0.1.0"
}

## 2026-08-09 - Tâche 5.2

### Objectif

Créer les endpoints FastAPI pour exposer les principaux résultats data du projet.

### Ce que j'ai appris

J'ai appris qu'une API permet de rendre les résultats accessibles à d'autres applications. Les scripts créent les fichiers de données, tandis que l'API lit ces fichiers et les retourne en JSON.

J'ai aussi appris à utiliser des paramètres de requête avec `Query`, comme `limit`, pour contrôler le nombre de résultats retournés.

### Ce que j'ai codé

J'ai modifié `backend/main.py`.

Les endpoints créés sont :
- `GET /dataset-summary`
- `GET /sales-kpis`
- `GET /top-products`
- `GET /top-countries`
- `GET /rfm-segments`

J'ai ajouté une fonction `load_csv` pour lire les fichiers CSV et retourner une erreur claire si un fichier est manquant.

J'ai aussi limité le paramètre `limit` entre 1 et 50 avec `Query`.

### Erreurs rencontrées

L'endpoint `/dataset-summary` retournait une erreur `500 Internal Server Error`.

La cause était une erreur de lecture CSV :
`Expected 9 fields in line 111, saw 10`.

### Solution

Certaines descriptions produits contiennent des virgules, comme `"AIRLINE LOUNGE,METAL SIGN"`. Le CSV contenait aussi des espaces après les séparateurs.

J'ai corrigé la lecture CSV avec :

```python
df = pd.read_csv(path, skipinitialspace=True)
df.columns = df.columns.str.strip()


## 2026-08-09 - Tâche 6.1

### Objectif

Créer la première interface utilisateur Streamlit du projet.

### Ce que j'ai appris

J'ai appris que Streamlit permet de créer une interface web en Python. J'ai compris que FastAPI sert de backend pour fournir les données, tandis que Streamlit sert de frontend pour les afficher à l'utilisateur.

J'ai aussi appris qu'il faut lancer FastAPI et Streamlit dans deux terminaux différents lorsque l'interface appelle l'API.

### Ce que j'ai codé

J'ai créé `frontend/app.py`.

L'application contient :
- une configuration de page Streamlit ;
- un menu latéral ;
- plusieurs vues de base : Home, Dataset, Sales KPIs, Products, Customers, RFM Segments et Architecture ;
- une vérification simple de connexion au backend via `GET /health`.

### Erreurs rencontrées

Streamlit a demandé une adresse email au premier lancement. Ce champ n'est pas obligatoire et peut être laissé vide.

### Solution

J'ai appuyé sur Entrée sans saisir d'email pour continuer.

### Résultats

L'application Streamlit démarre avec :

```powershell
streamlit run frontend\app.py


## 2026-08-09 - Tâche 6.2

### Objectif

Créer un dashboard analytics Streamlit connecté au backend FastAPI.

### Ce que j'ai appris

J'ai appris que Streamlit peut appeler une API avec `requests`. J'ai compris que FastAPI fournit les données en JSON et que Streamlit transforme ces réponses en tableaux, métriques et graphiques.

J'ai aussi compris qu'il faut lancer deux services pendant le développement : FastAPI pour servir les données et Streamlit pour afficher l'interface.

### Ce que j'ai codé

J'ai modifié `frontend/app.py`.

L'application affiche maintenant :
- un résumé du dataset ;
- les KPIs de ventes ;
- le top 10 produits par chiffre d'affaires ;
- les segments RFM ;
- une page architecture.

J'ai ajouté une fonction `get_api_data` pour centraliser les appels au backend.

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

Les données sont récupérées depuis FastAPI avec `requests.get`,

## 2026-08-09 - Tâche 7.1

### Objectif

Créer des documents métier pour préparer le futur module RAG.

### Ce que j'ai appris

J'ai appris qu'un RAG a besoin de documents pour répondre à des questions avec du contexte. Comme le dataset Online Retail ne contient pas de documents textuels, j'ai créé des documents synthétiques liés au projet.

J'ai aussi compris que ces documents servent à la fois à documenter le projet et à fournir une base de connaissance au futur assistant IA.

### Ce que j'ai créé

J'ai créé les fichiers suivants dans `data/documents/` :
- `business_context.md`
- `rfm_methodology.md`
- `customer_segments_guide.md`
- `project_faq.md`

Les documents sont écrits en français pour faciliter la compréhension pendant l'apprentissage.

### Erreurs rencontrées

Au début, les documents étaient proposés en anglais. J'ai décidé de les écrire en français pour mieux comprendre les concepts

## 2026-08-11 - Tâche 7.2

### Objectif

Créer un pipeline RAG local pour rechercher des passages pertinents dans les documents métier du projet.

### Ce que j'ai appris

J'ai appris qu'un RAG se compose de plusieurs étapes : documents, chunks, embeddings, base vectorielle, recherche et réponse.

J'ai compris qu'un embedding transforme un texte en vecteur numérique, et que ChromaDB compare ces vecteurs pour retrouver les passages les plus proches d'une question.

J'ai aussi appris que dans cette tâche, on construit d'abord la partie retrieval du RAG, sans encore brancher un LLM externe.

### Ce que j'ai codé

J'ai créé `src/rag/local_rag.py`.

Le script :
- charge les fichiers Markdown depuis `data/documents/`
- découpe les documents en chunks
- crée des embeddings avec `sentence-transformers/all-MiniLM-L6-v2`
- stocke les chunks et embeddings dans ChromaDB
- recherche les passages pertinents à partir d'une question
- retourne une réponse simple avec les sources trouvées
- permet de poser une question depuis PowerShell avec `sys.argv`

### Erreurs rencontrées

J'ai fait une faute dans le nom du package `sentence-transformers` lors de l'installation.

### Solution

J'ai corrigé la commande d'installation avec :

```powershell
pip install chromadb sentence-transformers
J'ai aussi ajouté data/processed/chroma_db/ dans .gitignore pour ne pas envoyer la base vectorielle locale sur GitHub.

### Résultats

Le pipeline local peut répondre à une question comme :
python src\rag\local_rag.py "Pourquoi utiliser RFM ?"
Il retourne les passages les plus pertinents depuis les documents métier.

## 2026-08-11 - Tâche 8.1

### Objectif

Créer un endpoint `/chat-docs` pour interroger les documents métier du projet via l'API FastAPI.

### Ce que j'ai appris

J'ai appris la différence entre `GET` et `POST`. Pour `/chat-docs`, on utilise `POST` parce que l'utilisateur envoie une question dans le corps de la requête.

J'ai aussi appris que Pydantic permet de valider les données envoyées à l'API avec `BaseModel` et `Field`.

### Ce que j'ai codé

J'ai modifié `backend/main.py`.

J'ai ajouté :
- le modèle `ChatDocsRequest`
- l'endpoint `POST /chat-docs`
- l'appel au RAG local avec `answer_question`
- le retour des sources avec `search_documents`

J'ai aussi modifié `frontend/app.py` pour ajouter une page `Chat Documents`.

Cette page permet :
- de saisir une question ;
- de choisir le nombre de chunks ;
- d'envoyer la question à FastAPI ;
- d'afficher la réponse et les sources.

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

Le système utilise la base ChromaDB locale créée par `src/rag/local_rag.py`.

### Résultats

L'endpoint `/chat-docs` peut recevoir une requête comme :

```json
{
  "question": "Pourquoi utiliser RFM ?",
  "top_k": 3
}

## 2026-08-11 - Tâche 8.2

### Objectif

Créer un module de chat data simple pour répondre à des questions prédéfinies sur les résultats du projet.

### Ce que j'ai appris

J'ai appris qu'un chat data simple peut fonctionner avec une détection d'intention par mots-clés. Cette approche ne comprend pas toutes les formulations possibles, mais elle permet de créer une première interaction utile sans LLM.

J'ai aussi appris à exposer cette logique via un endpoint FastAPI `POST /chat-data` et à l'appeler depuis Streamlit.

### Ce que j'ai codé

J'ai créé `src/analysis/simple_data_chat.py`.

Le module peut répondre aux questions sur :
- le chiffre d'affaires ;
- les top produits ;
- les top pays ;
- le nombre de clients ;
- les segments RFM.

J'ai modifié `backend/main.py` pour ajouter :
- `ChatDataRequest`
- `POST /chat-data`

J'ai modifié `frontend/app.py` pour ajouter une page `Chat Data`.

### Erreurs rencontrées

Aucune erreur bloquante pour l'instant.

### Solution

La fonction `detect_intent` utilise des mots-clés pour router la question vers la bonne fonction d'analyse.

### Résultats

L'utilisateur peut poser une question simple depuis Streamlit, et l'application retourne :
- l'intention détectée ;
- une réponse textuelle basée sur les données préparées.

### Prochaine étape
## 2026-08-12 - Tâche 8.3

### Objectif

Intégrer Mistral API au pipeline RAG pour générer des réponses naturelles à partir des documents métier.

### Ce que j'ai appris

J'ai appris la différence entre un RAG local qui retrouve des passages et un RAG génératif qui utilise un LLM externe pour rédiger une réponse.

J'ai compris que Mistral reçoit la question utilisateur et les passages retrouvés par ChromaDB, puis génère une réponse synthétique basée sur ce contexte.

J'ai aussi appris à stocker une clé API dans `.env` et à documenter les variables nécessaires dans `.env.example` sans exposer de secret.

### Ce que j'ai codé

J'ai créé `src/rag/mistral_rag.py`.

Le module :
- charge les variables d'environnement avec `load_dotenv`
- lit `MISTRAL_API_KEY` et `MISTRAL_MODEL`
- recherche les documents pertinents avec `search_documents`
- construit un contexte documentaire
- appelle Mistral API
- retourne une réponse générée avec les sources utilisées

J'ai modifié `backend/main.py` pour utiliser `generate_answer_with_mistral` dans l'endpoint `POST /chat-docs`.

J'ai aussi ajouté une vérification de configuration pour retourner une erreur claire si `MISTRAL_API_KEY` manque.

### Erreurs rencontrées

J'ai rencontré une erreur d'import du SDK Mistral, puis une erreur `ModuleNotFoundError: No module named 'src'` lors du lancement direct du fichier.

J'ai aussi rencontré une erreur `401 Invalid API Key`, liée à la clé API Mistral.

### Solution

J'ai corrigé l'import Mistral selon la version du SDK installée.

J'ai lancé le module avec :

```powershell
python -m src.rag.mistral_rag

au lieu de lancer directement le fichier.
J'ai vérifié la variable MISTRAL_API_KEY dans .env et corrigé la clé.

## Résultats


L'endpoint POST /chat-docs utilise maintenant :

- ChromaDB pour retrouver les passages pertinents ;
- Mistral API pour générer une réponse naturelle ;
- les sources documentaires pour garder la réponse traçable.