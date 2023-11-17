.. _logging_in:

Logging Into NCSA Systems
===========================

.. note:: 
   **Applicable Compute Resources:** Delta, Hydro, ICC, and Nightingale.

   See the ICRN user documentation `Acessing the System <https://docs.ncsa.illinois.edu/systems/icrn/en/latest/user_guide/accessing.html>`_ page for instructions on how to log into ICRN through your web browser.

.. _ssh:

SSH Clients
------------

Secure Shell (SSH) is a client-server architecture that provides a secure channel over an unsecured network. An SSH client is a program for logging securely into and executing commands on a remote machine. SSH encrypts the data sent over an open network, such as the internet, so that it can't be read by others.

Several SSH-based clients are available for accessing NCSA computing resources. The client you use depends on your workstation’s operating system.

.. _windows:

Microsoft Windows SSH Clients
-------------------------------

You can use the built-in SSH Client in Windows (version 10 and above) or select from several freely available third-party SSH clients. 
These typically provide a graphical user interface (GUI) rather than a command-line interface. `PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ is a popular choice, `MobaXterm <http://mobaxterm.mobatek.net/>`_ is another one.

MobaXterm
~~~~~~~~~~~~~

You can install `MobaXterm <https://mobaxterm.mobatek.net/>`_ on your workstation and use it to connect to nodes using SSH. 
MobaXterm enables an SSH connection and provides other useful utilities you can use when communicating with a cluster, such as file transfer and editing.

Follow the steps below to install MobaXterm and connect to a resource. 

One-time setup
$$$$$$$$$$$$$$$

This section is the one-time setup on your Windows machine so that it can connect to a resource.  

.. note::
   Nightingale has extra security to protect the data stored on it, so configuring this connection is slightly more complicated than other HPC clusters. The difference involves adding the SSH connection to the secure bastion node; this is described in Steps 5 and 6.

#. `Download MobaXterm <https://mobaxterm.mobatek.net/download-home-edition.html>`_ and **install** it on your Windows workstation. 

   You can install the Portable or Installer edition of MobaXterm. You will need to have admin privileges to install the Installer edition. 
   The Portable edition does not require admin privileges, to use it just **extract** the downloaded zip file and click **mobaxterm.exe**.

#. Launch the MobaXterm application and click the **Session** button in the upper left of the window to start an SSH session.

   ..  figure:: images/login/mobaxterm-session-button.png
       :alt: MobaXterm initial window with Session button circled.

#. Select **SSH** from the session types and click the **OK** button. 

   ..  figure:: images/login/mobaxterm-select-ssh.png
       :alt: MobaXterm Session window with SSH button circled.

#. In the **Basic SSH Settings** area:

   - Enter the name of the **login node** you want to access (either a general access or interactive node) in the **Remote host** text box. 

     - `Campus Cluster node hostnames <https://ncsa-campus-cluster.readthedocs-hosted.com/en/latest/user_guide/accessing.html#accessing-the-system>`_ 
     - `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#direct-access-login-nodes>`_
     - Hydro node hostnames
     - `Nightingale node hostnames <https://ncsa-nightingale.readthedocs-hosted.com/en/latest/user_guide/accessing.html#node-hostnames>`_

   - Check the **Specify username** box.

   - Enter your **NCSA Identity username**.

   The user in the below exmample is setting up to log into one of the Nightingale login nodes.

   ..  figure:: images/login/mobaxterm-basic-ssh-settings.png
       :alt: MobaXterm Session window with Basic SSH Settings filled in.

#. [**Nightingale Only**] Click the **Network settings** tab and then click the **SSH gateway (jump host)** button.

   ..  figure:: images/login/mobaxterm-network-settings.png
       :alt: MobaXterm Session window with showing Network settings tab clicked and SSH gateway jump host button displayed.

#. [**Nightingale Only**] In the configuration window displayed:

   - Enter **ngale-bastion-1.ncsa.illinois.edu** in the **Gateway host** box.

   - Enter your **NCSA username** in the **Username** box. 

   - Click the **OK** button. 

   - You may see a warning message saying that your remote host identification has changed; click the **Yes** button to continue.

   ..  figure:: images/login/mobaxterm-jump-host-configuration.png
       :alt: MobaXterm Session window with showing values for the SSH gateway jump host filled in.

#. Click the **OK** button in the **Session settings** window to initiate your SSH connection. 

#. Enter your **NCSA (Kerberos) password** in the terminal window and hit **Enter**.

Logging Into the System
$$$$$$$$$$$$$$$$$$$$$$$$$$

Once the above, one-time, steps are complete for a resource, follow the below steps each time you want to log into the resource to work.

#. Open **MobaXterm**. 

#. In the left bar, there is a list of **User sessions**. Each one is a node that you configured for logging in. Mouse over the node you want to log into, **right click**, and in the resulting menu, select **execute**. 

#. Enter your **NCSA password** in the pop-up window; as you type it, you will see a row of *************. Hit **Enter** or click **OK**.

#. A window will pop up asking for your 2FA code. Open your **Duo app**, click on the **NCSA** entry (not the *University of Illinois* entry), and type the 6-digit code displayed in the Duo app into the pop-up window. Like your password, it will display as ********** as you type.  

#. The screen will bring up a black window without a prompt. **You may need to wait 30 seconds or a minute here.** Then it will ask for your password. Enter your **NCSA password**. You **won't see your characters** echoed back on the screen; just type it blindly.

#. You should have a prompt at the bottom and a file window on the left showing your directories on the resource. You are now ready to work.  

