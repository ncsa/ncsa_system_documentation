Relocating Your .conda Directory to Project Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Large conda installations may exceed your home directory size. This can be fixed by relocating your .conda directory to your project space, which has a larger quota than your home directory.
To relocate your .conda directory to your project space go through the following steps:

.. code-block::

   ## Make a .conda dir for yourself in your project space
   [testuser1@golubh1 ~]$ mkdir -p /projects/<your proj. dir>/<your username>/.conda

   ## Copy over existing .conda data
   [testuser1@golubh1 ~]$ rsync -aAvP ~/.conda/* /projects/<your proj. dir>/<your username>/.conda/

   ## Remove your current .conda dir
   [testuser1@golubh1 ~]$ rm -rf ~/.conda

   ## Create link to your new .conda dir
   [testuser1@golubh1 ~]$ ln -s /projects/<your proj. dir>/<your username>/.conda ~/.conda
