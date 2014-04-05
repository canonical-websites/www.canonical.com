Setup
===

This site depends on [Fenchurch](https://bitbucket.org/nottrobin/fenchurch) - which is currently a private repository. Make sure you have SSH access to the above repository before attempting to install dependencies.

To prepare the site:

``` bash
git submodule update --init # Check out fenchurch package
pip install -r requirements.txt # Install packages to environment
./manage.py syncdb # setup local database
```

Run
===

To run the local development server:

``` bash
./manage.py runserver
```

Now visit <http://127.0.0.1:8000>
