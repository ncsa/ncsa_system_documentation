.. _transfer:

Transferring Files
===================

.. _globus:

Globus
-----------

.. warning::

   As of January 2023, Globus is available for use on **Nightingale**. However, we have not finished the final contracts and setup for specifically HIPAA-data certified variant of Globus, so **do not transfer HIPAA data over Globus** at this time. When HIPAA-certified Globus is installed, this warning will be removed. If you have any questions about data movement, please don't hesitate to submit a ticket (:ref:`help`).  

Globus is a web-based file transfer system that works in the background to move files between systems with "Globus Endpoints". Nightingale will have a permanent Globus Endpoint (with a name announced at that time). To transfer files to and from your directories using Globus, you will have to authenticate that endpoint, using your already-existing NCSA username, password, and NCSA Duo account. 

[**Hydro and Nightingale Only**] One-Time Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to set up a separate account on `globus.org <globus.org>`_, that will have a username and a separate password. To use Globus to transfer files to and from Nightingale, you will need to "link" your new Globus account with your NCSA identity. 

#. Log into `globus.org <globus.org>`_.

   .. figure:: images/transfer/globus-homepage.png
      :alt: Globus homepage with login button highlighted in upper-right corner.
      :figwidth: 800

#. Click on **Settings** in the left menu pane.

   .. figure:: images/transfer/globus-left-menu-pane.png
      :alt: Globus left menu pane with settings highlighted.
      :width: 75
      :figwidth: 175

#. Click on the **Account** tab.

   .. figure:: images/transfer/globus-settings-account-no-ncsa.png
     :alt: Globus account window showing no NCSA identity.
     :width: 800
     :figwidth: 900

   If your NCSA username and email address is **not* in that list (your University of Illinois at Urbana-Champaign identity **is not** your NCSA identity):

      a. Click **Link Another Identity**.

         .. figure:: images/transfer/globus-link-another-identity.png
             :alt: Globus link another identity button.
             :width: 300
             :figwidth: 400

      b. Enter **NCSA** in the organization search bar. 
      c. Select **National Center for Supercomputing Applications** and click **Continue**.

         .. figure:: images/transfer/globus-select-an-identity-to-link.png
            :alt: Globus select an identity to link window with national center for supercomputing applications entered.
            :width: 800
            :figwidth: 900

      d. Enter your **NCSA username** and **NCSA Kerberos password** and then click **Continue**.

         .. figure:: images/transfer/globus-ncsa-authentication.png
            :alt: NCSA web authentication window with NCSA username and NCSA Kerberos password fields.
            :width: 700
            :figwidth: 800

      e. Approve the **NCSA Duo** push on your mobile device.

         .. figure:: images/transfer/ncsa-duo-push.png  
            :alt: NCSA Duo Push window.
            :width: 400
            :figwidth: 500

      f. If you are directed to the **Log into your primary identity** window, click **Continue**.

         .. figure:: images/transfer/globus-log-into-your-primary-identity.png
            :alt: Globus log into your primary identity window.
            :width: 700
            :figwidth: 800

      g. You should be redirected to the Globus Settings **Account** window. Verify that your **NCSA** identity is listed; the organization will be **National Center for Supercomputing Applications**.

         .. figure:: images/transfer/globus-settings-account-with-ncsa.png
            :alt: Globus account window with an NCSA identity shown.
            :width: 800
            :figwidth: 900

Using Globus to Transfer Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**After** your identity (*NCSA identity* for Hydro and Nightingale) is linked in Globus, do the following to transfer files.

#. Navigate to globus.org and click **Log In** in the upper right corner

   We recommend that you use an independent password for your Globus account. If you are doing that, on the **Log in to use Globus Web App** screen, click on **Globus ID to sign in** at the very bottom, and sign in with your Globus password.  

#. If prompted, click **Allow** when asked to authorized the Globus Web App.

   .. figure:: images/transfer/globus-web-app-info-and-services.png
      :alt: Globus Web App authorization prompt.
      :width: 600
      :figwidth: 700

#. After you are logged in, you should be taken to the **File Manager** section. On one side, search for your desired endpoint and click on it from the resulting list. The below example shows the Nightingale **ncsa#ngale** endpoint.

   .. figure:: images/transfer/globus-file-manager-collection-search.png
      :alt: Globus file manager "nagle" search results.
      :width: 500
      :figwidth: 600

   - `Delta endpoints <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/data_mgmt.html#transferring-data>`_: **NCSA Delta**
   - `Hydro endpoints <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/accessing_transferring_files.html#using-globus-to-transfer-files>`_: **NFI Hydro**
   - `ICC endpoints <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_: **Illinois Research Storage**, **Illinois Research Storage - Box**, and **Illinois Research Storage - Google Drive**
   - `Nightingale <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_: **ncsa#ngale**

#. The system will prompt you to Authenticate to the endpoint, click **Continue**. 

   .. figure:: images/transfer/globus-authentication-consent.png
      :alt: Globus authentication/consent required prompt.
      :width: 600
      :figwidth: 700

#. If Globus prompts you to link your netid@illinois.edu identity, go ahead and do so. You will need to provide your NCSA Duo authority here.  

   .. figure:: images/transfer/globus-identity-required.png
      :alt: Globus link your @illinois.edu identity prompt.
      :width: 600
      :figwidth: 700

   .. figure:: images/transfer/globus-web-app-info-and-services-il-research-storage.png
      :alt: Globus Web App authorization prompt
      :width: 600
      :figwidth: 700

#. You should then be returned to the **File Manger** view. You can navigate from there to your home directory, under **/u**, or to your project directory, under **/projects**.  

   .. figure:: images/transfer/globus-file-manager.png
      :alt: Globus file manager view showing home and project directories.
      :width: 500
      :figwidth: 600

#. In a similar manner (in the right half of the **File Manger** view), search for and authenticate to the collection you are planning to transfer data to/from. Then use the GUI to transfer the data; you can choose transfer settings. You can click on the **Activity** button on the left to view your current transfer activity.

   .. figure:: images/transfer/globus-file-manager-transfer-window.png
      :alt: Globus file manager tansfer window.
      :width: 900
      :figwidth: 1000

|
