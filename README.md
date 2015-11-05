# flask-boilerplate

A convenient development framework to get up and running fast with Flask. Comes configured with **Flask-SQLAlchemy**, **Flask-WTF**, and **Bootstrap**.

<hr>

Project Structure
--------

  ```
  ├── README.md
  ├── notes.txt
  ├── project
  │   ├── app
  │   │   ├── __init__.py
  │   │   ├── email.py
  │   │   ├── main
  │   │   │   ├── __init__.py
  │   │   │   ├── errors.py
  │   │   │   ├── forms.py
  │   │   │   ├── views.py
  │   │   ├── models.py
  │   │   ├── static
  │   │   │   ├── css
  │   │   │   │   └── base.css
  │   │   │   ├── img
  │   │   │   ├── js
  │   │   │   │   └── base.js
  │   │   │   └── libs
  │   │   │       ├── bootstrap
  │   │   │       └── jquery
  │   │   └── templates
  │   │       ├── base_layout.html
  │   │       ├── error
  │   │       │   ├── 404.html
  │   │       │   └── 500.html
  │   │       └── main
  │   │           └── index.html
  ├── config.py
  ├── instance
  │   └── config.py
  ├── manage.py
  └── requirements.txt
  ```
