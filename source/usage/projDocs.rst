*********************
Project Documentation
*********************

Installing Python Sphinx
========================

Python Sphinx_ is a tool that helps build documentation out of reStructured Text (rst)
marked-up files.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/

You must have Python installed (we recommend `Python 3.x <https://www.python.org/downloads/>`_).

Once Python is installed, you should have the ``pip`` utility installed natively (if not, `go here <https://pip.pypa.io/en/stable/installing/>`_). To check if you have ``pip``:

.. code-block:: bash

   $ python -m pip --version
   pip 9.0.1 from C:\...\Python\Python36-32\lib\site-packages (python 3.6)

Once you checked ``pip`` is installed, run the command to install Sphinx:

.. code-block:: bash

   $ python -m pip install Sphinx

We will also need the ``sphinx_rtd_theme`` for our docs:

   $ python -m pip install sphinx_rtd_theme

Setup
=====

.. note::

   This should have been a one-time process setup by the administrator, and is only
   here for record keeping purposes. If you're reading this, it's setup.

All documentation related files are stored in the repository: ``CloudSevenConsulting.github.io``.
There are 2 branches of concern;

  - ``master``, which contains the built ``.HTML`` files as served on Github
  - ``src``, which contains the the source ``.rst`` files required for building
  - ``doxy``, which contains the DOxygen generated output; hopefully we don't push this up all the time, this is just there to get you started - we will rely on the actual DOxygen build

1. We first make our ``src`` repo

  .. code-block:: bash

      $ mkdir CloudSevenConsulting.github.io
      $ cd CloudSevenConsulting.github.io
      $ git init .
      $ git checkout --orphan src
      $ echo 'build/' > .gitignore            # this will host the master branch

2. Setup your Sphinx project

  .. code-block:: bash

      $ sphinx-quickstart.exe

      # press [enter] to all options
      # EXCEPT:
      #   - we want the ``build/`` and ``source/`` directories to be separate.
      #   - we want MathJAX

      $ git add --all
      $ git commit -m "init src"

2. Write and Build with ``make html`` (see building below)

4. Now we set up the ``git`` repo for the ``master`` branch

  .. code-block:: bash

      $ cd build/html
      $ touch .nojekyll       # This file is crucial for serving on Github
      $ git init .
      $ git add --all
      $ git commit -m "init"

New Contributors
================

1. First clone the ``src`` branch

  .. code-block:: bash

      $ git clone https://github.com/CloudSevenConsulting/CloudSevenConsulting.github.io.git
      $ cd CloudSevenConsulting.github.io
      $ git checkout src

2. Now clone in the ``master`` branch

  .. code-block:: bash

      $ mkdir build/
      $ cd build/
      $ git clone https://github.com/CloudSevenConsulting/CloudSevenConsulting.github.io.git html

3. Clone in your ``doxy`` branch

   .. code-block:: bash

       $ cd ../
       $ git clone https://github.com/CloudSevenConsulting/CloudSevenConsulting.github.io.git doxy
       $ cd doxy
       $ git checkout doxy

Building
========

Because of the way the branch ``gh-pages`` is set-up, a funny build process is required.

.. note::

   Team to consider automating this with Python tool

1. Make your modifications in the ``src`` branch (you shouldn't need to use the ``git checkout`` command at all, just ``cd``).

2. If the indexes in your build must change (i.e. new files added/files moved) then a clean is required before build

    a) **Do not** use ``make clean``, as this will remove the ``.git`` files.

    b) Manually remove all build files (everything in ``build/html`` excluding the hidden ``.git`` directory)
    c) Build the ``DOxygen`` ``xml``

    Alternatively you can use the script ``CleanBuild.py``

      .. code-block:: bash

          $ python CleanBuild.py

3. Commit your source changes & build

     .. code-block:: bash

         $ git add --all
         $ git commit -m "Update source..."
         $ git push origin src
         $ make html

  Alternatively, use:

    .. code-block:: bash

        $ python BuildDoc.py

  This does not clean, so make sure you do that!

4. Commit your changes

     .. code-block:: bash

         $ cd build/html/
         $ git add --all
         $ git commit -m "docs"   # who cares about commit messages here
         # git push origin master
