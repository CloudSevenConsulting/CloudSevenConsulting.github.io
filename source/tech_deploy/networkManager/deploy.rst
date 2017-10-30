*****************************
Deploying the Network Manager
*****************************

Required Software
=================

- Python 2.7.x

    + Python ``pip`` utility

- Git
- AWS CLI

Setup
=====

1. We will store all our Network Manager related software in a ``NetworkManager/`` directory. Note you can store this wherever you like (or name it whatever you like)

    .. code-block:: bash

        $ cd ~/Downloads        #temporary storage, choose where you want this to be
        $ mkdir NetworkManager

2. Clone the DustyPyManager repository with Git

    .. code-block:: bash

        $ cd ~/Downloads/NetworkManager/
        $ git clone https://github.com/CloudSevenConsulting/DustyPyManager.git

3. Install the required Python packages with your ``pip`` utility;

    .. code-block:: bash

        $ cd DustyPyManager
        $ python -m pip install -r requirements.txt

4. Install the SmartMesh SDK for Python

    Download the ``smartmesh-sdk`` from `DustCloud Github`_ and extract it into ``NetworkManager/``

    .. code-block:: bash

       $ cd ~/Downloads/NetworkManager/smartmeshsdk-master    # I.e. to the parent folder of the downloaded item
       $ py -2 setup.py install
       $ py -2 -m pip install -r requirements.txt
    .. _DustCloud Github: https://github.com/dustcloud/smartmeshsdk

5. Configure your AWS CLI environment

    .. code-block:: bash

        $ aws configure

Test
====

To test that everything is functional, connect the ``DC2274A-A`` device to your
computer and run the tests

.. code-block:: bash

   $ cd NetworkManager/DustyPyManager

   $ py -2 -m DustyPyManager.tests.runner
