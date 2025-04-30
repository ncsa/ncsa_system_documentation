.. _dir_full:

Home Directories Full
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On NCSA systems, users have space in their "home" file system (where their personal configuration files live) and other file systems specific to their work.  Quotas on the other file systems are usually much larger.  Unfortunately, some software stacks (python and conda in particular) store their libraries and configuration files in a hidden directory in a user's home area.  Because home quotas are generally fairly small, it's easy for the software to overrun a user's quota, and then they hit file system quota, which sometimes means they can't even log in.  

We are aware that users are hitting this problem frequently, unfortunately, there's no universal solution.  We will populate this page with individual software solutions as we find and test them.  

Conda
$$$$$$$$$$$$$$$

Various versions of the conda software are notorious for filling up user's home directories, especially when the user installs many versions of packages.  You can reduce the likelihood of filling up your home directory by frequenty running this command: 

.. code-block:: bash
  conda clean -a
