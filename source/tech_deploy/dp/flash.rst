*************************
Flashing the Dusty Module
*************************

Please see section: Project-HowTo's/:ref:`idx-usage-dev-flash` for the full guide.

Setup
=====

.. warning::

    The Dusty module must not be connected to anything during this process.

1. Make a backup of the current image loaded on the Dusty Module:

.. code-block:: bash

   $ ESP.exe -r IPM_A01_flash.bin

2. Download the Flash images from the ``git`` repository

.. code-block:: bash

    $ git clone https://github.com/CloudSevenConsulting/DustyFlash.git

3. Navigate to the latest release (in this case ``IPM_B03``)

.. note::

   All ``IPM_B`` are currently being withheld from release due to confidentiality
   issues. Please contact Cloud Seven Consulting (``cloudsevenconsulting@gmail``) for
   more information.

.. code-block:: bash

    $ cd DustyFlash/IPM_Release_B03/

4. Flash the image

.. code-block:: bash

    $ ESP.exe -P IPM_B03_Fuse.bin 0                 # Fuse Table
    $ ESP.exe -P mote_part_r52074.bin 800           # Partition Table
    $ ESP.exe -P mote_ip_1_4_1_8_oski.bin 1000      # Main Executable
    $ ESP.exe -P loader_1_0_6_4_oski.bin 77800      # Loader
