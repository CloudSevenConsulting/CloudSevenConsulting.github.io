*******************
Sensor Host Modules
*******************

Each module should be encapsulated into folder for good organization of code

The current existing modules are

=====================  ================================================  ==============================================================
Module                 Layer                                             Purpose
=====================  ================================================  ==============================================================
``sys``                System Core                                       Core system functions
``sm_clib``            Network                                           Core ``C`` functions for SmartMesh-IP protocol
``sm_qsl``             Network                                           API for Dusty communication
``Testing``            Application                                       Testing framework
``sample``             Application                                       Functions pertaining to process variable and memory handling
``usart``              Network                                           Programming interface between the ``qsl`` and duinoPRO
=====================  ================================================  ==============================================================

Adding Modules
==============

1. To add a module, a new folder **must** be created through Atmel Studio 7. This ensures the ``.cpproj`` file
is updated, and the ``Makefile`` builds the entire solution correctly.

2. The header files from this module must then be included in the main entry point ``main/main.cpp``

.. code-block:: c

    /*******************************************************************************
     * Core
     ******************************************************************************/
    #include "port.h"
    #include "dp_sm.h"
    #include "dp_conf.h"
    #include "sample/sensor.h"

    // ...

    extern "C" {
        #include "sm_qsl/dn_qsl_api.h"
    };


If the module is ``.c`` based module, then use the ``extern`` key word.

3. The initialisation of the module must occur in the ``setup()`` routine.

.. code-block:: c

    void setup()
    {

        // initialise
    }

Note that if initialisation of the module **should not** occur in testing builds,
wrap the initialisation in a preprocessor conditional build.

For example:

.. code-block:: c

     #if !DP_BUILD__TEST_MODE
        port_init();
        dn_qsl_init();
     #endif
