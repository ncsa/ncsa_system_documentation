.. _transfer:

Transferring Files
===================

.. _globus:

File Transfers with Globus
-----------------------------

.. warning::

   As of January 2023, Globus is available for use on **Nightingale**. However, we have not finished the final contracts and setup for specifically HIPAA-data certified variant of Globus, so **do not transfer HIPAA data over Globus** at this time. When HIPAA-certified Globus is installed, this warning will be removed. If you have any questions about data movement, please don't hesitate to submit a ticket (:ref:`help`).  

Globus is a web-based file transfer system that works in the background to move files between systems with "Globus Endpoints". Nightingale will have a permanent Globus Endpoint (with a name announced at that time). To transfer files to and from your directories using Globus, you will have to authenticate that endpoint, using your already-existing NCSA username, password, and NCSA Duo account. 

One-Time Setup
~~~~~~~~~~~~~~~~

You will need to set up a separate account on globus.org, that will have a username and a separate password. To use Globus to transfer files to and from Nightingale, you will need to "link" your new Globus account with your NCSA identity. 

#. Log into globus.org.
#. Click on **Account** in the left sidebar.
#. Click on the **Identities** tab. If your NCSA username and email address is not in that list, then click **Link Another Identity** in the upper right to link it.

Using Globus to Transfer Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your identity is linked (above), then do the following to transfer files using Globus.

#. Navigate to globus.org and click **Log In** in the upper right corner

   We recommend that you use an independent password for your Globus account. If you are doing that, on the **Log in to use Globus Web App** screen, click on **Globus ID to sign in** at the very bottom, and sign in with your Globus password.  

#. If prompted click **Allow** when asked to authorized the Globus Web App.

   .. figure:: images/transfer/globus-web-app-info-and-services.png
      :alt: Globus Web App authorization prompt.
      :width: 600
      :figwidth: 700

#. Once logged in, you should be taken to the **File Manager** section. On one side, search for "ngale" and click on the **ncsa#ngale** endpoint from the resulting list.

   .. figure:: images/transfer/globus-file-manager-collection-search.png
      :alt: Globus file manager "nagle" search results.
      :width: 500
      :figwidth: 600

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

#. In a similar manner (in the right half of the **File Manger** view), search for and authenticate to the collection you are planning to transfer data to/from. Then use the GUI to transfer the data; you can choose transfer settings. You can click on the **Activity* button on the left to view your current transfer activity.

   .. figure:: images/transfer/globus-file-manager-transfer-window.png
      :alt: Globus file manager tansfer window.
      :width: 800
      :figwidth: 900

|
