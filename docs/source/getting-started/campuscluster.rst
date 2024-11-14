.. _get-start-icc:

Getting Started with the Cammpus Cluster
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

/

If you are using a third-party SSH client with a GUI, you will enter the following connection information: 

- Hostname: cc-login.campuscluster.illinois.edu
- Username: Your Illinois NetID
- Port Number: 22

Once you are connected, a terminal window will be displayed and you will be prompted for your NetID password.

|
