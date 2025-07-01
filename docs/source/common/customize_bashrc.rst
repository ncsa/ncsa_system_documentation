
Customizing your .bashrc file
=======================================

The default login shell for all NCSA systems is bash.  We can't fully instruct you how to use bash, but here are a few brief items that will help you on NCSA systems.  This list is mostly a few do or don't-do specifications, a few of which have examples.  

The login shell, bash (the "sh" in bash stands for "shell") is a piece of software that accept your written commands and do things on your behalf.  It's the remote half of your text command-line login (the other half is ssh).  When you're logged in, your bash "session" has settings and configurations that, for example, give you access to commands and software to run, like compilers or other user software.  

When you log in, you can run commands to configure bash the way you want it.  If there are configuration changes that you always make, you can put those changes in one of the configuration files that bash loads when you log in.  Probably the easiest to use is the file ".bashrc" in your home directory.  Note the period, ".", or dot at the beginning of the file name.  Command-line tools like "ls" ignore files whose name begins with "." unless you tell them otherwise.  They're hidden except when you're explicitly looking for them.  There will be a stock .bashrc file in your home directory that contains standard settings.  

You can add commands to that file that will be run every time you start up a new bash shell, like when you log in via ssh.  This page lists several commands and settings that are useful to put in your .bashrc file.  Lightweight commands and settings are fine to put in that file, but BE AWARE...that file is run as a script EVERY TIME you invoke a new shell.  That means every time you run a shell script, any shell script, which sometimes includes system commands.  So in particular, **DO NOT load any python or conda environment in your .bashrc**, because that takes time and takes up a lot of resources.  

Loading modules 
--------------------
The module suite has a way to configure the software and compilers you have available in your shell environment.  Your .bashrc is a good place to load modules that you use **all the time**, but only the ones you *always* want.  If you just want a module sometimes, it's better to leave it out of your .bashrc and load it on the fly when you need it.  

Loading python (DON'T)
----------------------------

You should NOT load a python environment or conda environment in your .bashrc.  This can take minutes for a complex environment, and does a lot of loading from the parallel file system.  

command alaises 
------------------
It's common for unix users to add often-used aliases to their shell setup scripts.  Common shell aliases include: 

rm="rm -i"
cp="cp -i"
mv="mv -i"

So it's smart to put the following in your .bashrc any time you set up your account on a new Linux system: 

.. code_block:: bash

  alias rm="rm -i"
  alias cp="cp -i"
  alias mv="mv -i"

Informational propmpts: job aliases
------------------------------------------
The text you see to the left of where you need to type your command in a bash shell is called your "prompt".  It has a basic default value, but you can customize it to contain useful information as well.  This is useful especially if you're doing a lot of interactive jobs on the system, to remind you that you're **in a job** and you're **charging your allocation**.  

Normally your prompt in an interactive job shell looks just like your prompt anywhere else.  It's very easy to start an interactive job and forget you're in an interactive job, spending your allocation for nodes that you've forgotten about.  Putting this clause in your .bashrc is a smart idea on any system that runs slurm:

.. code_block:: bash

  if [ $SLURM_NNODES ]; then
    export PS1="${PS1}\e[1;31m[${SLURM_NNODES}]\e[0m "
  fi

"PS1" here is a magic environment variable that tells bash what to put in your prompt.  If you put this clause in your .bashrc, then if you have a shell start up that's running as an interactive job, it will sense that from the "SLURM_NNODES" environment variable that slurm sets in your environment.  This will put a **red** number in brackets in your prompt to remind you that you're spending from your allocation to have this interactive job running, with the indicate number of nodes. 

