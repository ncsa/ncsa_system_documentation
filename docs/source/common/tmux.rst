TMUX Multi-Terminal Emulator
================================

Tmux is an old-school text-terminal tool that is useful on modern computing systems for preserving *state*.  If you're logged into an ssh session (whether via text ssh from your terminal, or MobaXterm, or Termius, or one of the terminal emulators within Open OnDemand) if your connection is lost, then your shell's state is also lost, so you'll have to log back in, run any initialization, and get back to where you were.  

However, if you do your terminal work in a tmux session, then if you get disconnected, your working shell stays resident on the login node.  You can log back in, use the tmux command to reconnect to your existing shell, and continue work without interruption.  This allows you to have login sessions that effective persist for weeks or more.  (Tmux sessions are lost when the head nodes are rebooted.)
  
