# Smart Retail AI Analyst - Portfolio Summary

## Short Project Pitch

Smart Retail AI Analyst is an end-to-end data and AI project built on the Online Retail dataset. It combines data cleaning, retail analytics, RFM customer segmentation, KMeans clustering, FastAPI, Streamlit, RAG, Mistral AI, LangFuse, Docker and Google Cloud Platform.

The project turns raw e-commerce transactions into business insights and exposes them through an API, a dashboard and an AI assistant.

## 30-Second Interview Pitch

I built an end-to-end retail analytics and AI assistant project using Python. The project cleans the Online Retail dataset, calculates business KPIs, analyzes sales by product, country and month, and segments customers with RFM scoring and KMeans clustering.

I exposed the analytics through a FastAPI backend and a Streamlit dashboard. I also built a RAG pipeline with ChromaDB, sentence-transformer embeddings and Mistral AI, with LangFuse tracing to monitor the LLM calls.

Finally, I containerized the backend with Docker, deployed it on Google Cloud Run, uploaded cleaned data to Cloud Storage and BigQuery, and added initial Pytest unit tests.

## CV Bullet Points

- Built an end-to-end retail analytics and AI assistant project using Python, Pandas, FastAPI, Streamlit and Google Cloud Platform.
- Cleaned and transformed the Online Retail dataset, removing invalid transactions and preparing processed datasets for analysis.
- Developed business analytics modules for revenue KPIs, monthly sales, top products, top countries and customer behavior.
- Implemented RFM scoring and KMeans clustering to segment customers and identify actionable customer groups.
- Built a Retrieval-Augmented Generation pipeline using ChromaDB, sentence-transformer embeddings and Mistral AI.
- Integrated LangFuse observability to trace LLM calls, inspect retrieved chunks and compare RAG quality.
- Exposed analytics and AI features through a FastAPI backend with endpoints for KPIs, segmentation and document chat.
- Created a Streamlit dashboard to make the project usable through a simple interface.
- Dockerized the backend and deployed it to Google Cloud Run using Artifact Registry.
- Loaded cleaned data into Cloud Storage and BigQuery and validated analytical SQL queries.
- Added initial unit tests with Pytest for KPI functions, analytical functions and FastAPI endpoints.

## LinkedIn Post Draft

I recently completed a portfolio project called Smart Retail AI Analyst.

The goal was to build an end-to-end data and AI system around an online retail dataset.

The project includes:

- data cleaning and preparation with Python and Pandas;
- retail KPI analysis;
- monthly sales analysis;
- top products and countries;
- RFM customer scoring;
- KMeans customer segmentation;
- FastAPI backend;
- Streamlit dashboard;
- RAG assistant with ChromaDB and Mistral AI;
- LangFuse tracing for LLM observability;
- Docker and Docker Compose;
- deployment on Google Cloud Run;
- Cloud Storage and BigQuery integration;
- initial unit tests with Pytest.

This project helped me connect several important skills: data analysis, machine learning, backend APIs, LLM applications, observability, containerization and cloud deployment.

The most interesting part was building and evaluating the RAG pipeline, then using LangFuse to compare retrieval quality and improve the prompt.

GitHub repo: https://github.com/la9ba3/smart-retail-ai-analyst

## Demo Script

### 1. Project Overview

This is Smart Retail AI Analyst, an end-to-end data and AI project based on the Online Retail dataset.

The goal is to transform raw transaction data into business insights and make those insights accessible through an API, a dashboard and an AI assistant.

### 2. Data Pipeline

First, the project loads and cleans the Online Retail dataset.

The cleaning removes missing customers, invalid quantities, invalid prices and cancelled invoices. It also creates a `TotalPrice` column.

### 3. Business Analytics

Then the project calculates key retail metrics:

- total revenue;
- number of invoices;
- number of customers;
- average basket value;
- top products;
- top countries;
- monthly revenue.

### 4. Customer Segmentation

The project applies RFM scoring to understand customer behavior using recency, frequency and monetary value.

It also applies KMeans clustering to group customers into behavioral segments.

