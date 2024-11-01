.. _depend-constraints:

Job Dependencies and Contraints
=================================

.. _jobdepend:

Job Dependencies
-------------------

Slurm job dependencies allow you to set the execution order that your queued jobs run in. 
Job dependencies are set by using the ``‑‑dependency`` option with the syntax, ``‑‑dependency=<dependency type>:<JobID>``. 
Slurm places the jobs in *Hold* state until they are eligible to run.

The following are examples on how to specify job dependencies using the ``afterany`` dependency type, which indicates to Slurm that the dependent job should become eligible to start only after the specified job has completed.

On the command line:

.. code-block:: terminal

   [golubh1 ~]$ sbatch --dependency=afterany:<JobID> jobscript.sbatch

In a job script:

.. code-block:: terminal

   #!/bin/bash
   #SBATCH --time=00:30:00
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=16
   #SBATCH --account=account_name    # <- replace "account_name" with an account available to you
   #SBATCH --job-name="myjob"
   #SBATCH --partition=secondary
   #SBATCH --output=myjob.o%j
   #SBATCH --dependency=afterany:<JobID>

In a shell script that submits batch jobs:

.. code-block:: terminal

   #!/bin/bash
   JOB_01=`sbatch jobscript1.sbatch |cut -f 4 -d " "`
   JOB_02=`sbatch --dependency=afterany:$JOB_01 jobscript2.sbatch |cut -f 4 -d " "`
   JOB_03=`sbatch --dependency=afterany:$JOB_02 jobscript3.sbatch |cut -f 4 -d " "`
   ...

Generally, the recommended dependency types to use are ``after``, ``afterany``, ``afternotok``, and ``afterok``. 
There are more dependency types, however the dependencies that work based on batch job error codes may not behave as expected because of the difference between a batch job error and application errors. 
See the dependency section of the ``sbatch`` man page for additional information.

.. _job-contraints:

Job Constraints
----------------

Use the ``--constraint`` option to specify required *features* for a job. Refer to the `Slurm srun -\-constraint documentation <https://slurm.schedmd.com/srun.html#OPT_constraint>`_ for more details. (You can also find the same information in the `Slurm sbatch documentation <https://slurm.schedmd.com/sbatch.html#OPT_constraint>`_ and `Slurm salloc documentation <https://slurm.schedmd.com/salloc.html#OPT_constraint>`_.) 

Features include:

- CPU type 
- GPU type
- Memory 
- Interconnect 

Run the ``sinfo`` command below to see a full list of features for nodes that are in queues that you can submit to:

.. code-block:: terminal

   sinfo -N --format="%R (%N): %f" -S %R | more 

If a constraint(s) cannot be satisfied, your job will *not* run and ``squeue`` will return ``BadConstraints``; refer to the `Slurm squeue documentation <https://slurm.schedmd.com/squeue.html#OPT_BadConstraints>`_.

|
