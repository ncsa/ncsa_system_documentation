
Customizing your .bashrc file
=======================================

The default login shell for all NCSA systems is bash.  A full bash tutorial is beyond the scope of this documentation, but here are a few brief items that will help you on NCSA systems.  This list is mostly a few do or don't-do specifications with some examples.  

The login shell, bash (the "sh" in bash stands for "shell") is a piece of software that accepts your written commands and does things on your behalf.  It's the remote half of your text command-line login (the other half is ssh).  When you're logged in, your bash "session" has settings and configurations that, for example, give you access to commands and software to run, like compilers or other user software.  

When you log in, you can run commands to configure bash the way you want it.  If there are configuration changes that you always make, you can put those changes in one of the configuration files that bash loads when you log in.  Probably the easiest to use is the file ``.bashrc`` in your home directory.  Note the period, ".", or "dot" at the beginning of the file name.  Command-line tools like ``ls`` ignore files whose name begins with "." unless you tell them otherwise.  They're hidden except when you're explicitly looking for them.  There will be a stock ``.bashrc`` file in your home directory that contains standard settings.  

You can add commands to .bashrc that will be run every time you start up a new bash shell, like when you log in via ssh.  This page lists several commands and settings that are useful to put there.  Lightweight commands and settings are fine to put in that file, but BE AWARE...that file is run EVERY TIME you invoke a new shell.  In particular, **DO NOT load any Python or Conda environments in your .bashrc**, because that takes time and takes up a lot of resources.  

.. warning:: 
   Be very careful sourcing other files inside your ``.bashrc`` (and indeed in your ``.profile`` or other initialization files).  The shell itself generally calls these files in a reasonable order; there's no need to have them call each other.  If you call one from the another and then mistakenly do the reverse, your new shell will end up in an infinite recursive loop which won't allow you to log in.  

Modifying your path
----------------------
Shells have an internal variable called ``PATH`` that's a list of directories where bash will look for commands to run.  PATH is a colon-separated list all in a string; each item is a directory to search.  When the shell starts up it has a sensible default list in PATH.  If you have a directory with scripts of your own, it's handy to add that directory to your path.  This is also true if you install software in your own space on a system; you'll usually want to add the path of the ``/bin`` directory of that software to your path.  

You can easily do it with a statement like this in your ``.bashrc`` file: 

.. code-block:: bash

  PATH=$PATH:/sw/admin/scripts

This sets the new PATH equal to the existing path ($PATH) but with one new directory at the end of the list.  When you type a command, bash will search the directories in the path **in order** until it finds a match, so be careful putting a directory at the beginning of your path.  If it's software that you've written, it's probably best to put it at the **end** of your path.  

Loading modules 
--------------------
The module suite is a system to configure the software and compilers when you're logged into the system in your shell environment.  Your ``.bashrc`` is a good place to load modules that you use **all the time**, but only the ones you *always* want.  If you just want a module sometimes, it's better to leave it out of your .bashrc and load it on the fly when you need it.  

Loading Python (DON'T)
----------------------------

You should NOT load a Python environment or Conda environment in your ``.bashrc``.  This can take minutes for a complex environment, and does a lot of loading from the parallel file system.  You **should** also **not run** any ``conda install`` commands; these do the same thing.  

command alaises 
------------------
It's useful to add often-used aliases to your ``.bashrc`` file.  Common shell aliases include: 

rm="rm -i"

cp="cp -i"

mv="mv -i"

These aliases call ``rm`` (remove), ``cp`` (copy), and ``mv`` (move) with the command-line option ``-i``, which asks you before it does anything.  This is very handy so that you can review by eye the file that youre removing or copying or moving.  This can keep you out of a lot of trouble as a command-line user.  (If you're managing a whole bunch of files, then it's worth running the command this way, making sure that the first several files seem to be what you want, then cancel out of the command then re-run it with the additional option ``-f`` which countermands the ``-i`` option.)

So it's smart to put the following in your ``.bashrc`` any time you set up your account on a new Linux system: 

.. code-block:: bash

  alias rm="rm -i"
  alias cp="cp -i"
  alias mv="mv -i"

Informational propmpts: job aliases
------------------------------------------
The text you see to the left of where you need to type your command in a bash shell is called your "prompt".  It has a basic default configuration, but you can customize it to your preferences.  This is useful especially if you're doing a lot of interactive jobs on the system, to remind you that you're **in a job** and you're **charging your allocation**.  

Normally your prompt in an interactive job shell looks just like your prompt anywhere else.  It's very easy to start an interactive job and forget you're in one if your prompt doesn't change.  This would be a waste of your allocation and to be avoided.  Putting this clause in your .bashrc is a smart idea on any system that runs slurm:

.. code-block:: bash

  if [ $SLURM_NNODES ]; then
    export PS1="${PS1}\e[1;31m[${SLURM_NNODES}]\e[0m "
  fi

``PS1`` here is a magic shell environment variable that tells bash what to put in your prompt.  If you put this clause in your ``.bashrc``, then if you start an interactive job, the new shell running the job will sense that and display the number of nodes you're being charged for in **red**.  This should be a reminder that when you're done with the nodes, to exit out of the shell which will stop the job.  

