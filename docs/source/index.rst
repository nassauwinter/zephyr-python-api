.. Zephyr Python API documentation master file, created by
   sphinx-quickstart on Sat Jun 17 21:27:13 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Zephyr Python API's documentation!
=============================================

The package is a set of python wrappers for Zephyr Scale (TM4J) REST API (both Cloud and Server/DataCenter).
Interact with Zephyr Scale without GUI, access it with python code and create automation scripts for your daily routines.

The idea of the package is to have two parts in it: a set of low-level wrappers and  Zephyr objects (like a test case or  a test cycle).
The low-level wrappers are simply performing requests to the API endpoints of Zephyr with no logic added. The Zephyr objects
is a set of classes where the Zephyr interaction logic is placed. The logic is implemented using the low-level API wrappers.
Currently the Zephyr objects are not implemented.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   installation
   examples
   troubleshooting
   zephyr

Limitations
***********

The wrappers only implement public API methods from the official SmartBear Zephyr Scale Cloud and Server/DataCenter APIs.

Useful links
************

`Zephyr Scale Cloud API docs <https://support.smartbear.com/zephyr-scale-cloud/api-docs/>`_

`Zephyr Scale Server/Data Center API docs <https://support.smartbear.com/zephyr-scale-server/api-docs/v1/>`_