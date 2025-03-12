.. _conda:

Relocating Software Directories to Project Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On NCSA systems, users have space in their "home" file system (where their personal configuration files live) and other file systems specific to their work.  Quotas on the other file systems are usually much larger.  Unfortunately, some software stacks (python and conda in particular) store their libraries and configuration files in a hidden directory in a user's home area.  Because home quotas are generally fairly small, it's easy for the software to overrun a user's quota, and then they hit file system quota, which sometimes means they can't even log in.  

This can be avoided by relocating that software directory to your project space, which has a larger quota.  Here are the steps to find what directory is causing the problem and how to move it to somewhere with higher capacity.  

Relocate your ``.conda`` directory to your project space using the following steps:

#. Make a ``.conda`` directory in your project space.

   .. code-block:: 

      [testuser1@golubh1 ~]$ mkdir -p /projects/<your proj. dir>/<your username>/.conda

#. Copy over your existing ``.conda`` data.  (This may take several minutes if your ``.conda`` directory is large.)

   .. code-block::

      [testuser1@golubh1 ~]$ rsync -aAvP ~/.conda/* /projects/<your proj. dir>/<your username>/.conda/

#. Remove your current ``.conda`` directory.

   .. code-block::

      [testuser1@golubh1 ~]$ rm -rf ~/.conda

#. Create a link to your new ``.conda`` directory.

   .. code-block::

      [testuser1@golubh1 ~]$ ln -s /projects/<your proj. dir>/<your username>/.conda ~/.conda

|

..
  .. code-block::
  
     ## Make a .conda dir for yourself in your project space
     [testuser1@golubh1 ~]$ mkdir -p /projects/<your proj. dir>/<your username>/.conda
  
     ## Copy over existing .conda data
     [testuser1@golubh1 ~]$ rsync -aAvP ~/.conda/* /projects/<your proj. dir>/<your username>/.conda/
  
     ## Remove your current .conda dir
     [testuser1@golubh1 ~]$ rm -rf ~/.conda
  
     ## Create link to your new .conda dir
     [testuser1@golubh1 ~]$ ln -s /projects/<your proj. dir>/<your username>/.conda ~/.conda
