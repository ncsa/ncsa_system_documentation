.. _transfer:

Transferring Files
===================

.. note::
   **Applicable Compute Resources:** Delta, Hydro, ICC, and Nightingale.

.. _globus:

Globus
-----------  

`Globus <https://www.globus.org>`_ is a web-based file transfer system that works in the background to move files between systems with Globus endpoints. Globus is a good tool to use to transfer many files or large files to and from your directories. 

- If you are new to Globus, reference the `Globus log in and transfer files tutorial <https://docs.globus.org/guides/tutorials/manage-files/transfer-files/>`_ to get started. The tutorial includes step-by-step instructions for transferring files that you can follow along with using their built-in demonstration collections.

- Find the collection names for NCSA's endpoints at the below links:

  - `Delta endpoint <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/data_mgmt.html#transferring-data>`_
  - `Hydro endpoint <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/accessing_transferring_files.html#using-globus-to-transfer-files>`_
  - `ICC endpoint <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_ 
  - `Nightingale endpoint <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/file_mgmt.html#file-transfers-with-globus>`_ 

- If you have issues using Globus, review the resources on the `Globus Contact Us <https://www.globus.org/contact-us>`_ page.

Tips for Using Globus with NCSA Compute Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- When you select one of the above endpoints for the first time, you *may* see an Authentication/Consent Required prompt (Nightingale example shown below). 

  #. Click continue.

     .. figure:: images/transfer/globus-authentication-required-example.png
        :alt: Authentication/Consent Required prompt example for the Nightingale endpoint.

  #. Click the identity you want to link (there may only be one option).

     .. figure:: images/transfer/globus-link-an-identity.png
        :alt: Link an identity prompt example for the Nightingale endpoint.

  #. Follow the prompts to log into and link your required identity. 

- Reference the `Globus link an identity tutorial <https://docs.globus.org/guides/tutorials/manage-identities/link-to-existing/>`_ for instructions on how to proactively link an identity to your Globus account. Consider linking your UIUC, NCSA, and/or ACCESS identity, as applicable, depending on the compute resource you're using and how you created your Globus account.

      

- After you have navigated to an endpoint using the **Collection** search, entering a forward slash ( / ) into the **Path** field will display the top-level directories you have access to at that endpoint. From there you can navigate to the location you want to transfer to/from. (You can also enter the direct file path into the **Path** field.)

  .. figure:: images/transfer/globus-file-manager-path-example.png
     :alt: Globus screenshot example showing the results with "Illinois Research Storage" collection and "/" path.
   
|

