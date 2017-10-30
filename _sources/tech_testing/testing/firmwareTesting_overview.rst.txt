*************************
Firmware Testing Overview
*************************

Testing is performed with a separate build from the production build.

Selecting the build mode is done in software source code.

Building Test Mode
==================

In ``main.c`` the following code enables Test mode.

.. code-block:: c

    /*******************************************************************************
     * Build settings
     ******************************************************************************/
    #define DP_BUILD__TEST_MODE 0


The **pre-processor** macro ``DP_BUILD__TEST_MODE`` is a boolean which is checked in source
code. If it is set, then the compiler will only build the test mode code.
If instead ``TEST_MODE`` is zero, then the compiler will build into production

Testing Configuration
---------------------

Certain tests can be enabled or disabled in ``tester.h``

.. code-block:: c

   /* ****************************************************************************
    * Test Selection
    * ***************************************************************************/
   #define DP_BUILD__TCTRL_DNJOIN 0
   #define DP_BUILD__TCTRL_DPUART 0
   #define DP_BUILD__TCTRL_DPSYS 1
   #define DP_BUILD__TCTRL_DPFRAMING 1
   #define DP_BUILD__TCTRL_DPSAMPLE 1
   #define DP_BUILD__TCTRL_DPSAMPLE_DIAG 1
   #define DP_BUILD__TCTRL_DPSAMPLE_TIME 1
   #define DP_BUILD__TCTRL_DPSAMPLE_SENS 1
   #define DP_BUILD__TCTRL_PORT 1

As seen in the code-block above, similar macros are defined to enable or disable
certain tests. When the macros are set to 1, then the compiler will build the
relevant test functions and then run them. If the macros are set to 0, no build
will occur for the tests in question.
