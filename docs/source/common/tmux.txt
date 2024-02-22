tmux Multi-Terminal Emulator
================================

`tmux <https://github.com/tmux/tmux/wiki>`_ is a text-terminal tool that is useful on modern computing systems for preserving *state*. 

If you do your terminal work in a tmux session and you get disconnected, your working shell stays resident on the login node. Then, you can log back in, use the tmux command to reconnect to your existing shell, and continue work without interruption. This allows you to have login sessions that effectively persist for weeks or more.  **tmux sessions are lost when the head nodes are rebooted.**

In contrast, if you're logged into an SSH session via text SSH from your terminal, MobaXterm, Termius, or one of the terminal emulators within Open OnDemand and your connection is lost, then your shell's state is also lost; you will have to log back in, run any initialization, and get back to where you were.  


  
