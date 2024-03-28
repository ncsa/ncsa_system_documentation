.. _transfer:

Transferring Files
===================

.. _scp:

CLI Transfer Method - Secure Copy (scp)
-----------------------------------------

`scp <https://man.openbsd.org/scp.1>`_ is a command line interface (CLI) application that provides a secure way to copy files and directories between machines over an unsecured network. Use ``scp`` for small to modest transfers to avoid impacting usability of a system's login node.

``scp`` requires a **source** and a **destination**; these are specified with a file path if it is on your local machine or as ``<username>@<hostname>:<file_name>`` if it is on a remote machine.

.. code-block::

   scp <options> <username>@<source_hostname>:<source_file_path> <username>@<destination_hostname>:<destination_file_path>

- `scp <options> <https://man.openbsd.org/scp.1>`_

- `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#login-node-hostnames>`_
- `Hydro node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
- `ICC DTN node hostname <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#cli-dtn-nodes>`_
- `Nightingale node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_

Transferring from Local Machine to Remote Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   scp <options> <source_file_name> <username>@<hostname>:<destination_path>

.. code-block:: terminal

   ## ICC example:
   ## testuser1 transfers a file ("local_file") from their
   ## local machine to the their home directory on the Campus Cluster
   
   [testuser1_machine] ~ % scp local_file testuser1@cc-xfer.campuscluster.illinois.edu:~/

Transferring from Remote Machine to Local Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: 

   scp <options> <username>@<hostname>:<source_file_path> <destination_path>

.. code-block:: terminal

   ## ICC example:
   ## testuser1 transfers a file ("remote_file") from their 
   ## home directory on the Campus Cluster to their local machine

   [testuser1_machine] ~ % scp testuser1@cc-xfer.campuscluster.illinois.edu:~/remote_file ./

.. _rsync:

CLI Transfer Method - rsync
-----------------------------

`rsync <https://download.samba.org/pub/rsync/rsync.1>`_ is a CLI utility that syncs files and directories. Use ``rsync`` for small to modest transfers to avoid impacting usability of a system's login node.

``rsync`` requires a **source** and a **destination**; these are specified with a file path if it is on your local machine or as ``<username>@<hostname>:<file_name>`` if it is on a remote machine.

.. code-block::

   rsync <options> <username>@<source_hostname>:<source_file_path> <username>@<destination_hostname>:<destination_file_path>

- `rsync <options> <https://download.samba.org/pub/rsync/rsync.1#OPTION_SUMMARY>`_

- `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#login-node-hostnames>`_
- `Hydro node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
- `ICC DTN node hostname <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#cli-dtn-nodes>`_
- `Nightingale node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_

Transferring from Local Machine to Remote Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   rsync <options> <source_file_name> <username>@<hostname>:<destination_path>

.. code-block::

   ## ICC example:
   ## testuser 1 transfers the "images" directory from their 
   ## local machine to a projects directory on the Campus Cluster

   [testuser1_machine] ~ % ls
   images

   [testuser1_machine] ~ % rsync -avP images testuser1@cc-xfer.campuscluster.illinois.edu:/projects/$teams_directory/

Transferring from Remote Machine to Local Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   rsync <options> <username>@<hostname>:<source_file_path> <destination_path>


.. _sftp:

Secure File Transfer Protocol (sftp)
---------------------------------------

You can transfer data using ``sftp`` via the command line or one of many common transfer utilities. Two transfer utility options, `WinSCP <https://winscp.net/eng/download.php>`_ and `Cyberduck <https://cyberduck.io/download/>`_, are described below; both are free to download and install.

WinSCP
~~~~~~~~

#. Download and install `WinSCP <https://winscp.net/eng/download.php>`_.
#. Open WinSCP and log into the associated NCSA system node. 

   a. File protocol: SFTP
   b. Host name:

     - `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#login-node-hostnames>`_
     - `Hydro node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
     - `ICC DTN node hostname <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#cli-dtn-nodes>`_
     - `Nightingale node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_

   c. Port number: 22
   d. User name: Your username for the associated NCSA system.
   e. Password: Your password for the associated NCSA system.

   ICC example:

   .. figure:: images/transfer/winscp-new-login.png
      :alt: WinSCP new login example for Campus Cluster DTN node.
      :width: 768px

#. Once you're logged in, WinSCP works like a drag and drop interface for moving files between your local machine and remote machine connection.

Cyberduck
~~~~~~~~~~

#. Download and install `Cyberduck <https://cyberduck.io/download/>`_.
#. Open Cyberduck and click the **Open Connection** button in the upper left corner.

   .. figure:: images/transfer/cyberduck-open-connection-button.png
      :alt: Cyberduck interface highlighting the "Open Connection" button in the upper left corner.
      :width: 512px

