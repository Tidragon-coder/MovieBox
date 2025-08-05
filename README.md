# 🎬 MovieBox

MovieBox est une application web développée avec Django permettant de gérer une collection de films.  
L'utilisateur peut ajouter, modifier et consulter des films, avec des notes, commentaires, images et informations associées.

---

## 🚀 Fonctionnalités

- 📄 Liste des films ajoutés (triée du plus récent au plus ancien)
- ➕ Ajout de nouveaux films (titre, année, genre, image, note, commentaire)
- ✏️ Modification des films existants
- ⭐ Moyenne automatique des notes affichée en haut de la page

---

## 🛠️ Technologies

- Python 3.13
- Django 5.2.4
- HTML / CSS
- SQLite (base de données par défaut)
- Bootstrap ou CSS personnalisé

---

## 📁 Structure du projet

moviebox/
│
├── films/
│ ├── migrations/
│ ├── templates/
│ │ └── films/
│ │ ├── film_list.html
│ │ ├── film_add.html
│ │ └── film_update.html
│ ├── static/
│ │ └── films/
│ │ ├── style.css
│ │ ├── film_add.css
│ │ └── film_update.css
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── moviebox/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-pseudo/moviebox.git
cd moviebox
2. Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
Si requirements.txt est manquant, installe Django manuellement :
pip install django

4. Lancer le projet
python manage.py migrate
python manage.py runserver

5. Accéder à l'application
🔗 Ouvre ton navigateur sur http://127.0.0.1:8000



