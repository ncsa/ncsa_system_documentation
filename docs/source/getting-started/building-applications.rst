.. _compile:

Building Applications
---------------------

The GNU Compiler Collection (GCC) is available by default for compiling source code. 
The general syntax to compile source code and build an application (executable) is to type the **compile command** followed by the **source code file**. 
For example, to build an executable for a C program named ``myprogram.c`` the syntax would be:

.. code-block:: terminal

   gcc myprogram.c

A successful build will generate an executable (binary) file named ``a.out`` that can be executed (run) by typing:

.. code-block:: terminal

   ./a.out

Additional information can be found in the :ref:`compile` section.

.. raw:: html

   <details>
   <summary><a><b>GCC Build Example</b> <i>(click to expand/collapse)</i></a></summary>

To build an application using the ``hello.c`` program that was created in the nano text editor example above:

#. Type:

   .. code-block:: terminal

      [My_NetID@cc-login1 ~]$ gcc hello.c

#. An executable file will be created named ``a.out``. To verify that the file exists, type:

   .. code-block:: terminal

      [My_NetID@cc-login1 ~]$ ls -l a.out

.. raw:: html

   </details>

|

.. _submit:

Batch Job Submission
~~~~~~~~~~~~~~~~~~~~

The head (login) nodes on the cluster are a shared resource for all users. Computational use of the head nodes should be limited to compiling and building programs, and for short non-intensive runs. 
Users should do all production work by submitting jobs to the batch system.

To submit jobs on the cluster, users should create a *job script*. 
A job script is a plain text file that contains special lines that describe the resources needed for the batch job. 
Also contained in the job script are sequential commands to execute specific tasks or run a specific code.

The job script is submitted to the batch system using the ``sbatch`` command.

.. raw:: html

   <details>
   <summary><a><b>Job Script Creation and Submission Example</b> <i>(click to expand/collapse)</i></a></summary>

**Job Script Creation**

This example uses nano to create a job script. 

#. Type the following to open a blank text file named ``myjob.sbatch``:

   .. code-block:: terminal

      [My_NetID@cc-logn1 ~]$ nano myjob.sbatch

#. Type the job script as shown below in your nano text editing session.

   If you don't know the name of the account(s) available to you, ask your `technical representative <https://campuscluster.illinois.edu/about/investors/>`_ or :ref:`submit a support request <help>`.

   .. code-block:: terminal

      #!/bin/bash
      #
      #SBATCH --time=00:05:00
      #SBATCH --nodes=1
      #SBATCH --ntasks-per-node=16
      #SBATCH --job-name=myjob
      #SBATCH --account=account_name   # <- replace "account_name" with an account available to you
      #SBATCH --partition=secondary
      #SBATCH --output=myjob.o%j
      ##SBATCH --error=myjob.e%j
      ##SBATCH --mail-user=NetID@illinois.edu     # <- replace "NetID" with your University NetID
      ##SBATCH --mail-type=BEGIN,END
      #
      # End of embedded SBATCH options
      #
   
      # Run the hello world executable (a.out)
      ./a.out

#. After entering the job script, exit the nano text editing session by holding down control (**Ctrl**) and **X**, which is indicated by a "**^X**" in the bottom left corner of the nano session. 

   Exiting a nano session after editing a text file will prompt to save the changes made to the text file. To save changes without exiting the nano session hold down control (**Ctrl**) and **O**.

**Job Submission**

To submit a job to the batch system using the job script created in nano above, type:

.. code-block:: terminal

   [My_NetID@cc-login1 ~]$ sbatch myjob.sbatch

A message with a job identification number similar to the one shown below is printed to the screen as confirmation that the job was successfully submitted to the batch system.

.. code-block:: terminal

   Submitted batch job 110975

.. raw:: html

   </details>

|

To try other types of beginner examples (MPI, OpenMP, or Hybrid), view the ``README.helloworld`` file by typing the below on the command line:

.. code-block:: terminal

   cat /projects/consult/examples/README.helloworld

Batch Commands
~~~~~~~~~~~~~~

There are a number of commands/utilities available that will report details about a batch job. 
The numeric portion of the job identification (``JobID``) string or the ``NetID`` can be used to view details about a batch job. 
Some examples of the available commands are as follows:

- To display the status of all jobs in the batch system owned by you:

  .. code-block:: terminal

     squeue -u My_NetID

- To display details of a specific job identified by ``JobID``:

  .. code-block:: terminal

     scontrol show job JobID

- To remove a queued job or delete a running job identified by ``JobID``:

  .. code-block:: terminal

     scancel JobID