..
  Termius
  ~~~~~~~~~

.. _mac:

Mac OS X SSH Clients
----------------------

Mac OS X comes with a built-in open-source version of SSH called OpenSSH. You can access it via the Terminal application. 
`PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ is also available for Mac OS X.

One-time X Window Software Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use an application from a resource and have its windows on your own computer, before logging in, install XQuartz on your Mac OS system. You can `download XQuartz here <https://www.xquartz.org/>`_.  

One-time SSH Configuration 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open the **Terminal** application on your Mac; that presents a black window that you can type commands into. 

#. At the prompt, type ``cd ~/.ssh`` and then hit **return** or **Enter** (in these instructions, **return** and **Enter** are interchangeable).  

#. Type ``nano config`` and hit **return**. This will bring you into an editor program that looks like this:

   .. code-block::  

       UW PICO 5.09                            File: config                               







       ^G Get Help   ^O WriteOut   ^R Read File  ^Y Prev Pg    ^K Cut Text   ^C Cur Pos    
       ^X Exit       ^J Justify    ^W Where is   ^V Next Pg    ^U UnCut Text ^T To Spell   

   This allows you to edit a configuration file that sets up connections to the outside world, so you don't have to type as much all the time. 

#. Copy the lines from the below code block, you will modify them in your window per the next steps. 

   .. note::
      If you are using Nightingale, copy both the **Host ngb1** and **Host ng-login01** paragraphs. If you are using any other resource, only copy the **Host ng-login01** paragraph.

   .. code-block::

      Host ngb1
        HostName ngale-bastion-1.ncsa.illinois.edu
        ControlMaster auto
        ControlPath /tmp/ssh_mux_%h_%p_%r
        ControlPersist 5h
        User YOUR_USERNAME

      Host ng-login01
        HostName ng-login01.ngale.internal.ncsa.edu
        ProxyJump ngb1
        User YOUR_USERNAME

#. After pasting the above lines into the file, use the arrow keys to position your cursor and replace the below inputs:

   - [If you are *not* logging into Nightingale]: Replace **ng-login01** with the name of the head node you are logging into.   
   - Replace **YOUR_USERNAME** with your NCSA identity username. 
   - [If you are *not* logging into Nightingale]: Replace **ng-login01.ngale.internal.ncsa.edu** with the node hostname you are logging into:

     - `Campus Cluster node hostnames <https://ncsa-campus-cluster.readthedocs-hosted.com/en/latest/user_guide/accessing.html#accessing-the-system>`_ 
     - `Delta node hostnames <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/accessing.html#direct-access-login-nodes>`_
     - Hydro node hostnames

   [**Nightingale only**] If you have an interactive node assigned to you on Nightingale, you can add another copy of the last stanza of the configuration file, and in that stanza, replace "ng-login01" with the name of *your* login node.  

     For example, a user with username "hirop" with the assigned node "ng-gpu-x07" on Nightingale would have the below configuration file.  

     .. code-block::

        Host ngb1
          HostName ngale-bastion-1.ncsa.illinois.edu
          ControlMaster auto
          ControlPath /tmp/ssh_mux_%h_%p_%r
          ControlPersist 5h
          User hirop

        Host ng-login01
          HostName ng-login01.ngale.internal.ncsa.edu
          ProxyJump ngb1
          User hirop
      
        Host ng-gpu-x07
          HostName ng-gpu-x07.ngale.internal.ncsa.edu
          ProxyJump ngb1
          User hirop
      
#. Once you have finished editing the file, hit **control-O** to write the file.

#. Hit **return** to confirm the file name. 

#. Hit **control-X** to exit the editor, and you are back at the prompt.  
      
Logging Into the System
~~~~~~~~~~~~~~~~~~~~~~~~~~
      
Once the above, one-time, steps are complete, follow the below steps each time you want to log into a resource to work.

#. Type the following at the prompt, replacing **ng-login01** with the name of the node you are logging into:

   .. code-block::

      ssh -X ng-login01

   You may see a message that begins "The authenticity of host...." and ends with "Are you sure you want to continue connecting (yes/no/[fingerprint])?" You may safely type **yes** then hit **return**.  

#. Enter your NCSA (kerberos) password at the prompt. You **won't see your characters** echoed back to the screen; just type it blindly.  

#. There will be a Duo prompt asking for a passcode or for "option 1". You may either:

   - Type **1**, then your phone Duo will ask you for login confirmation. 
   
   Or 

   - Enter a 6-digit password from the **NCSA** entry of your Duo app.  

#. Again enter your NCSA password at the prompt. You again **won't see your characters** echoed to the screen; just type it blindly.  

#. You should now be at a prompt that reflects that you are on a node for the system. You will know this because the prompt (the bottom line in your terminal or SSH window) will contain the name of the machine you are working on; that should begin with "ng-" for Nightingale, "??-" for Delta, "??-" for ICC, and "??-" for Hydro. It will look something like this: 

   .. code-block::

      [hirop@ng-gpu-m01 ~] $

   You can load modules and run software and access your files from there.  

.. _linux:

Linux SSH Clients
-------------------

The Linux operating system has SSH built into it. You use the Linux terminal application to connect via SSH. 
`PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ is also available for Linux.

Open OnDemand
---------------
Open OnDemand is a graphical login client that creates an entire Linux virtual desktop in a browser tab.  It is implemented on most NCSA systems.  

Thinlinc
----------------
Thinlinc is a graphical login client that creates an entire Linux virtual desktop in a browser tab.  It is available on select NCSA systems.  
