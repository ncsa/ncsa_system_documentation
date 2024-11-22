.. _vscode-on-ncsa:

VS Code on NCSA Resources
===========================

Use Policy
------------

Do not run large processing work on login nodes, run it on compute nodes.

Login nodes are intended for moving files around and setting up computational jobs, not for processing large amounts of data. Processes that do a lot of work on login nodes can interfere with other user login sessions and are subject to being killed without notice. 

System-Specific Information
-------------------------------

- `Delta VS Code <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/prog_env.html#visual-studio-code>`_
- `DeltaAI VS Code <https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/user-guide/prog-env.html#visual-studio-code>`_
- `HAL VS Code <https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/user-guide/prog-env.html#visual-studio-code>`_

.. _vscode-trouble:

Troubleshooting 
-----------------

.. _vscode-access-quota:

Cannot Log in with VS Code - Disk Quota Exceeded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you log in to a system with VS Code, VS Code must be able to write to your home directory (``~/``) on log in. Therefore, if your home directory is at its quota/limit, you will not be able to log in to the system via VS Code. To resolve this:

#. Use ``ssh`` to log in to the system in a **terminal**. Go to the system user guide for instructions on how to log in with ``ssh``:

   - `Delta Login <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/login.html>`_
   - `DeltaAI Login <https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/user-guide/login.html>`_
   - `HAL Login <https://docs.ncsa.illinois.edu/systems/hal/en/latest/user-guide/login.html>`_
   - `Hydro Login <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html>`_
   - `Illinois Campus Cluster Login <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/accessing.html>`_
   - `Illinois HTC Login <https://docs.ncsa.illinois.edu/systems/iccp-htc/en/latest/user-guide/accessing.html>`_
   - `Nightingale Login <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html>`_

#. Run the ``quota`` command on the system to see how much above the quota/limit you are in your **home directory**. Note, you may have reached your "Block Used" and/or "File Used" quota/limit. For a detailed explanation of the ``quota`` command output, see :ref:`quotas`.

#. Delete files in your home directory (or move them to the ``/projects``, ``/scratch``, or ``/work`` directory, as appropriate) until you are below the quota/limit.

#. After you have returned your home directory below the quota/limit, try to log in to the system using VS Code.

We have also seen cases where it was necessary to remove ``$HOME/.vscode`` on the system, similar the `VS Code documentation - clean uninstall <https://code.visualstudio.com/docs/setup/uninstall#_clean-uninstall>`_.

VS Code Performance Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to `Microsoft's VS Code Performance Issues Guide <https://github.com/Microsoft/vscode/wiki/Performance-Issues>`_ for steps to try to resolve different performance issues.

You can run ``code --status`` in a VS Code terminal to display status information about your running VS Code and the workspace you have opened.

..  image:: images/vscode/01_code_status.png
    :alt: Using the code --status command with vscode.
    :width: 700

|