#. Connect to the associated NCSA system node.

   a. Select **SFTP** in the drop-down menu.
   b. Server: 

     - `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#login-node-hostnames>`_
     - `Hydro node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
     - `ICC DTN node hostname <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#cli-dtn-nodes>`_
     - `Nightingale node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_
   c. Port: 22
   d. Username: Your username for the associated NCSA system.
   e. Password: Your password for the associated NCSA system. 

   ICC example:

   .. figure:: images/transfer/cyberduck-sftp-protocol-connection.png
      :alt: Cyberduck SFTP protocol connection window. SFTP selected from drop-down menu. Server: cc-xfer.campuscluster.illinois.edu. Port: 22. Username and password: your campus cluster credentials.
      :width: 500px

#. Once connected, you should see a listing of your home directory, and you can navigate the file system via the GUI. Download and upload files, as needed.

.. _globus:

Globus
-----------  

`Globus <https://www.globus.org>`_ is a web-based file transfer system that works in the background to move files between computer systems with Globus `endpoints <https://docs.globus.org/faq/globus-connect-endpoints/#what_is_an_endpoint>`_. Globus is a good tool to use to transfer many files or large files between directories (within the same system or between a systems).

.. note::
   If you are new to Globus, the `Globus log in and transfer files tutorial <https://docs.globus.org/guides/tutorials/manage-files/transfer-files/>`_ includes step-by-step instructions for transferring files that you can follow along with using their built-in demonstration collections.

The NCSA systems listed have Globus endpoints configured by the system administrators; the collection names for these endpoints are at the links below. To transfer data to/from a system that does not have a Globus endpoint, see :ref:`globus_connect_personal`.

- `Delta endpoints <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/data_mgmt.html#globus>`_
- `Hydro endpoint <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/accessing_transferring_files.html#using-globus-to-transfer-files>`_
- `ICC endpoint <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_ 
- `Nightingale endpoint <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/file_mgmt.html#file-transfers-with-globus>`_ 

If you have issues using Globus, review the resources on the `Globus Contact Us <https://www.globus.org/contact-us>`_ page.

.. _globus_connect_personal:

Globus Connect Personal
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install `Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_ to transfer files between a Globus endpoint and a system that does not have an existing Globus endpoint (a personal laptop, for example). On Nightingale, the `protected data <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/protected_data.html>`_ requirements still apply. 

Tips for Using Globus with NCSA Compute Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you select a Globus endpoint for the first time, you *may* see an Authentication/Consent Required prompt (Nightingale example shown below). 

#. Click continue.

   .. figure:: images/transfer/globus-authentication-required-example.png
      :alt: Authentication/Consent Required prompt example for the Nightingale endpoint.

#. Click the identity you want to link (there may only be one option).

   .. figure:: images/transfer/globus-link-an-identity.png
      :alt: Link an identity prompt example for the Nightingale endpoint.

#. Follow the prompts to log into and link your required identity. 

Reference the `Globus link an identity tutorial <https://docs.globus.org/guides/tutorials/manage-identities/link-to-existing/>`_ for instructions on how to proactively link an identity to your Globus account. Consider linking your UIUC, NCSA, and/or ACCESS identity, as applicable, depending on the compute resource(s) you're using and how you created your Globus account.

After you have navigated to an endpoint using the **Collection** search, entering a forward slash ( / ) into the **Path** field displays the top-level directories you have access to at that endpoint. From there you can navigate to the location you want to transfer to/from. (You can also enter the direct file path into the **Path** field.)

  .. figure:: images/transfer/globus-file-manager-path-example.png
     :alt: Globus screenshot example showing the results with "Illinois Research Storage" collection and "/" path.

|
