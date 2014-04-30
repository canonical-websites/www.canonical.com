Setup
===

To prepare the site:

``` bash
make setup # Install ruby and python dependencies
```

Fenchurch
---

This site depends on [Fenchurch](https://bitbucket.org/nottrobin/fenchurch) - which is currently a private repository. Make sure you have SSH access to the above repository before attempting to install dependencies.

Run
===

To run the local development server:

``` bash
# source the virtualenv
source env/bin/activate

# Run sass compiler and the server
make 

#...

# Deactivate virtualenv when finished
deactivate
```

Now visit <http://127.0.0.1:8000>
