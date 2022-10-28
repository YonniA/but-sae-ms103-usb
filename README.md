# **Configuration d'un poste de travaille sous Linux**  
---  
| <center>Sommaire</center> |
| :----- |
| [Création de deux utilisateurs](#les-utilisateurs-andr0134-et-admin) |
| [Installation des outils Python](#les-installations-sur-la-machine-virtuelle) |

---

## **Les utilisateurs andr0134 et admin**  
Création d'un identifiant à partir de la commande ` adduser --UID 30591 --GID 100 --home /home/andr0134 andr0134` et affectation directe à l'UID, le GID et le répertoire d'accueil demandé.  

Création d'un identifiant administrateur à partir de la commande `sudo adduser --UID 63975 --GID 100 --home /home/administrateur admin` et affection directe à l'UID, le GID et le répertoire d'accueil demandé. (à noter que pour créer un utilisateur avec des droits d'administration, il faut utiliser la commande sudo).  
Pour ajouter l'utilisateur au groupe secondaire sudo, on fait la commande `sudo addgroup admin sudo`

---

## **Les installations sur la machine virtuelle**  
* Python, ses outils et bibliothèques
  * pip : `sudo apt install python3-pip` , pip permet l'installation et la vérification facile d'outils python
  * black : `pip install black` , black sert à réorganiser un fichier python, par exemple si il y a des espaces en trop, l'utilisation de black enlèvera ces espaces inutiles
  * blue : `pip install blue` , blue est globalement la même chose que black, à la différence que lui utilise de simples guillements pour les chaines de caractères et blue à également plus d'extensions disponibles comme :
    * pyproject.toml
    * setup.cfg
    * tox.ini
    * .blue
  * flake8 : `pip install flake8` , flake8 permet la localisation des erreurs dans un fichier python
  * bandit : `pip install bandit` , bandit fait la même chose que flake9
  * mypy : `pip install mypy` , mypy détecte également les erreurs dans un fichier python, mais cette fois-ci ce sont les erreurs de syntaxe
  * docformatter : `pip install docformatter` , docformatter formatte automatiquement les docstrings selon la convention  PEP 257
  * pytest : `pip install pytest` , pytest sert à détailler les tests python pour vérifier si une fonction fonctionne
  * pygame : `pip install pygame` , pygame est une bibliothèque python permettant la création de jeux-vidéos
* Git étant déjà installé de base, son installation n'a pas été requise
* Meld : `sudo apt install meld` , meld est un outil de comparaison et de fusion  

---
## **Bibliographie et sitographie**
* Ysabeau, Python - [Formateur de code, analyse statique](https://linuxfr.org/news/python-partie-9-formateur-de-code-analyse-statique)
* [Documentation Ubuntu](https://doc.ubuntu-fr.org/)


