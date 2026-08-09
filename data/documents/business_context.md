# Contexte Métier

## Présentation Du Projet

Smart Retail AI Analyst est un projet portfolio basé sur le dataset Online Retail.

L'objectif est d'analyser les transactions clients, de comprendre la performance des ventes, de segmenter les clients et de préparer un assistant IA capable de répondre à des questions métier à partir de données structurées et de documents.

## Contexte Du Dataset

Le dataset Online Retail contient des transactions d'une entreprise de vente en ligne.

Chaque ligne représente une ligne de facture, c'est-à-dire un produit acheté dans une commande. Une même facture peut contenir plusieurs produits.

Les colonnes importantes sont :
- `InvoiceNo` : identifiant de la facture ;
- `StockCode` : identifiant du produit ;
- `Description` : nom du produit ;
- `Quantity` : quantité achetée ;
- `InvoiceDate` : date et heure de transaction ;
- `UnitPrice` : prix unitaire ;
- `CustomerID` : identifiant du client ;
- `Country` : pays du client.

## Objectifs Métier

Les objectifs principaux sont :
- comprendre la performance globale des ventes ;
- identifier les meilleurs produits et les meilleurs pays ;
- segmenter les clients selon leur valeur et leur comportement ;
- détecter les clients fidèles, les clients à forte valeur et les clients inactifs ;
- préparer des actions marketing personnalisées ;
- exposer les résultats via une API et un dashboard.

## Périmètre Analytique

Le projet couvre :
- le nettoyage des données ;
- l'analyse exploratoire ;
- le scoring RFM ;
- la segmentation KMeans ;
- les endpoints FastAPI ;
- le dashboard Streamlit ;
- le futur assistant RAG.

## Limites

Le dataset ne contient pas de données démographiques détaillées, d'historique de campagnes marketing, de catégories produits complètes ou de marges.

L'analyse se concentre donc sur le comportement transactionnel plutôt que sur l'identité complète ou la profitabilité réelle des clients.