# Smart Retail AI Analyst



Smart Retail AI Analyst est un projet portfolio construit étape par étape autour du dataset Online Retail.



L'objectif final est de créer un assistant IA capable d'analyser des ventes retail, de segmenter les clients, puis de proposer une API, une interface Streamlit et un module RAG.



## Objectifs du projet



- Charger et nettoyer le dataset Online Retail.

- Analyser les ventes, les clients, les produits et les pays.

- Construire un scoring RFM et une segmentation client.

- Exposer les résultats avec FastAPI.

- Créer une interface utilisateur avec Streamlit.

- Ajouter un module RAG sur des documents métier.

- Préparer le projet pour Docker et Google Cloud Platform.



## Structure du projet



```text

smart-retail-ai-analyst/

├── backend/

├── frontend/

├── notebooks/

├── src/

│   ├── data/

│   ├── analysis/

│   ├── ml/

│   └── rag/

├── data/

│   ├── raw/

│   ├── processed/

│   └── documents/

├── docs/

├── tests/

├── docker/

├── .env.example

├── .gitignore

├── README.md

└── requirements.txt

Dataset

Le dataset principal sera Online Retail, disponible sur le UCI Machine Learning Repository.
Les fichiers de données volumineux ne sont pas versionnés dans Git. Ils seront placés dans data/raw/ ou data/processed/ en local.