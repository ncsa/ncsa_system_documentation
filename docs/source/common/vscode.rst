.. _vscode-trouble:

VS Code Troubleshooting and Performance Issues
================================================

.. _vscode-access-quota:

Cannot Log in with VS Code Due to Disk Quota Exceeded
-------------------------------------------------------

When you log in to a system with VS Code, VS Code must be able to write to your home directory (``~/``) on log in. Therefore, if your home directory is at its quota/limit, you will not be able to log in to the system via VS Code. To resolve this:

#. Use ``ssh`` to log in to the system in a **terminal**. 

#. Run the ``quota`` command on the system to see how much above the quota/limit you are in your home directory. Note, you may have reached your "Block Used" and/or "File Used" quota/limit.

#. Delete files in your home directory (or move them to the ``/projects``, ``/scratch``, or ``/work`` directory, as appropriate) until you are below the quota/limit.

#. After you have returned your home directory below the quota/limit, try logging in to the system via VS Code.

We have also seen cases where it was necessary to remove ``$HOME/.vscode`` on Delta similar the `VS Code documentation - clean uninstall <https://code.visualstudio.com/docs/setup/uninstall#_clean-uninstall>`_.

VS Code Performance Issues
----------------------------

#. See `Microsoft's VS Code Performance Issues Guide <https://github.com/Microsoft/vscode/wiki/Performance-Issues>`_.

#. Run the ``code --status`` command in a VS Code terminal.

   ..  image:: ../images/vscode/01_code_status.png
       :alt: Using the code --status command with vscode.
       :width: 700
