# AdVConnect
<h1>Django based Advertisement creator</h1>
<h2>How to deploy this project</h2>
<p>To run locally, do the usual:

#. Create a Python 3.6 virtualenv

# Create a django environment

#. Make a directory to store the project's data (MEDIA_ROOT, DOC_BUILDS_ROOT,
   etc.). We'll use ~/.djangoproject for example purposes.

   Create a 'secrets.json' file in a directory named 'conf' in that directory,
   containing something like::

    { "secret_key": "xyz",
      "superfeedr_creds": ["any@email.com", "some_string"],
      "db_host": "localhost",
      "db_password": "secret",
      "trac_db_host": "localhost",
      "trac_db_password": "secret" }

#. Add `export DJANGOPROJECT_DATA_DIR=~/.djangoproject` (without the backticks)
   to your ~/.bashrc (or ~/.zshrc if you're using zsh, ~/.bash_profile if
   you're on macOS and using bash) file and then run `source ~/.bashrc` (or
   `source ~/.zshrc`, or `source ~/.bash_profile`) to load the changes.

#. Create databases::

    createuser -d djangoproject --superuser
    createdb -O djangoproject djangoproject
    createuser -d code.djangoproject --superuser
    createdb -O code.djangoproject code.djangoproject

#. Setting up database access

   If you are using the default postgres configuration, chances are you will
   have to give a password for the newly created users to be able to
   use them for Django::

     psql
     ALTER USER djangoproject WITH PASSWORD 'secret';
     ALTER USER "code.djangoproject" WITH PASSWORD 'secret';
     \d

   (Use the same passwords as the ones you've used in your `secrets.json` file)

#. Create tables::

    psql -d code.djangoproject < tracdb/trac.sql

    ./manage.py migrate

#. Create a superuser::

   ./manage.py createsuperuser

#. Populate the www and docs hostnames in the django.contrib.sites app::

    ./manage.py loaddata dev_sites

#. Point the ``www.djangoproject.localhost``, ``docs.djangoproject.localhost``,
   and ``dashboard.djangoproject.localhost`` hostnames with your ``/etc/hosts``
   file to ``localhost``/``127.0.0.1`` by adding::

     127.0.0.1 docs.djangoproject.localhost www.djangoproject.localhost dashboard.djangoproject.localhost

   This is unnecessary with some browsers (e.g. Opera and Chromium/Chrome) as
   they handle localhost subdomains automatically.

   If you're on macOS and don't feel like editing the ``/etc/hosts`` file
   manually, there is a great preference pane called `Hosts.prefpane`_. On
   Ubuntu, there is a `built-in network admin`_ GUI to do the same. Remember
   both require admin privileges, just like you'd need when editing
   ``/etc/hosts`` with your favorite editor.

   If you don't have admin rights but have an internet connection, you can use a
   service like `xip.io <http://xip.io>`_. In that case, you'll also have to
   update `ALLOWED_HOSTS` in `djangoproject/settings/dev.py` as well as the
   content of the `django_site` table in your database.
  
#. Finally, run the server::

    make run

   This runs both the main site ("www") as well as the
   docs and dashboard site in the same process.
   Open http://www.djangoproject.localhost:8000/,
   http://docs.djangoproject.localhost:8000/,
   or http://dashboard.djangoproject.localhost:8000/.
</p>
<h1> Working of the Project go to the link</h1>
  Open http://ishagoel1603.pythonanywhere.com/
 <h2> To Login </h2>
 <p>You can login with github or facebook or locally. For local login</p>
  <p>user- user
  password-user1234</p>
  <h3>UML and ER daigrams are in it</h3>  