### 5. API And Dashboard

The results are exposed through a FastAPI backend and can also be explored through a Streamlit dashboard.

The API includes endpoints such as `/health`, `/dataset-summary`, `/sales-kpis`, `/top-products`, `/top-countries`, `/rfm-segments` and `/chat-docs`.

### 6. RAG Assistant

The project includes a RAG assistant that can answer questions about the project documentation.

It uses Markdown documents, ChromaDB, sentence-transformer embeddings and Mistral AI.

LangFuse is used to trace the LLM calls and inspect retrieved sources.

### 7. Docker And Cloud

The backend is packaged with Docker and deployed on Google Cloud Run.

The cleaned dataset was also uploaded to Cloud Storage and loaded into BigQuery for SQL analysis.

### 8. Testing

Finally, I added initial Pytest tests for KPI calculations, analytical functions and FastAPI endpoints.

## Useful Screenshots To Capture

- GitHub repository homepage with the README.
- FastAPI Swagger page locally or on Cloud Run.
- `/health` endpoint response.
- `/dataset-summary` endpoint response.
- `/chat-docs` response with sources.
- Streamlit dashboard KPIs page.
- Streamlit RAG/chat page.
- LangFuse trace showing input, output, latency and sources.
- Docker Desktop showing the backend image/container.
- Cloud Run service page.
- BigQuery query result for revenue by country.
- Pytest terminal output.

## Strong Technical Points To Mention

- End-to-end project from raw data to cloud deployment.
- Clear data cleaning pipeline.
- Business-oriented KPI analysis.
- Customer segmentation with both RFM and KMeans.
- FastAPI backend with documented endpoints.
- RAG implementation with vector search and external LLM.
- LangFuse observability for LLM traces.
- Docker and Docker Compose setup.
- Cloud Run deployment with Artifact Registry.
- Cloud Storage and BigQuery integration.
- Unit tests with Pytest.
- Debugging of real issues such as Docker dependencies, `.env` formatting, Cloud Run memory limits and BigQuery schema issues.

## Possible Improvements To Mention

- Add API authentication for the public Cloud Run endpoint.
- Add GitHub Actions for automated testing.
- Improve Streamlit UI design.
- Use BigQuery as the production data source instead of local CSV files.
- Reduce Docker image size.
- Add integration tests.
- Add architecture diagrams.
- Record a short demo video.


# Version Française

## Pitch Court Du Projet

Smart Retail AI Analyst est un projet portfolio data et IA de bout en bout construit à partir du dataset Online Retail.

Le projet combine nettoyage de données, analyse retail, segmentation client RFM, clustering KMeans, FastAPI, Streamlit, RAG, Mistral AI, LangFuse, Docker et Google Cloud Platform.

Il transforme des transactions e-commerce brutes en insights business accessibles via une API, un dashboard et un assistant IA.

## Pitch Entretien En 30 Secondes

J'ai construit un projet data et IA de bout en bout autour d'un dataset e-commerce.

Le projet nettoie le dataset Online Retail, calcule des KPIs business, analyse les ventes par produit, pays et mois, puis segmente les clients avec la méthode RFM et le clustering KMeans.

J'ai exposé les résultats avec un backend FastAPI et une interface Streamlit. J'ai aussi construit un pipeline RAG avec ChromaDB, des embeddings sentence-transformers et Mistral AI, puis utilisé LangFuse pour tracer et analyser les appels LLM.

Enfin, j'ai dockerisé le backend, l'ai déployé sur Google Cloud Run, envoyé les données nettoyées vers Cloud Storage et BigQuery, et ajouté des premiers tests unitaires avec Pytest.

## Points Pour Le CV

