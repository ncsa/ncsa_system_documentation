.. _transfer:

Transferring Files
===================

.. note::
   **Applicable Compute Resources:** Delta, Hydro, ICC, and Nightingale.

.. _globus:

Globus
-----------  

Globus is a web-based file transfer system that works in the background to move files between systems with **Globus Endpoints**. Globus is a good tool to use when transferring many files or large files to and from your directories.

.. _globus-link:

One-Time Setup
~~~~~~~~~~~~~~~~

To use Globus to transfer files to and from a resource, you need to "link" your Globus account with your NCSA (Delta, Hydro, and Nightingale) or UIUC (ICC) identity. 

#. Go to `globus.org <globus.org>`_ and click on **LOG IN**.

   .. image:: images/transfer/globus-homepage.png
      :alt: Globus homepage with login button highlighted in upper-right corner.

#. Enter **UIUC** in the organization search bar. 

#. Select **University of Illinois at Urbana-Champaign** from the dropdown menu and click **Continue**

#. Complete your UIUC login and UIUC Duo authentication, when prompted. 

   If you have an existing Globus account, separate from UIUC/NCSA, you can `link your idenity to an existing Globus account <https://docs.globus.org/guides/tutorials/manage-identities/link-to-existing/>`. 

   .. note::
      If you are using ICC, you can now jump to the :ref:`file transfer <transfer-globus>` steps. If you are using Delta, Hydro, or Nightingale, continue with the remaining setup steps.

#. Click on **Settings** in the left menu pane.

   .. image:: images/transfer/globus-left-menu-pane-copy.png
      :alt: Globus left menu pane with settings highlighted.

#. Click on the **Account** tab.

   .. note::
      If your NCSA username and email address is listed (your University of Illinois at Urbana-Champaign identity **is not** your NCSA identity), you can now jump to the :ref:`file transfer <transfer-globus>` steps. If your NCSA username and email address are *not* listed, continue with the remaining steps.

   .. figure:: images/transfer/globus-settings-account-with-ncsa.png
     :alt: Globus account window showing no NCSA identity.

#. Click **Link Another Identity**.

   .. figure:: images/transfer/globus-link-another-identity.png
      :alt: Globus link another identity button.

#. Enter **NCSA** in the organization search bar. 
#. Select **National Center for Supercomputing Applications** and click **Continue**.

    .. figure:: images/transfer/globus-select-an-identity-to-link.png
       :alt: Globus select an identity to link window with national center for supercomputing applications entered.

#. Enter your **NCSA username** and **NCSA Kerberos password** and then click **Continue**.

    .. figure:: images/transfer/globus-ncsa-authentication.png
       :alt: NCSA web authentication window with NCSA username and NCSA Kerberos password fields.

#. Approve the **NCSA Duo** push on your mobile device.

#. If you are directed to the **Log into your primary identity** window, click **Continue**.

   .. figure:: images/transfer/globus-log-into-your-primary-identity.png
      :alt: Globus log into your primary identity window.

#. You should be redirected to the Globus Settings **Account** window. Verify that your **NCSA** identity is listed; the Identity Provider and Organization will be **National Center for Supercomputing Applications**.

   .. figure:: images/transfer/globus-settings-account-with-ncsa.png
      :alt: Globus account window with an NCSA identity shown.

.. _transfer-globus:

Using Globus to Transfer Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to globus.org and click **Log In** in the upper right corner

   We recommend that you use an independent password for your Globus account. If you are doing that, on the **Log in to use Globus Web App** screen, click on **Globus ID to sign in** at the very bottom, and sign in with your Globus password.  

#. If prompted, click **Allow** when asked to authorized the Globus Web App.

   .. figure:: images/transfer/globus-web-app-info-and-services.png
      :alt: Globus Web App authorization prompt.

#. After you are logged in, you should be taken to the **File Manager** section. On one side, search for your desired endpoint and click on it from the resulting list. The below example shows the Nightingale **ncsa#ngale** endpoint.

   .. figure:: images/transfer/globus-file-manager-collection-search.png
      :alt: Globus file manager "nagle" search results.

   - `Delta endpoints <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/data_mgmt.html#transferring-data>`_: **NCSA Delta**
   - `Hydro endpoints <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/accessing_transferring_files.html#using-globus-to-transfer-files>`_: **NFI Hydro**
   - `ICC endpoints <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_ 

     - POSIX: **Illinois Research Storage** 
     - Box: **Illinois Research Storage - Box**
     - Google Drive: **Illinois Research Storage - Google Drive**

   - `Nightingale <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_: **ncsa#ngale**

#. The system will prompt you to Authenticate to the endpoint, click **Continue**. 

   .. figure:: images/transfer/globus-authentication-consent.png
      :alt: Globus authentication/consent required prompt.

#. If Globus prompts you to link your netid@illinois.edu identity, go ahead and do so. You will need to provide your NCSA Duo authority here.  

   .. figure:: images/transfer/globus-identity-required.png
      :alt: Globus link your @illinois.edu identity prompt.

   .. figure:: images/transfer/globus-web-app-info-and-services-il-research-storage.png
      :alt: Globus Web App authorization prompt

#. You should then be returned to the **File Manger** view. You can navigate from there to your home directory, under **/u**, or to your project directory, under **/projects**.  

   .. figure:: images/transfer/globus-file-manager.png
      :alt: Globus file manager view showing home and project directories.

#. In a similar manner (in the right half of the **File Manger** view), search for and authenticate to the collection you are planning to transfer data to/from. Then use the GUI to transfer the data; you can choose transfer settings. You can click on the **Activity** button on the left to view your current transfer activity.

   .. figure:: images/transfer/globus-file-manager-transfer-window.png
      :alt: Globus file manager tansfer window.

|
