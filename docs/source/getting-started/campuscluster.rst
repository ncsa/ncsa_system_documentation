.. _get-start-icc:

Getting Started on the Campus Cluster
==========================================

This guide is intended for users with *no prior experience* with Linux/Command Line Interface (CLI) or cluster computing. 
Refer to the user guide sections for detailed information on using the Campus Cluster. 

.. note:: 
   For a more detailed introduction to cluster computing, including step-by-step exercises, go to our self-paced tutorial `Getting Started on the Illinois Campus Cluster <https://www.hpc-training.org/moodle/course/view.php?id=39>`_.

.. include:: allocation.rst

.. include:: introduction.rst

Connecting to the Campus Cluster
---------------------------------

To connect to the Campus Cluster login nodes using Secure Shell (SSH), you will need the following:

- An account on the Campus Cluster
- Your University of Illinois NetID and NetID password
- The hostname for the campus cluster: **cc-login.campuscluster.illinois.edu**
- Access to an SSH client

Connect from a Terminal Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open a terminal window on your local workstation.

#. Enter the following command. Replace ``NetID`` with your Illinois NetID.

   .. code-block::
      
      ssh NetID@cc-login.campuscluster.illinois.edu

#. At the prompt, enter your NetID password and press **enter (return)**. As you type, the terminal will not show your password (or placeholder symbols such as asterisks [*]).

Third-Party SSH Client with a GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using a third-party SSH client with a GUI, you will enter the following connection information: 

- Hostname: cc-login.campuscluster.illinois.edu
- Username: Your Illinois NetID
- Port Number: 22

Successful Login
~~~~~~~~~~~~~~~~~

If your login is successful, you will be connected to one of the Campus Cluster login nodes. Which one of the nodes will be indicated in the terminal window command prompt. The example prompt shown below indicates that the user has been logged into the login node named ``cc-login1``.

.. code-block::

   [NetID@cc-login1 ~]$

Once you are connected, a terminal window will be displayed and you will be prompted for your NetID password.

.. include:: cli.rst

.. include:: text-editors.rst

.. include:: building-applications.rst

.. include:: ../common/transfer.rst
   :start-after: Secure File Transfer Protocol (sftp)

.. include:: windows-compatibility.rst

|
