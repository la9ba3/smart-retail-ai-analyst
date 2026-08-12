# FAQ Du Projet

## Quel Est L'Objectif Du Projet ?

L'objectif du projet Smart Retail AI Analyst est de construire une application complète d'analyse retail.

Le projet combine :
- nettoyage de données ;
- analyse exploratoire ;
- segmentation client ;
- API FastAPI ;
- interface Streamlit ;
- futur module RAG ;
- préparation au déploiement cloud.

## Quel Dataset Est Utilisé ?

Le projet utilise le dataset Online Retail du UCI Machine Learning Repository.

Ce dataset contient des transactions d'une entreprise de vente en ligne.

## Pourquoi Nettoyer Le Dataset ?

Le nettoyage est nécessaire parce que le dataset contient :
- des clients sans `CustomerID` ;
- des quantités négatives ou nulles ;
- des prix unitaires invalides ;
- des factures annulées.

Ces lignes peuvent fausser les analyses business.

## Pourquoi Créer `TotalPrice` ?

La colonne `TotalPrice` est calculée avec :

```text
TotalPrice = Quantity * UnitPrice
Elle permet de mesurer le chiffre d'affaires généré par chaque ligne de facture.

## Pourquoi Utiliser RFM ?

RFM permet de segmenter les clients selon :
leur récence d'achat ;
leur fréquence d'achat ;
leur montant dépensé.
C'est une méthode simple, explicable et très utile pour le marketing client.
Avec RFM, on peut identifier :
les clients fidèles ;
les clients à forte valeur ;
les clients récents ;
les clients à risque ;
les clients perdus.

## Pourquoi La Récence Est-Elle Importante ?

La récence indique depuis combien de temps un client n'a pas acheté.
Un client qui a acheté récemment est souvent plus engagé qu'un client qui n'a pas acheté depuis longtemps.
Exemple :
dernier achat il y a 5 jours : client actif ;
dernier achat il y a 250 jours : client dormant ou à risque.

## Pourquoi La Fréquence Est-Elle Importante ?

La fréquence indique combien de commandes un client a passées.
Un client qui commande souvent montre une relation plus forte avec l'entreprise.
Exemple :
1 commande : client occasionnel ;
20 commandes : client fidèle.

## Pourquoi Le Montant Est-Il Important ?

Le montant indique combien un client a dépensé au total.
Un montant élevé peut indiquer un client à forte valeur.
Exemple :
50 euros dépensés : faible valeur ;
5 000 euros dépensés : forte valeur.

## Pourquoi Utiliser KMeans ?

KMeans permet de trouver automatiquement des groupes de clients qui se ressemblent.
Dans ce projet, KMeans utilise :
recency ;
frequency ;
monetary.
Les clusters doivent ensuite être interprétés avec une lecture business.

## Pourquoi Standardiser Les Variables Avant KMeans ?

KMeans utilise des distances entre les clients.
Si les variables n'ont pas la même échelle, une variable peut dominer les autres.
Exemple :
recency est souvent en dizaines ou centaines de jours ;
frequency est souvent en unités ou dizaines ;
monetary peut être en centaines ou milliers.
La standardisation permet de mettre les variables sur une échelle comparable.

## Pourquoi Les Clusters KMeans N'Ont Pas Directement Un Nom Métier ?

KMeans retourne seulement des numéros de clusters, comme :
cluster 0 ;
cluster 1 ;
cluster 2 ;
cluster 3.
Ces numéros ne veulent rien dire seuls.
L'analyste doit regarder :
la récence moyenne ;
la fréquence moyenne ;
le montant moyen ;
le nombre de clients.
Ensuite, il peut donner un nom métier au cluster, comme :
VIP ;
clients fidèles ;
clients potentiels ;
clients dormants.

## Pourquoi Utiliser FastAPI ?

FastAPI permet d'exposer les résultats sous forme d'API.
Ainsi, les KPIs, top produits, top pays et segments peuvent être utilisés par d'autres applications, comme Streamlit.
FastAPI permet aussi de créer une documentation automatique avec Swagger.

## Pourquoi Utiliser Streamlit ?

Streamlit permet de créer une interface utilisateur rapidement avec Python.
Il sert à afficher :
les KPIs ;
les tableaux ;
les graphiques ;
les résultats des analyses.
Dans ce projet, Streamlit appelle l'API FastAPI pour récupérer les données.

## Pourquoi Séparer FastAPI Et Streamlit ?

FastAPI et Streamlit ont deux rôles différents.
FastAPI sert à fournir les données et la logique backend.
Streamlit sert à afficher les résultats à l'utilisateur.
Cette séparation rend le projet plus propre, plus professionnel et plus proche d'une vraie architecture applicative.

## Pourquoi Créer Des Documents Pour Le RAG ?

Le RAG a besoin de documents pour répondre à des questions métier.
Comme le dataset ne contient pas de documents textuels, le projet crée des documents synthétiques expliquant :
le contexte métier ;
la méthode RFM ;
les segments clients ;
la FAQ du projet.

## C'Est Quoi Le RAG ?

RAG signifie Retrieval-Augmented Generation.
En français, cela veut dire génération augmentée par recherche documentaire.
Le principe est simple :
l'utilisateur pose une question ;
le système cherche les passages utiles dans les documents ;
l'IA génère une réponse à partir de ces passages.

## Pourquoi Ne Pas Juste Demander À L'IA Sans Documents ?

Sans documents, l'IA peut répondre de manière trop générale ou inventer des informations.
Avec un RAG, l'IA répond en s'appuyant sur les documents du projet.
Cela rend les réponses plus utiles, plus contextualisées et plus contrôlées.

## Quelles Sont Les Limites Du Projet ?

Le dataset ne contient pas :
de données démographiques ;
de catégories produits complètes ;
de coûts ou marges ;
d'historique marketing ;
de données comportementales web.
Les analyses sont donc centrées sur les transactions.

## Quelles Améliorations Sont Possibles ?

Le projet pourrait être amélioré avec :
une analyse de marge ;
des catégories produits ;
une prédiction du churn ;
une estimation de la customer lifetime value ;
un moteur de recommandation ;
un vrai système RAG connecté à une base vectorielle ;
un déploiement cloud complet sur GCP.