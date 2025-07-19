# BruteForceWebPopUpBase64

> **Avertissement légal** Utilisez ces scripts uniquement sur des cibles que vous possédez ou pour lesquelles vous avez une autorisation écrite. L’attaque non autorisée de systèmes informatiques est illégale.

---

## Présentation

Ces scripts Python ont pour but de réaliser du bruteforce sur une pop up web de connexion avec un username et un password encodé en base64 de la forme username:password :
* genBase64cred.py génère une liste de username:password encodé en base64 avec le username fixé et le password qui couvre l'ensemble des combinaisons possibles pour une longueur donnée ;
* bruteForceWebPopUp.py réalise l'attaque bruteforce sur une pop up web de connexion ;

---

## Prérequis

| Outil / Librairie | Version conseillée |
| ----------------- | ------------------ |
| **Python**        | 3.8+               |
| **requests**      | >=2.31             |
| **termcolor**     | >=2.4              |


Installation rapide:

```bash
python -m venv venv
source venv/bin/activate        # sous Windows : venv\Scripts\activate
pip install requests termcolor
```

(ou)

```bash
pip install -r requirements.txt
```

---

## Utilisation

```bash
python genBase64cred.py <username> <longueur_attendue>
python bruteForceWebPopUp.py https://example.com/login <username> enumBase64Cred.txt <nb_thread>
```

Exemple:

```bash
python genBase64cred.py admin 7
python bruteForceWebPopUp.py https://example.com/login admin enumBase64Cred.txt 30
```

---

## License

Ce projet est publié sous une licence MIT.

---

## Author

**Corentin Mahieu** – [@Fir3n0x](https://github.com/Fir3n0x)
