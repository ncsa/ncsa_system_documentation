.. _storage-areas:

Storage Areas
================

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
