.. _conda:

Relocating Your .conda Directory to Project Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Large conda installations may exceed your home directory size. This can be avoided by relocating your ``.conda`` directory to your project space, which has a larger quota than your home directory.

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
