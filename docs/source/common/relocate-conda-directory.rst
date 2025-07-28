.. _dir_full:

Home Directories Full
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On NCSA systems, users have space in their "home" file system (where their personal configuration files live) and other file systems specific to their work.  Quotas on the other file systems are usually much larger.  Unfortunately, some software stacks (python and conda in particular) store their libraries and configuration files in a hidden directory in a user's home area.  Because home quotas are generally fairly small, it's easy for the software to overrun a user's quota, and then they hit file system quota, which sometimes means they can't even log in.  

Users need to not store computational data in their home directories.  Do that in /projects or in /work.  

We are aware that users are running out of space in their home directories frequently; unfortunately, there's no universal solution.  Users need to find where software is storing their libraries and install files and wherever possible, install the software in locations other than their home directory, and configure the software to use storage in directories other than their home directory.  How to do this is dependent on what the software is.  



Conda
$$$$$$$$$$$$$$$

Various versions of the conda software can easily fill up user's home quota, especially when the user installs many versions of packages.  If you use conda, you can reduce the likelihood of filling up your home directory by frequenty running this command (especially after installing packages): 

.. code-block:: 

   conda clean -a

*Please understand*, running "conda clean" will remove index cache, lock files, unused cache packages, tarballs, and logfiles. See the `conda clean documentation page <https://docs.conda.io/projects/conda/en/stable/commands/clean.html>`_ for more information.  

How to Relocate Your .conda Directory to Project Space
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

If even with keeping up with "conda clean" as above, your .conda directory is filling up your home directory, you may need to rebuilt your .conda installation.  If you need to move it without rebuilding it, feel free to try this procedure as a last resort, which relocates your ``.conda`` directory to your project space, which has a larger quota than your home directory.

Relocate your .conda directory to your project space using the following steps:

#. Make a ``.conda`` directory in your project space.

   .. code-block:: terminal

      [testuser1@cc-login1 ~]$ mkdir -p /projects/illinois/$college/$department/$pi_netid/<your_username>/.conda

#. Copy over existing ``.conda`` data.

   .. code-block:: terminal

      [testuser1@cc-login1 ~]$ rsync -aAvP ~/.conda/* /projects/illinois/$college/$department/$pi_netid/<your_username>/.conda/

#. Remove your ``.conda`` directory from home.

   .. code-block:: terminal

      [testuser1@cc-login1 ~]$ rm -rf ~/.conda

#. Create a link to your new ``.conda`` directory.

   .. code-block:: terminal

      [testuser1@cc-login1 ~]$ ln -s /projects/illinois/$college/$department/$pi_netid/<your_username>/.conda ~/.conda
