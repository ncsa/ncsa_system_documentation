.. _data-transfer:

Data Transfer
---------------

At some point, you will need to transfer data/files to or from the cluster. There are several ways to transfer data to or from the cluster, two tools (sftp and Globus) will be outlined here. For more information and options for transferring data, see `Transferring Files <https://docs.ncsa.illinois.edu/en/latest/common/transfer.html>`_.

Secure File Transfer Protocol (sftp)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can transfer data using ``sftp`` via the command line or one of many common transfer utilities. Two transfer utility options, `WinSCP <https://winscp.net/eng/download.php>`_ and `Cyberduck <https://cyberduck.io/download/>`_, are described below; both are free to download and install.

WinSCP
$$$$$$$$

#. Download and install `WinSCP <https://winscp.net/eng/download.php>`_.
#. Open WinSCP and log in to the associated NCSA system node. 

   a. **File protocol**: SFTP
   b. **Host name**:

     - `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#login-node-hostnames>`_
     - `HAL data node hostname <https://docs.ncsa.illinois.edu/systems/hal/en/latest/user-guide/data-mgmt.html>`_
     - `Hydro node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
     - `ICC DTN node hostname <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#cli-dtn-nodes>`_
     - `Nightingale node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_

   c. **Port number**: 22
   d. **User name**: The username you use to log in to the system whose hostname you entered.
   e. **Password**: The password you use to log in to the system whose hostname you entered.

   ICC example:

   .. figure:: ../common/images/transfer/winscp-new-login.png
      :alt: WinSCP new login example for Campus Cluster DTN node.
      :width: 768px

#. Once you're logged in, WinSCP works like a drag and drop interface for moving files between your local machine and remote machine connection.

Cyberduck
$$$$$$$$$$$

#. Download and install `Cyberduck <https://cyberduck.io/download/>`_.
#. Open Cyberduck and click **Open Connection** in the upper left corner.

   .. figure:: ../common/images/transfer/cyberduck-open-connection-button.png
      :alt: Cyberduck interface highlighting the "Open Connection" button in the upper left corner.
      :width: 512px

#. Connect to the associated NCSA system node.

   a. Select **SFTP** in the drop-down menu.
   b. **Server**: 

     - `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#login-node-hostnames>`_
     - `HAL data node hostname <https://docs.ncsa.illinois.edu/systems/hal/en/latest/user-guide/data-mgmt.html>`_
     - `Hydro node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
     - `ICC DTN node hostname <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#cli-dtn-nodes>`_
     - `Nightingale node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_
   c. **Port**: 22
   d. **Username**: The username you use to log in to the system whose hostname you entered.
   e. **Password**: The password you use to log in to the system whose hostname you entered.

   ICC example:

   .. figure:: ../common/images/transfer/cyberduck-sftp-protocol-connection.png
      :alt: Cyberduck SFTP protocol connection window. SFTP selected from drop-down menu. Server: cc-xfer.campuscluster.illinois.edu. Port: 22. Username and password: your campus cluster credentials.
      :width: 500px

#. Once connected, you should see a listing of your home directory, and you can navigate the file system via the GUI. Download and upload files, as needed.

.. _globus-jump:

Globus
~~~~~~~~

`Globus <https://www.globus.org>`_ is a web-based file transfer system that works in the background to move files between computer systems with Globus `endpoints <https://docs.globus.org/faq/globus-connect-endpoints/#what_is_an_endpoint>`_. Globus is a good tool to use to transfer many files or large files between directories (within the same system or between a systems).

.. note::
   If you are new to Globus, the `Globus log in and transfer files tutorial <https://docs.globus.org/guides/tutorials/manage-files/transfer-files/>`_ includes step-by-step instructions for transferring files that you can follow along with using their built-in demonstration collections.

The NCSA systems listed have Globus endpoints configured by the system administrators; the collection names for these endpoints are at the links below. To transfer data to/from a system that does not have a Globus endpoint, see :ref:`globus_connect_personal`.

- `Delta endpoints <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/data_mgmt.html#globus>`_
- `HAL endpoint <https://docs.ncsa.illinois.edu/systems/hal/en/latest/user-guide/data-mgmt.html>`_
- `Hydro endpoint <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/accessing_transferring_files.html#using-globus-to-transfer-files>`_
- `ICC endpoints <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoints>`_ 
- `Nightingale endpoint <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/file_mgmt.html#transferring-files-with-globus>`_ 

If you have issues using Globus, review the resources on the `Globus Contact Us <https://www.globus.org/contact-us>`_ page.

.. _globus_connect_personal:

Globus Connect Personal
$$$$$$$$$$$$$$$$$$$$$$$$$

Install `Globus Connect Personal <https://www.globus.org/globus-connect-personal>`_ to transfer files between a Globus endpoint and a system that does not have an existing Globus endpoint (a personal laptop, for example). On Nightingale, the `protected data <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/protected_data.html>`_ requirements still apply. 

Tips for Using Globus with NCSA Compute Resources
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

- When you select a Globus endpoint for the first time, you *may* see an Authentication/Consent Required prompt (Nightingale example shown below). 

  #. Click **Continue**.

     .. figure:: ../common/images/transfer/globus-authentication-required.png
        :alt: Authentication/Consent Required prompt example for the Nightingale endpoint.
        :width: 700

  #. Click the identity you want to link (there may only be one option).

     .. figure:: ../common/images/transfer/globus-link-an-identity.png
        :alt: Link an identity prompt example for the Nightingale endpoint.
        :width: 700

  #. Follow the prompts to log in to and link your required identity. 

- Reference the `Globus link an identity tutorial <https://docs.globus.org/guides/tutorials/manage-identities/link-to-existing/>`_ for instructions on how to proactively link an identity to your Globus account. Consider linking your UIUC, NCSA, and/or ACCESS identity, as applicable, depending on the compute resource(s) you're using and how you created your Globus account.

\

- After you have navigated to an endpoint using the **Collection** search, entering a forward slash ( / ) into the **Path** field displays the top-level directories you have access to at that endpoint. From there you can navigate to the location you want to transfer to/from. (You can also enter the direct file path into the **Path** field.)

  .. figure:: ../common/images/transfer/globus-file-manager-example.png
     :alt: Globus file manager showing the results of "NCSA Delta" collection and "/" path.
     :width: 700

