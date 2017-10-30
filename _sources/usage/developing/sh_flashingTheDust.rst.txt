*************************
Flashing The Dusty Module
*************************

The complete guide can be found at `Linear Technology ESP Guide <https://cds.linear.com/docs/en/software-and-simulation/Eterna_Serial_Programmer_Guide.pdf>`_ (ETERNA01).

.. _idx-usage-dev-flash:

Required Software
=================

All software from `Linear Technology ESP <http://www.linear.com/solutions/4260>`_ (ETERNA04) is required (exclusing FTDI drivers if you have a normal
laptop...)


Backing-Up the Existing Flash
=============================

.. warning::

   Flashing the Dusty module will overwrite the existing flash. Back up the existing
   flash in case things go wrong!

First a backup of the existing Flash should be created with the following command

.. code-block:: bash

    $ ESP.exe -r IPM_Flash_01_Orig.bin

            ESP, Eterna SPI Programmer, version 1.1.1-6
            cfg.devName = Auto, type = 0, flashID = 0x1f24, locID = 0x0, spiClkHz = 3000000
            FTCSPI.dll = 2.1.2.2
            INFO: clkHz set to 3000000
            Open ok, flash emulation mode enabled, devName = Dust Interface Board B
            Read: fileName = IPM_Flash_01_Orig.bin, offset = 0, len = 524288
            ................

            setup = 1843 ms, dt = 1625 ms
            ESP exiting: tries remaining = 0, err = 0

Check to see that the file was

.. code-block:: bash

    $ ls

            Directory: ..\Eterna-Serial-Programmer\esp_1.1.1.6


            Mode                LastWriteTime         Length Name
            ----                -------------         ------ ----
            ------       2015-03-28     12:55         101376 ESP.exe
            ------       2015-03-28     12:55         102400 ftcspi.dll
            -a----       2017-09-29     18:27         524288 IPM_Flash_01_Orig.bin

Flashing the Whole Image
========================

4 image components are required to flash the whole image

=================  =====================
Image Component    Start Address (Hex)
=================  =====================
Fuse Table         0
Partition Table    800
Main Executable    1000
Load               77800
=================  =====================

Each component is flashed onto the Dusty module with the command

.. code-block:: bash

    $ ESP.exe -P [Image] [Start Hex-Addr]

Thus, with these items located in the current directory:

.. code-block:: bash

    $ ESP.exe -P FuseTable.bin 0
    $ ESP.exe -P PartitionTable.bin 800
    $ ESP.exe -P Main.bin 1000
    $ ESP.exe -P Loader.bin 77800

