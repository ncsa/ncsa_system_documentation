.. _quotas:

Quotas
=======

- :ref:`Jump to Quota Command <quota-command>`
- :ref:`Jump to Block Used vs File Used <blockvfile>`
- :ref:`Jump to Soft Quota vs Hard Limit <softvhard>`
- :ref:`Jump to Example Output <example-out>`
- :ref:`Jump to Cannot Log in to System with VS Code Due to Disk Quota <vscode-access-quota>`

.. _quota-command:

Quota Command
---------------

Execute the ``quota`` command to check the usage, soft quotas, and hard limits of your home directory and the shared directories you have access to.

.. _blockvfile:

Block Used vs File Used
-------------------------

There are two types of limits/quotas for each directory, block and file. 

The **block used** column is the amount of memory being used in that directory. The soft quota and hard limit columns directly following this column are the memory limits for the directory.

The **file used** column is the count of the number of files in that directory. The soft quota and hard limit columns directly following this column are the file limits for the directory.

.. _softvhard:

Soft Quota vs Hard Limit
---------------------------

.. note::
   These rules apply if you reach or exceed either the block or file quotas/limits.

On some systems, the **soft quota** and **hard limit** have the same value, and on others, they are different. 

When the soft quota and hard limit are the **same**, this is the limit that you are not allowed to exceed. If you reach it, you will not be able to write to that filesystem area until you reduce the usage to below the limit.

When the soft quota and hard limit are **different**:

- If you exceed the **soft quota**, there is a grace period to reduce the usage below that quota (the default grace period is 7 days, unless otherwise noted for a system).
- If, after the grace period, you are still exceeding the **soft quota**, you will not be able to write to that filesystem area until you reduce the usage to below the **soft quota**.
- You are not allowed to exceed the **hard limit** (there is no grace period). If you reach it, you won't be able to write to that filesystem area until you reduce the usage to below the limit.

.. _example-out:

Example Output
---------------

The following is a ``quota`` output example from Delta. This example user has access to two projects (bbka and bbkw). Notice that on Delta, the soft quotas and hard limits are different.

.. code-block:: terminal

   [username@dt-login03 ~]$ quota
   Quota usage for user username:
   -----------------------------------------------------------------------------------------------
   |        Directory Path        |  User   |  User   |  User   |   User   |   User   |   User   |
   |                              |  Block  |  Soft   |  Hard   |   File   |   Soft   |   Hard   |
   |                              |  Used   |  Quota  |  Limit  |   Used   |   Quota  |   Limit  |
   -----------------------------------------------------------------------------------------------
   | /u/username                  | 3300M   | 90600M  | 95368M  | 96806    | 490k     | 500k     |
   -----------------------------------------------------------------------------------------------
   
   Quota usage for allocations user username is a member of:
   --------------------------------------------------------------------------------------------------------------
   |        Directory Path        | Allocation | Allocation | Allocation | Allocation | Allocation | Allocation |
   |                              |   Block    |    Soft    |    Hard    |    File    |    Soft    |    Hard    |
   |                              |   Used     |    Quota   |    Limit   |    Used    |    Quota   |    Limit   |
   --------------------------------------------------------------------------------------------------------------
   | /projects/bbka               | 1.338T     | 1.953T     | 2.002T     | 596278     | 750000     | 3000000    |
   | /projects/bbkw               | 44k        | 500G       | 550G       | 11         | 375000     | 412500     |
   --------------------------------------------------------------------------------------------------------------
   | /scratch/bbka                | 4.858T     | 46.57T     | 51.22T     | 4996918    | 37500000   | 41250000   |
   | /scratch/bbkw                | 27.99M     | 500G       | 550G       | 45         | 850000     | 935000     |
   --------------------------------------------------------------------------------------------------------------
   [username@dt-login03 ~]$ 

.. _vscode-access-quota:

Cannot Log in to System with VS Code Due to Disk Quota
-------------------------------------------------------

In order to log in to a system with VS Code, VS Code must be able to write to your home directory (~/) on log in. If you home directory is at the quota/limit, then you will not be able to log in to the system via VS Code. To resolve this:

#. Use ``ssh`` to log in to the system in a terminal. 

   - `Delta login node hostnames <Cannot Access System in VS Code Due to Disk Quota>`_
   - `DeltaAI login node hostnames <https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/user-guide/login.html#login-node-hostnames>`_
   - `HAL login node hostnames <https://docs.ncsa.illinois.edu/systems/hal/en/latest/user-guide/login.html#login-node-hostnames>`_
   - `Hydro login node hostname <https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/accessing.html#logging-in>`_
   - `Illinois Campus Cluster login node hostnames <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/accessing.html#logging-in-to-the-cluster>`_
   - `Illinois HTC login node hostname <https://docs.ncsa.illinois.edu/systems/iccp-htc/en/latest/user-guide/accessing.html#how-to-log-into-the-system>`_
   - `Nightingale login node hostnames <https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/accessing.html#node-hostnames>`_

#. Run the ``quota`` command on the system to see how much above the quota/limit you are in your home directory. Note, you may have reached your "Block Used" and/or "File Used" quota/limit.

#. Delete files in your home directory (or move them to ``/projects``, ``/scratch``, or ``/work`` directory, as appropriate) until you are below the quota/limit.

#. After you have returned your home directory back below the quota/limit, try logging in to the system via VS Code.

|
