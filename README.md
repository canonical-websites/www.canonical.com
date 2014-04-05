Setup
===

To prepare the site:

``` bash
git submodule update --init # Check out fenchurch package
pip install -r requirements.txt # Install packages to environment
./manage syncdb # setup local database
```

Run the development server
===

To run the local development server:

``` bash
./manage runserver
```

Now visit <http://127.0.0.1:8000>
