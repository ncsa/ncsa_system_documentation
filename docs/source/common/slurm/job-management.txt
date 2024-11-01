.. _job-mgmt:

Job Management
===============

sview 
-------

`sview <https://slurm.schedmd.com/sview.html>`_ is a graphical user interface (GUI) that can be used to view job, node and partition (queue) states. Use the following steps to use ``sview``:

  #. Install an `X Window server <https://docs.ncsa.illinois.edu/systems/icc/en/latest/user_guide/x_window_system.html#x-windows-software>`_ on your local machine.
  #. Enable X11 when you SSH into the system with the ``-Y`` or ``-X`` option. This is an example for Delta:

     .. code-block:: terminal

        ssh -Y <loginID>@login.delta.ncsa.illinois.edu

     Once you're logged into the system, you can verify X11 is enabled by running ``xterm``. 

  #. Run ``sview`` to initiate the GUI.

..  figure:: ../images/slurm/sview-sinfo.png
    :alt: sview view of Slurm partitions

squeue
-------

The ``squeue`` command is used to pull up information about batch jobs submitted to the batch system. By default, the ``squeue`` command will print out the JobID,  partition, username, job status, number of nodes, and name of nodes for all batch jobs queued or running within batch system.

.. table:: ``squeue`` command options

  ============================ ============
  Slurm Command                Description
  ============================ ============
  ``squeue -a``                List the status of all batch jobs in the batch system.
  ``squeue -u $USER``          List the status of all your batch jobs in the batch system.
  ``squeue -j JobID``          List nodes allocated to a specific running batch job in addition to basic information.
  ``scontrol show job JobID``  List detailed information on a particular batch job.
  ============================ ============

See the squeue man page for other available options.

.. code-block::

   $ sbatch tensorflow_cpu.slurm
   Submitted batch job 2337924
   $ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           2337924 cpu-inter    tfcpu  mylogin  R       0:46      1 cn006

If the **NODELIST(REASON)** is **MaxGRESPerAccount**, that means that a user has exceeded the number of cores or GPUs allotted per user or project for a given partition.

sinfo
-------

The ``sinfo`` command is used to view partition and node information for a system running Slurm.

.. table:: ``sinfo`` command options

  +------------------------+----------------------------------------------------------+
  | Slurm Command          | Description                                              |
  +========================+==========================================================+
  | ``sinfo -a``           | List summary information on all the partitions (queues). |
  +------------------------+----------------------------------------------------------+
  | ``sinfo -p PRTN_NAME`` | Print information only about the specified partition(s). |
  |                        |                                                          |
  |                        | Multiple partitions are separated by commas.             |
  +------------------------+----------------------------------------------------------+

See the sinfo man page for other available options (``man sinfo``).

scontrol
----------

The ``scontrol`` command can be used to view detailed information on a particular job (JobID).

.. code-block::

   scontrol show job JobID

See the scontrol man page for other available options. Note that most of the ``scontrol`` options can only be executed by user root or an administrator.

scancel
---------

The ``scancel`` command deletes a queued job or ends a running job.

.. table:: ``scancel`` command options

  +------------------------------+--------------------------------------------------------------------------+
  | Slurm Command                | Description                                                              |
  +==============================+==========================================================================+
  | ``scancel JobID``            | To delete/end a specific batch job                                       |
  +------------------------------+--------------------------------------------------------------------------+
  | ``scancel JobID01, JobID02`` | To delete/end multiple batch jobs, use a comma-separated list of JobIDs  |
  +------------------------------+--------------------------------------------------------------------------+
  | ``scancel -u $USER``         | To delete/end all your batch jobs (removes all your batch jobs from      |
  |                              |                                                                          |
  |                              | the batch system regardless of the batch job’s state)                    |
  +------------------------------+--------------------------------------------------------------------------+
  | ``scancel --name JobName``   | To delete/end multiple batch jobs based on the batch job’s name          |
  +------------------------------+--------------------------------------------------------------------------+

See the scancel man page for other available options.

|
