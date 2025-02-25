.. _install-software:

Install Software/Libraries
==================================

You can install software/libraries specific to your needs into any location on a system that you have **write access** to. These locations are generally:

- **Home**
- **Projects** (recommended)
- **Scratch** or **work** (not recommended - but good for testing the installation process)

Use What is Already Available
------------------------------

NCSA systems include a lot of pre-installed software. 
You can leverage (build against) a system's built-in software/library installations. 
Run the following command to see what is already available.

.. code-block:: terminal

   module avail

When you find the software/library you want, use the following command to load it into your environment. (Replace ``<module_name>`` with the name of the module you want to load).

.. code-block:: terminal

   module load <module_name>

Software/Library that isn't Pre-Installed
-----------------------------------------------

Software/library installation instructions generally assume that the installer has Admin, Root, SU or SUDO access to the system that they are installing the software/library on. 
You do not have this level of access on NCSA computing systems; it would make a cluster unstable/unreliable if users could install software/libraries into the system locations. Providing users with root/sudo access could allow users to uninstall, update, and/or modify software and libraries out from underneath one another.

On NCSA systems, user-installed software/libraries must be installed without the use of privileged installation commands like ``sudo``, ``yum``, ``apt-get``, and ``rpm``. This can generally require building software/libraries from source, specifying a **non-system** installation directory, and setting environment variables. In some cases, specific software/libraries can be installed via an anaconda environment.

The following sections have additional system-specific information:

- `Delta: Installed Software <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/software.html>`_
- `DeltaAI: Installed Software <https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/user-guide/software.html>`_
- `HAL: Software <https://docs.ncsa.illinois.edu/systems/hal/en/latest/user-guide/software.html>`_
- `Hydro: Programming Environments <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/prog-env.html>`_
- `ICC: Investor-Specific Software Installation <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/investor.html>`_, `ICC: Software <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/software.html>`_
- `ICRN: Packages <https://docs.ncsa.illinois.edu/systems/icrn/en/latest/user_guide/packages.html>`_
- `Nightingale: Software <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/software.html>`_

If there is a software/library that you think should be installed on a system for **all users**, :ref:`submit a support request <help>` and system admins will review your request for broad applicability and installation effort.

|
