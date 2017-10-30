*************
System Timing
*************

System timing for the sensor-host is managed in the ``sm_qsl/dn_time`` module (as of release 0.6a).

In particular the functions ``uint32_t dn_time_ms(void)`` and ``void dn_sleep_ms(uint32_t milliseconds)``
are crucial in time management for the Dusty-to-DuinoPRO communication

Advanced sleeping functions should be incorporated here if future developers wish to improve
the system performance

Watchdog
========

CSC has **not** implemented a watchdog timer due to time restrictions, however this
will be crucial for long-term unsupervised operation of the sensor-host. It is likely
a non-responsive network or Dusty module will cause the system to halt execution indefinitely.

The watchdog timer will be crucial in managing this

This can be handled in ``sm_qsl/dn_watchdog``.

In particular

.. code-block:: c

    #include "dn_watchdog.h"

    void dn_watchdog_feed(void)
    {
        // ...
    }