..
  =================
  .. _globus-link:
  
  One-Time Setup
  ~~~~~~~~~~~~~~~~
  
  To use Globus to transfer files to and from your NCSA resource directories, you first need to *link* your NCSA (Delta, Hydro, and Nightingale) or UIUC (ICC) identity.
  
  #. Go to `globus.org <globus.org>`_ and click on **LOG IN**.
  
     .. figure:: images/transfer/globus-homepage.png
        :alt: Globus homepage with login button highlighted in upper-right corner.
  
  #. Enter **UIUC** in the **Look-up your organization** field. 
  
  #. Select **University of Illinois at Urbana-Champaign** from the dropdown menu and click **Continue**.
  
     .. figure:: images/transfer/globus-login-organization.png
        :alt: Globus use your existing organizational login window with University of Illinois at Urbana-Champaign entered.
  
  #. Complete your **UIUC login** and **UIUC Duo** authentication, when prompted. 
  
     If you have an existing Globus account, separate from UIUC/NCSA, you can `link your idenity to an existing Globus account <https://docs.globus.org/guides/tutorials/manage-identities/link-to-existing/>`_. 
  
     .. note::
        If you are using ICC, you can now jump to the :ref:`file transfer <transfer-globus>` steps. 
  
        If you are using Delta, Hydro, or Nightingale, continue with the remaining setup steps.
  
  #. Click on **Settings** in the left menu pane.
  
     .. figure:: images/transfer/globus-left-menu-pane.png
        :alt: Globus left menu pane with settings highlighted.
  
  #. Click on the **Account** tab.
  
     .. note::
        If your NCSA username and email address is listed (your University of Illinois at Urbana-Champaign identity is **not** your NCSA identity), you can now jump to the :ref:`file transfer <transfer-globus>` steps. 
  
        If your NCSA username and email address are **not** listed, continue with the remaining steps.
  
     .. figure:: images/transfer/globus-settings-account-with-ncsa.png
       :alt: Globus account window showing no NCSA identity.
  
  #. Click **Link Another Identity**.
  
     .. figure:: images/transfer/globus-link-another-identity.png
        :alt: Globus link another identity button.
  
  #. Enter **NCSA** in the **Look-up your organization** field. 
  #. Select **National Center for Supercomputing Applications** and click **Continue**.
  
     .. figure:: images/transfer/globus-select-an-identity-to-link.png
        :alt: Globus select an identity to link window with National Center for Supercomputing Applications entered.
  
  #. Enter your **NCSA username** and **NCSA Kerberos password** and then click **Login**.
  
     .. figure:: images/transfer/globus-ncsa-authentication.png
        :alt: NCSA web authentication window with NCSA username and NCSA Kerberos password fields.
  
  #. Approve the **NCSA Duo** push on your mobile device.
  
  #. If you are directed to the **Log into your primary identity** window, click **Continue**.
  
     .. figure:: images/transfer/globus-log-into-your-primary-identity.png
        :alt: Globus log into your primary identity window.
  
  #. You should be redirected back to the Globus Settings **Account** window. Verify that your **NCSA** identity is listed; the Identity Provider and Organization will be **National Center for Supercomputing Applications**.
  
     .. figure:: images/transfer/globus-settings-account-with-ncsa.png
        :alt: Globus account window with an NCSA identity shown.
  
  .. _transfer-globus:
  
  Using Globus to Transfer Files
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  After you :ref:`link your identity to Globus <globus-link>`, use the below steps to transfer files.
  
  .. #. Navigate to globus.org and click **Log In** in the upper right corner
  
  ..   We recommend that you use an independent password for your Globus account. If you are doing that, on the **Log in to use Globus Web App** screen, click on **Globus ID to sign in** at the very bottom, and sign in with your Globus password.  
  
  .. #. If prompted, click **Allow** when asked to authorized the Globus Web App.
  
  ..   .. figure:: images/transfer/globus-web-app-info-and-services.png
  ..      :alt: Globus Web App authorization prompt.
  
  #. Log into `globus.org <globus.org>`_ and click on **File Manager** in the left menu pane. 
  
     .. figure:: images/transfer/globus-file-manager.png
        :alt: Globus left menu pane with file manager highlighted.
  
  #. In the **Collection** field, search for the **endpoint** of your resource (use the links below to find the endpoint of each resource). 
  
     - `Delta endpoint <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/data_mgmt.html#transferring-data>`_
     - `Hydro endpoint <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/accessing_transferring_files.html#using-globus-to-transfer-files>`_
     - `ICC endpoint <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/storage_data.html#globus-endpoint-posix-endpoint>`_ 
     - `Nightingale endpoint <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/file_mgmt.html#file-transfers-with-globus>`_ 
  
     The below example shows the Nightingale **ncsa#ngale** endpoint.
  
     .. figure:: images/transfer/globus-file-manager-collection-search.png
        :alt: Globus file manager "nagle" search results.
  
  #. Click on the **endpoint** from the search results.
  
  #. The system will prompt you to Authenticate to the endpoint, click **Continue**. 
  
     .. figure:: images/transfer/globus-authentication-consent.png
        :alt: Globus authentication/consent required prompt.
  
  #. If Globus prompts you to link your \netid@illinois.edu identity, do so. You will need to provide your NCSA Duo authority here.  
  
     .. figure:: images/transfer/globus-identity-required.png
        :alt: Globus link your @illinois.edu identity prompt.
  
     .. figure:: images/transfer/globus-web-app-info-and-services-il-research-storage.png
        :alt: Globus Web App authorization prompt
  
  #. You should be returned to the **File Manger** view. Navigate from there to your home directory or project directory. 
  
     .. figure:: images/transfer/globus-file-manager-ngale.png
        :alt: Globus file manager view showing home and project directories.
  
  #. In the other half of the **File Manger**, search for and authenticate to the collection you are planning to transfer data to/from. 
  
     .. note::
        You may need to change the **Panels** selction in the upper right corner to the *split* option to show the **Collection** search field in the other half of the **File Manager** .
  
        .. figure:: images/transfer/globus-panels-toggle.png
           :alt: Globus panels icons in upper right corner of file manager window.
  
  #. Use the GUI to transfer the data; you can choose transfer settings under **Transfer & Sync Options**. 
  
     The **Activity** tab, accessible from the left menu pane, shows your current transfer activity.
  
     .. figure:: images/transfer/globus-file-manager-transfer-window.png
        :alt: Globus file manager tansfer window.
