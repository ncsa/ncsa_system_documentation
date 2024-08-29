.. _storage-areas:

Storage Areas
================

Quotas
--------

When you run the ``quota`` command, you will see columns for soft quota and hard limit. On some systems, these will have the same value, and on some systems, they will be different. 

If the soft quota and hard limit are the **same**, then it is straightforward, this is the limit that you will not be allowed to exceed. If you do exceed it, you won't be able to write to that filesystem area until you reduce the usage to below the limit.

If the soft quota and hard limit are **different**:

- If you exceed your **soft quota**, there is a grace period to reduce your usage below that limit (the default grace period is 7 days, unless otherwise noted for a specific system).
- If, after the grace period, you are still exceeding the **soft quota**, you will not be able to write anything to that filesystem area until you reduce the usage to below the **soft quota** value.
- At no point, can you exceed a **hard limit**. If your reach the **hard limit** for a filesystem area, you will not be able to write to it until you reduce the usage below the limit.

The following is a ``quota`` output example from Delta; this example user has access to two projects (bbka and bbkw). You can see that on Delta, the soft quota and hard limit are different.

.. code-block:: terminal

   [username@dt-login03 ~]$ quota
   Quota usage for user username:
   -----------------------------------------------------------------------------------------------
   |        Directory Path        |  User   |  User   |  User   |   User   |   User   |   User   |
   |                              |  Block  |  Soft   |  Hard   |   File   |   Soft   |   Hard   |
   |                              |  Used   |  Quota  |  Limit  |   Used   |   Quota  |   Limit  |
   -----------------------------------------------------------------------------------------------
   | /u/username                  | 2520M   | 90600M  | 95368M  | 84734    | 490k     | 500k     |
   -----------------------------------------------------------------------------------------------
   
   Quota usage for allocations user username is a member of:
   --------------------------------------------------------------------------------------------------------------
   |        Directory Path        | Allocation | Allocation | Allocation | Allocation | Allocation | Allocation |
   |                              |   Block    |    Soft    |    Hard    |    File    |    Soft    |    Hard    |
   |                              |   Used     |    Quota   |    Limit   |    Used    |    Quota   |    Limit   |
   --------------------------------------------------------------------------------------------------------------
   | /projects/bbka               | 1.275T     | 1.953T     | 2.002T     | 308133     | 750000     | 3000000    |
   | /projects/bbkw               | 44k        | 500G       | 550G       | 11         | 375000     | 412500     |
   --------------------------------------------------------------------------------------------------------------
   | /scratch/bbka                | 6.44T      | 46.57T     | 51.22T     | 5050378    | 85000000000 | 93500000000 |
   | /scratch/bbkw                | 27.99M     | 500G       | 550G       | 45         | 850000     | 935000     |
   --------------------------------------------------------------------------------------------------------------
   [username@dt-login03 ~]$ 


.. _storage-home:

Home
-----

The ``/home`` area of the filesystem is where you land when you log into the cluster via SSH and is where your ``$HOME`` environment variable points. 
This area typically has a small quota and is meant to contain your configuration files, job output/error files, and smaller software installations. 
Your ``/home`` area of the filesystem is automatically provisioned during the account provisioning process and the space is provided by the program. 
It is *not* possible to request an expansion of home directory quota.

.. _storage-project:

Project
---------

The ``/projects`` area of the filesystem is where a group's (single faculty member, lab group, department, or an entire college) storage capacity resides. 
You can have access to multiple project subdirectories if you are a member of various investment groups, and have been granted access to the space by the investments principal investigator (PI). 
This storage area is typically where the bulk of the filesystem’s capacity is allocated.

.. _storage-scratch:

Scratch
--------

The ``/scratch`` area of the filesystem is where you can place data while it's under active work. 
The scratch area of the cluster is provisioned for all users to have access to. 

.. _storage-scratch-local:

Scratch — Local
------------------

The ``/scratch.local`` area is allocated on an individual compute node on the system, this disk is provided by a compute node’s local disk, not the shared filesystem. 
The size of ``/scratch.local`` will vary across nodes of different systems. Be careful on assuming size, especially when running in a secondary queue where you have less control over what node your job lands on. 

Data in ``/scratch.local`` is purged following a job’s completion, prior to the next job beginning on the node.

|