- Construction d'un projet data et IA de bout en bout avec Python, Pandas, FastAPI, Streamlit et Google Cloud Platform.
- Nettoyage et transformation du dataset Online Retail avec suppression des transactions invalides.
- Développement de modules d'analyse business : KPIs, ventes mensuelles, top produits, top pays et comportement client.
- Implémentation du scoring RFM et du clustering KMeans pour segmenter les clients.
- Création d'un pipeline RAG avec ChromaDB, embeddings sentence-transformers et Mistral AI.
- Intégration de LangFuse pour tracer les appels LLM, inspecter les chunks récupérés et comparer la qualité du RAG.
- Exposition des analyses via une API FastAPI avec endpoints pour KPIs, segmentation et chat documentaire.
- Création d'un dashboard Streamlit pour rendre le projet utilisable via une interface simple.
- Dockerisation du backend et déploiement sur Google Cloud Run avec Artifact Registry.
- Chargement des données nettoyées dans Cloud Storage et BigQuery avec validation par requêtes SQL.
- Ajout de tests unitaires avec Pytest pour les fonctions KPI, les fonctions d'analyse et les endpoints FastAPI.

## Brouillon De Post LinkedIn

J'ai récemment terminé un projet portfolio appelé Smart Retail AI Analyst.

L'objectif était de construire un système data et IA de bout en bout autour d'un dataset e-commerce.

Le projet inclut :

- nettoyage et préparation des données avec Python et Pandas ;
- analyse des KPIs retail ;
- analyse des ventes mensuelles ;
- top produits et top pays ;
- scoring client RFM ;
- segmentation client avec KMeans ;
- backend FastAPI ;
- dashboard Streamlit ;
- assistant RAG avec ChromaDB et Mistral AI ;
- observabilité LLM avec LangFuse ;
- Docker et Docker Compose ;
- déploiement sur Google Cloud Run ;
- intégration Cloud Storage et BigQuery ;
- premiers tests unitaires avec Pytest.

Ce projet m'a permis de connecter plusieurs compétences importantes : analyse de données, machine learning, APIs backend, applications LLM, observabilité, containerisation et déploiement cloud.

La partie la plus intéressante a été la construction puis l'évaluation du pipeline RAG, avec LangFuse pour comparer la qualité de récupération documentaire et améliorer le prompt.

GitHub repo: https://github.com/la9ba3/smart-retail-ai-analyst

## Script De Démo

### 1. Présentation Du Projet

Voici Smart Retail AI Analyst, un projet data et IA de bout en bout basé sur le dataset Online Retail.

L'objectif est de transformer des données transactionnelles brutes en insights business, puis de les rendre accessibles via une API, un dashboard et un assistant IA.

### 2. Pipeline Data

Le projet commence par charger et nettoyer le dataset Online Retail.

Le nettoyage supprime les clients manquants, les quantités invalides, les prix invalides et les factures annulées. Il crée aussi une colonne `TotalPrice`.

### 3. Analyse Business

Ensuite, le projet calcule les principaux indicateurs retail :

- chiffre d'affaires total ;
- nombre de factures ;
- nombre de clients ;
- panier moyen ;
- meilleurs produits ;
- meilleurs pays ;
- chiffre d'affaires mensuel.

### 4. Segmentation Client

Le projet applique la méthode RFM pour comprendre le comportement client à partir de la récence, de la fréquence et du montant dépensé.

Il applique aussi KMeans pour regrouper les clients en segments comportementaux.

### 5. API Et Dashboard

Les résultats sont exposés avec un backend FastAPI et explorables via un dashboard Streamlit.

L'API contient des endpoints comme `/health`, `/dataset-summary`, `/sales-kpis`, `/top-products`, `/top-countries`, `/rfm-segments` et `/chat-docs`.

### 6. Assistant RAG

Le projet inclut un assistant RAG capable de répondre à des questions sur la documentation du projet.

Il utilise des documents Markdown, ChromaDB, des embeddings sentence-transformers et Mistral AI.

LangFuse permet de tracer les appels LLM et d'inspecter les sources récupérées.

### 7. Docker Et Cloud

Le backend est packagé avec Docker puis déployé sur Google Cloud Run.

Le dataset nettoyé a aussi été envoyé vers Cloud Storage et chargé dans BigQuery pour faire des analyses SQL.

### 8. Tests

Enfin, j'ai ajouté des premiers tests Pytest pour les calculs KPI, les fonctions d'analyse et les endpoints FastAPI.