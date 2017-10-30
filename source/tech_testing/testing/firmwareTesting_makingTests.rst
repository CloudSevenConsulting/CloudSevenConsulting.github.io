************
Making Tests
************

To make a set of tests, 3 files must be modified/created:

- A separate ``.cpp`` file must be created in ``Testing\``
- A corresponding ``.h`` file must be created in ``Testing\``
- ``tester.c`` must be modified to include the testing

Ideally, each ``.cpp`` file should correspond to the testing for one logical
grouping of peripherals/resources/types of tests. However no strict guidelines
are in place and is *ad-hoc*.

Creating the ``.cpp`` file
==========================

The ``.cpp`` file contains the functions for testing. Each file contains one
`cpp` class inherited from the base class ``Testing/TestCase.cpp``.

Importantly, every ``TestCase`` must override the virtual method ``run()``, in
which the ``tester.cpp`` will call.

.. note::

   Currently, the ``tester`` must manually call this ``.run()`` method. However future
   versions can investigate automating the test suite by using interfaces and dynamic
   class instantiating.

It is recommended that the ``.run()`` method is only a wrapper of potentially several
methods which contain the tests.

Every test method should use the standardised ``.t_fail()`` and ``.t_pass()`` inherited
from the parent class ``TestCase`` as a standardised means for interpreting test results.

.. note::

   Developer will need to modify this methods to suit their needs


Creating the ``.h`` file
========================

The ``.h`` file is a regular header file with an header include guard. This is where the
class should be defined for the ``TestCase``.

As an example:

.. code-block:: c

    #ifndef TESTDPSYS_H_
    #define TESTDPSYS_H_

    #include "TestCase.h"

    class TestDpSys: public TestCase {

        private:

        protected:

        public:
            TestDpSys(void);
            void run(void);
            void TU_SH_DpSys_FlashBlink_Op(void);   // A test function

            # ...
    };

    #endif /* TESTDPSYS_H_ */


Modifying ``tester``
=====================

One modification must be made in ``tester.h``:
- Create a new macro for testing selection

Two modifications must be made in ``tester.cpp`` for a new test:

- Include the ``.h`` file for the test in question (with the necessary conditional build statements)
- Call the testing functions in the ``do_system_test()`` routine, handling the test outcome accordingly (and with the necessary conditional build statements)


Macro for Test Selection
------------------------

The macro for test selection must be defined in ``tester.h`` as follows (for example,
let's say we are testing 'a new thing');

.. code-block:: c

   /* ****************************************************************************
    * Test Selection
    * ***************************************************************************/

    # ..

    #define DP_BUILD__TCTRL_DPSAMPLE_SENS 1
    #define DP_BUILD__TCTRL_PORT 1


   /* ... */

   #define TEST_NEWTHING_ENABLE 1    /*<-- our new macro*/

Include Testing Header
----------------------

The header must be included in ``tester.cpp`` **if the corresponding macro is set to 1**.
This is done in the ``Test Headers`` section of the source code as follows (for example,
let's say our header was ``test_newthing.h``)

.. code-block:: c

   /* ****************************************************************************
    * Test Headers
    * ***************************************************************************/
   #if DP_BUILD__TCTRL_PORT
        #include "test_smb.h"
   #endif

   /* ... */

   #if TEST_NEWTHING_ENABLE         /*<-- our new test*/
        #include "test_newthing.h"
   #endif

Calling the Test Functions
--------------------------

Finally, the ``do_system_test()`` routine must call the relevant test functions
from ``test_newthing.c`` (our example).

Note, that the available testing functions for reporting (in this case ``TestFail()``) may
change.

.. code-block:: c

    void do_system_test(void)
    {

    /*-----------------------------------*/
    #if DP_BUILD__TCTRL_DPSYS
        TestDpSys test_dp_sys;
        test_dp_sys.run();
    #endif

    /*-----------------------------------*/
    #if TEST_NEWTHING_ENABLE
        TestNewThing test_new_thing;
        test_new_thing.run();
    #endif

    }
