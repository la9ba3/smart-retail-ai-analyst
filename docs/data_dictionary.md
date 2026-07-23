# Data Dictionary - Online Retail



Ce document explique les colonnes du dataset Online Retail.



## Vue d'ensemble



Le dataset Online Retail contient des transactions de vente d'une entreprise retail en ligne. Chaque ligne représente une ligne de facture, c'est-à-dire un produit vendu dans une commande.



## Colonnes



| Colonne | Type observé | Description | Exemple | Remarque |

|---|---|---|---|---|

| InvoiceNo | Texte | Numéro de facture ou de commande. | 536365 | Si le numéro commence par `C`, il s'agit d'une annulation. |

| StockCode | Texte | Code unique du produit. | 85123A | Permet d'identifier les produits. |

| Description | Texte | Nom ou description du produit. | WHITE HANGING HEART T-LIGHT HOLDER | Peut contenir des valeurs manquantes. |

| Quantity | Nombre entier | Quantité achetée pour ce produit dans la facture. | 6 | Une quantité négative peut indiquer une annulation ou un retour. |

| InvoiceDate | Date/texte | Date et heure de la transaction. | 2010-12-01 08:26:00 | À convertir en vrai format date pendant le nettoyage. |

| UnitPrice | Nombre décimal | Prix unitaire du produit. | 2.55 | Les prix à 0 ou négatifs devront être vérifiés. |

| CustomerID | Nombre décimal | Identifiant du client. | 17850.0 | Peut contenir des valeurs manquantes. Utile pour l'analyse client. |

| Country | Texte | Pays du client. | United Kingdom | Utile pour l'analyse géographique des ventes. |



## Observations importantes



- `InvoiceNo` peut indiquer une annulation si la valeur commence par `C`.

- `CustomerID` contient des valeurs manquantes.

- `Description` peut contenir des valeurs manquantes.

- `InvoiceDate` devra être convertie en date.

- `Quantity` et `UnitPrice` devront être contrôlées avant les analyses.



## À retenir



Avant d'analyser un dataset, il faut comprendre ce que signifie chaque colonne. Cela évite de faire des calculs faux ou d'interpréter les résultats trop vite.

