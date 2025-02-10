
Customizing your .bashrc file
=======================================

The default login shell for all NCSA systems is bash.  We can't fully instruct you how to use bash, but here are a few brief items that will help you on NCSA systems.  This list is mostly a few do or don't-do specifications, a few of which have examples.  

The login shell, bash (the "sh" in bash stands for "shell") is a piece of software that accept your written commands and do things on your behalf.  It's the remote half of your text command-line login (the other half is ssh).  When you're logged in, your bash "session" has settings and configurations that, for example, give you access to commands and software to run, like compilers or other user software.  

When you log in, you can run commands to configure bash the way you want it.  If there are configuration changes that you always make, you can put those changes in one of the configuration files that bash loads when you log in.  Probably the easiest to use is the file ".bashrc" in your home directory.  Note the period, ".", or dot at the beginning of the file name.  Command-line tools like "ls" ignore files whose name begins with "." unless you tell them otherwise.  They're hidden except when you're explicitly looking for them.  There will be a stock .bashrc file in your home directory that contains standard settings.  You can add commands to that file that will be run every time you start up a new bash shell, like when you log in via ssh.  

This page lists several commands and settings that are useful to put in your .bashrc.  Lightweight commands and settings 

Loading modules 
--------------------
The module suite has a way to configure your 


NOT initiating python or conda envronments

alaises 
-----------
It's common for unix users to add often-used aliases to their shell setup scripts.  Common shell aliases include: 

rm="rm -i"

cp="cp -i"

mv="mv -i"

So it's smart to put the following in your .bashrc any time you set up your account on a new Linux system: 

alias rm="rm -i"

alias cp="cp -i"

alias mv="mv -i"
