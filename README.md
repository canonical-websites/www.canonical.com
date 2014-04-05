Setup
===

To prepare the site:

``` bash
pip install -r requirements.txt # Install dependencies
./manage.py syncdb # Create local database
```

Fenchurch
---

This site depends on [Fenchurch](https://bitbucket.org/nottrobin/fenchurch) - which is currently a private repository. Make sure you have SSH access to the above repository before attempting to install dependencies.

Run
===

To run the local development server:

``` bash
./manage.py runserver
```

Now visit <http://127.0.0.1:8000>
