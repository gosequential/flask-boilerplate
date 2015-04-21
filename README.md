# flask-boilerplate

A convenient framework to get up and running fast with Flask. Comes configured with **Flask-SQLAlchemy**, **Flask-WTF**, and **Bootstrap**.

<hr>

Project Structure
--------

  ```
  ├── README.md
  ├── notes.txt
  ├── project
      ├── app.py
      ├── config.py
      ├── models.py
      ├── requirements.txt
      ├── static
      │   ├── css
      │   │   ├── bootstrap-3.0.0.min.css
      │   │   ├── base.css
      │   └── js
      │       ├── libs
      │       │   ├── bootstrap-3.0.0.min.js
      │       │   ├── jquery-1.10.2.min.js
      │       └── base.js
      └── templates
          ├── errors
          │   ├── 404.html
          │   └── 500.html
          ├── forms
          │   ├── forgot.html
          │   ├── login.html
          │   └── register.html
          ├── layouts
          │   ├── form.html
          │   └── main.html
          └── pages
              ├── placeholder.about.html
              └── placeholder.home.html
  ```