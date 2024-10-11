.. _install-software:

Install Software/Libraries
==================================

You can install software/libraries specific to your needs into any location that you have **write access** to. These locations are generally:

- **home**
- **projects** (recommended)
- **scratch** or **work** (not recommended - but ideal for testing the installation process)

Use What is Already Available
------------------------------

You can leverage (build against) the system's software/library installations. Run the following command to see what's already available on the system.

.. code-block:: terminal

   module avail

After you find the software/library you want, use the following command to load it into your environment. (Replace ``module_name`` with the name of the module you want to load).

.. code-block:: terminal

   module load <module_name>

Software/Library that isn't Pre-Installed
-----------------------------------------------

Software/library installation instructions generally assume that the installer has Admin, Root, SU or SUDO access to the system that they are installing the software/library on. 
This is not the case for you on NCSA computing systems; it would make a cluster unstable/unreliable if any user could install software/libraries into the system locations. Providing users with root/sudo access could allow users to uninstall, update, modify software and libraries out from underneath one another.

User installed software/libraries must be installed without the use of privileged installation commands (for example, ``sudo``, ``yum``, ``apt-get``, and ``rpm``). This can generally require building software/libraries from source, specifying an installation directory (non-system), and setting environment variables. In some cases, specific software/libraries can be installed via an anaconda environment.

If there is a software/library that you think should be installed on a system for **all users**, :ref:`submit a support request <help>` and system admins will review your request for broad applicability.

|
