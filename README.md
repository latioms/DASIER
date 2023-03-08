# DASIER
## Description
Le projet est de type MLOps, une architecture python permettant de construire différents modèles de machine learning, de les remplacer et de les déployer sur un serveur. Les modèles sont stockés sur un serveur disponible depuis des requêtes API. Une application web est également disponible pour les interactions avec les clients.

## Fontionalites
Le projet MLOps dispose des fonctionnalités suivantes :

Construction de modèles de Machine Learning à l'aide de Python.
Intégration continue : chaque push sur une branche du projet déclenche une série de tests pour vérifier que le code est toujours fonctionnel.
Déploiement des modèles de Machine Learning : lorsqu'un modèle est mis à jour, la nouvelle version est automatiquement déployée sur un serveur et est disponible via une API.
Stockage des modèles de Machine Learning : les modèles sont stockés sur un serveur et sont disponibles pour les requêtes via une API.
Application web pour interagir avec les clients : une application web permet aux clients d'interagir avec les modèles de Machine Learning via une interface utilisateur.

## Architecture
Le projet MLOps est basé sur une architecture Python qui utilise plusieurs librairies populaires pour la construction, le déploiement et l'utilisation de modèles de Machine Learning. Les principales librairies utilisées sont :

Scikit-learn : une librairie pour le développement de modèles de Machine Learning en Python.
Flask : un framework Python pour la création d'applications web.
Docker : une plateforme de conteneurisation pour le développement et le déploiement d'applications.

L'architecture du projet MLOps est la suivante :

- Construction du modèle : un modèle de Machine Learning est construit à l'aide de Scikit-learn.
- Tests et intégration continue : chaque push sur une branche du projet déclenche une série de tests pour vérifier que le code est toujours fonctionnel.
- Déploiement : lorsqu'un modèle est mis à jour, la nouvelle version est automatiquement déployée sur un serveur Docker.
- API : le serveur Docker expose une API permettant d'accéder aux modèles de Machine Learning.
- Application web : une application web est créée à l'aide de Flask pour interagir avec les clients.
