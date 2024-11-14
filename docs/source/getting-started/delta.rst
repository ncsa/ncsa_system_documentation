.. _get-start-delta:

Getting Started with Delta
==========================================

This guide is intended for users with *no prior experience* with Linux/Command Line Interface (CLI) or cluster computing. 
Refer to the user guide sections for detailed information on using the Campus Cluster. 

.. note:: 
   For a more detailed introduction to cluster computing, including step-by-step exercises, go to our self-paced tutorial `Getting Started on the Illinois Campus Cluster <https://www.hpc-training.org/moodle/course/view.php?id=39>`_.

.. include:: allocation.rst

.. include:: introduction.rst

Connecting to Delta
------------------------

To connect to the Delta login nodes using Secure Shell (SSH), you will need the following:

- An account on Delta
- Your NCSA username, password, and Duo multi-factor authentication. (You will set these up when you receive your allocation.)
- The hostname for the Delta: **login.delta.ncsa.illinois.edu**
- Access to an SSH client

Connect from a Terminal Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open a terminal window on your local workstation.

#. Enter the following command. Replace ``username`` with your NCSA username.

   .. code-block::
      
      ssh username@login.delta.ncsa.illinois.edu

#. At the prompt, enter your NCSA password and press **enter (return)**. As you type, the terminal will not show your password (or placeholder symbols such as asterisks [*]).

#. When prompted, complete NCSA Duo multi-factor authentication (MFA).

Connect to a Shell Interface in Open OnDemand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also access a Delta shell interface in a web browser through Open OnDemand.

#. Navigate to the `Open OnDemand shell interface <https://openondemand.delta.ncsa.illinois.edu/pun/sys/shell/ssh/dt-login>`_.
#. Log in through CILogon with your NCSA username, password, and Duo MFA.
#. Enter your NCSA password in the terminal interface prompt and hit **enter (return)**.
#. Complete NCSA Duo MFA, when prompted.

Successful Login
~~~~~~~~~~~~~~~~~~

If your login is successful, you will be connected to one of the Delta login nodes. The node will be indicated in the terminal window command prompt. The example prompt shown below indicates that the user has been logged in to the ``dt-login01`` login node.

.. code-block::

  [username@dt-login01 ~]$

.. include:: cli.rst

.. include:: text-editors.rst

.. include:: building-applications.rst

.. include:: windows-compatibility.rst

|
