.. _dir_full:

Home Directories Full
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On NCSA systems, you have space in your "home" file system (where your personal configuration files live) and other file systems specific to your work.  Quotas on the other file systems are usually much larger.  Unfortunately, some software stacks (python and conda in particular) store their libraries and configuration files in a hidden directory in your home area.  Because home quotas are generally fairly small, it's easy for the software to overrun your quota, and then they hit file system quota, which sometimes prevents you from logging in.  

Do not store computational data in your home directory. Instead use the /projects or the /work directories.

We are aware that users are running out of space in their home directories frequently; unfortunately, there's no universal solution.  You will need to find where software is storing their libraries and install files.  Whenever possible, install software in locations other than under your home directory.  Configure the software to use storage in directories other than your home directory.  How you do this is dependent on what the software is.  



Conda
$$$$$$$$$$$$$$$

Various versions of the conda software can easily fill up your home quota, especially when you install many versions of packages.  If you use conda, you can reduce the likelihood of filling up your home directory by frequenty running this command (especially after installing packages): 

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
