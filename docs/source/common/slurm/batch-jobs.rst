.. _batch-jobs:

Batch Jobs
=============

.. _sbatch:

A "batch job" is a collection of computational work that a user wants to be done on a computational cluster.  The steps to be done is defined in a "batch script".  When a cluster system provisions and then reserves resources for a batch job, the batch system runs the batch script on the user's behalf, which then directs (and potentially montiors) the computational work, and exits when the work is done.  

Use batch scripts for jobs that are debugged, ready to run, and don't require interaction.
For mixed resource heterogeneous jobs, see the `Slurm heterogeneous jobs documentation <https://slurm.schedmd.com/heterogeneous_jobs.html#submitting>`_. 

sbatch
--------

Batch jobs are submitted through a *job script* (as in the :ref:`examples`) using the ``sbatch`` command. 
Job scripts generally start with a series of Slurm *directives* that describe requirements of the job, such as number of nodes and wall time required, to the batch system/scheduler. Slurm directives can also be specified as options on the sbatch command line; command line options take precedence over those in the script. 
The rest of the batch script consists of user commands.

The syntax for submitting a batch job with ``sbatch`` is:

.. code-block:: terminal

  sbatch [list of sbatch options] script_name

.. table:: main ``sbatch`` options

  +-------------------------+------------------------------------------------------------------+
  | Option                  | Description                                                      |
  +=========================+==================================================================+
  | ``--time=time``         | time = maximum wall clock time (d-hh:mm:ss) [default: 30 minutes]|
  +-------------------------+------------------------------------------------------------------+
  | ``--nodes=n``           | Total number of nodes for the batch job.                         |
  |                         |                                                                  |
  |                         | n = number of 64-core nodes [default: 1 node]                    |
  +-------------------------+------------------------------------------------------------------+
  | ``--ntasks=p``          | Total number of cores for the batch job.                         |
  |                         |                                                                  |
  |                         | p = number of cores per job to use (1 - 64) [default: 1 core]    |
  +-------------------------+------------------------------------------------------------------+
  | ``--ntasks-per-node=p`` | Number of cores per node.                                        |
  |                         |                                                                  |
  |                         | p = number of cores per node to use (1 - 64) [default: 1 core]   |
  +-------------------------+------------------------------------------------------------------+

**Example:**

  .. code-block:: terminal

     --time=00:30:00 
     --nodes=2 
     --ntasks=32

  or 

  .. code-block:: terminal

     --time=00:30:00 
     --nodes=2 
     --ntasks-per-node=16

See the `sbatch page at SchedMD <https://slurm.schedmd.com/sbatch.html>`_ for additional information.

Useful Batch Job Environment Variables
-----------------------------------------

.. table:: useful batch job environment variables

  +-------------------------+----------------------------+-------------------------------------------------------------------------+
  | Description             | Slurm Environment Variable | Detail Description                                                      |
  +=========================+============================+=========================================================================+
  | Array JobID             | $SLURM_ARRAY_JOB_ID        | Each member of a job array is assigned a unique identifier.             |
  |                         |                            |                                                                         |
  |                         | $SLURM_ARRAY_TASK_ID       |                                                                         |
  +-------------------------+----------------------------+-------------------------------------------------------------------------+
  | Job Submission Directory| $SLURM_SUBMIT_DIR          | By default, jobs start in the directory that the job was submitted      |
  |                         |                            |                                                                         |
  |                         |                            | from. So the "cd $SLURM_SUBMIT_DIR" command is not needed.              |
  +-------------------------+----------------------------+-------------------------------------------------------------------------+
  | JobID                   | $SLURM_JOB_ID              | Job identifier assigned to the job.                                     |
  +-------------------------+----------------------------+-------------------------------------------------------------------------+
  | Machine(node) list      | $SLURM_NODELIST            | Variable name that contains the list of nodes assigned to the batch job.|
  +-------------------------+----------------------------+-------------------------------------------------------------------------+

See the sbatch man page for additional environment variables available.

|
