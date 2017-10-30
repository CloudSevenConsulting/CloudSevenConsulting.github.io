*************************
Deploying the Sensor Host
*************************

Setup
=====

1. The code base must first be downloaded from the ``git`` repository

.. code-block:: bash

   $ git clone https://github.com/CloudSevenConsulting/DustyDuinoPro.git
   $ cd DustyDuinoPro/

2. With Atmel Studio 7 (as setup in :ref:`idx-usage-dev-as7`), open the project solution file (``.atsln``) in
the repository.

Configuring the Build
=====================

The build may be configured through several preprocessor ``#defines`` which conditionally include
certain portions of the code-base.

For a production build (i.e. usual deployment) the ``DP_BUILD__TEST_MODE`` must be set to ``0``.

In ``main.cpp``:

.. code-block:: c

    /*******************************************************************************
     * Build settings
     ******************************************************************************/
    #define DP_BUILD__TEST_MODE 0               // <--- Set this to zero for production
    #define DP_BUILD__UART_USB_MODE 0

Test Builds
-----------

With ``DP_BUILD__TEST_MODE``, the system will build into its 'test mode' in which
unit tests will be run.

Test control (``TCTRL``) flags can be modified to selectively chose tests to be
performed, where ``TCTRL`` of ``1`` indicates the test will be run.

In ``tester.h``:

.. code-block:: c

    #define DP_BUILD__TCTRL_DNJOIN 0                // 0 = Ignore test case
    #define DP_BUILD__TCTRL_DPUART 1                // 1 = Run test case
    #define DP_BUILD__TCTRL_DPSYS 1
    #define DP_BUILD__TCTRL_DPFRAMING 1
    #define DP_BUILD__TCTRL_DPSAMPLE 1
    #define DP_BUILD__TCTRL_DPSAMPLE_DIAG 1
    #define DP_BUILD__TCTRL_DPSAMPLE_TIME 1
    #define DP_BUILD__TCTRL_DPSAMPLE_SENS 1
    #define DP_BUILD__TCTRL_PORT 1

Build
=====

The system is ready to be built; first compile the object and then export the ``.hex``
with the tool described in :ref:`idx-usage-dev-as7`
