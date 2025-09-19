.. _interactive:

Interactive Jobs
==================

Use :ref:`srun` for interactive use of a compute node, ``srun`` will run a single command through Slurm on a compute node. ``srun`` blocks, which means that it will wait until Slurm has scheduled compute resources, and when it returns, the job is complete.

:ref:`salloc`: is also interactive, use ``salloc`` when you want to reserve compute resources for a period of time and interact with them using multiple commands. Each command you type after your salloc session begins will run on the login node if it is just a normal command, or on your reserved compute resources if prefixed with ``srun``.  Run ``exit`` when you are finished with a ``salloc`` allocation, if you want to end it before the time expires.

.. _srun:

srun
-----

Command Line
~~~~~~~~~~~~~~~

Instead of queuing up a batch job to run on the compute nodes, you can request that the job scheduler allocate you to a compute node **now** and log you onto it. These are called **interactive batch jobs**. Projects that have dedicated interactive nodes, do not need to go through the scheduler; members of these projects just log in directly to their nodes.

To launch an interactive batch job using the job scheduler with the default values for the job resources (nodes, cores, memory, and so on), run the following command; replace ``ALL_ACCT`` with the name of your allocation account:

.. code-block:: terminal

   srun -A ALL_ACCT --pty bash 

.. warning::
   Run ``exit`` to end the interactive job **as soon as you're done**. If you leave the job running, even if you are not running any processes, your allocation account is being charged for the time.

To specify resources for your interactive batch job the ``srun`` command syntax should look similar to the following; replace ``ACCT_NAME`` with the name of your charge account. This example will run an interactive batch job in the CPU partition (queue) with a wall clock limit of **30 minutes**, using **1 node** and **16 cores per node**. You can also use other ``sbatch`` options:

.. code-block:: terminal

  srun --account=ACCT_NAME --partition=cpu --time=00:30:00 --nodes=1 --ntasks-per-node=16 --pty /bin/bash

As another example, the following command will run an interactive job, on **Delta**, in the gpuA100x4 or gpuA40x4 partition with a wall-clock time limit of 30 minutes, using one node and 16 cores per node and 1 GPU:

.. code-block:: terminal

   srun -A ALL_ACCT --time=00:30:00 --nodes=1 --ntasks-per-node=16 \
   --partition=gpuA100x4,gpuA40x4 --gpus=1 --mem=16g --pty /bin/bash

After you enter the command, you will have to wait for Slurm to start the job. You will see output similar to:

.. code-block:: terminal

   srun: job 123456 queued and waiting for resources

Specifying a small number of nodes for smaller amounts of time should shorten the wait time because the job will backfill among larger jobs. Once the job starts, you will see something similar to the below and will be presented with an interactive shell prompt on the launch node. At this point, you can use the appropriate command(s) to start your program.

.. code-block:: terminal

   srun: job 123456 has been allocated resources

When you are done with your interactive batch job session, use the ``exit`` command to end the job.

srun Examples
$$$$$$$$$$$$$$$

- Single core with 16GB of memory, with one task on a CPU node

  .. code-block:: terminal

     srun --account=account_name --partition=cpu-interactive \
       --nodes=1 --tasks=1 --tasks-per-node=1 \
       --cpus-per-task=4 --mem=16g \
       --pty bash

- Single core with 20GB of memory, with one task on a *Delta* A40 GPU node

  .. code-block:: terminal

     srun --account=account_name --partition=gpuA40x4-interactive \
       --nodes=1 --gpus-per-node=1 --tasks=1 \
       --tasks-per-node=16 --cpus-per-task=1 --mem=20g \
       --pty bash 

Batch Script
~~~~~~~~~~~~~~

Inside a batch script if you want to run multiple copies of a program you can use the ``srun`` command followed by the name of the executable: 

.. code-block:: terminal

   srun ./a.out

By default, the total number of copies run is equal to number of cores specified in the batch job resource specification.
You can use the ``-n``  flag/option with the ``srun`` command to specify the number of copies of a program that you would like to run; the value for the ``-n`` flag/option must be less than or equal to the number of cores specified for the batch job.

.. code-block:: terminal

   srun -n 10 ./a.out

.. _salloc:

salloc
--------

While interactive like ``srun``, ``salloc`` allocates compute resources for you, while leaving your shell on the login node. Run commands on the login node as usual, use ``exit`` to end a salloc session early, and use ``srun`` with no extra flags to launch processes on the compute resources.

.. code-block:: terminal

   $ salloc --mem=16g --nodes=1 --ntasks-per-node=1 --cpus-per-task=2 \
     --partition=gpuA40x4-interactive,gpuA100x4-interactive \
     --account=your_account_name --time=00:30:00 --gpus-per-node=1
   salloc: Pending job allocation 2323230
   salloc: job 2323230 queued and waiting for resources
   salloc: job 2323230 has been allocated resources
   salloc: Granted job allocation 2323230
   salloc: Waiting for resource configuration
   salloc: Nodes gpub073 are ready for job
   $ hostname #<-- on the login node
   dt-login03.delta.ncsa.illinois.edu
   $ srun bandwidthTest --htod #<-- on the compute resource, honoring your salloc settings
   CUDA Bandwidth Test - Starting...
   Running on...

   Device 0: NVIDIA A40
   Quick Mode

   Host to Device Bandwidth, 1 Device(s)
   PINNED Memory Transfers
   Transfer Size (Bytes)        Bandwidth(GB/s)
   32000000                     24.5

   Result = PASS
   $ exit
   salloc: Relinquishing job allocation 2323230

MPI Interactive Jobs: Use salloc Followed by srun
---------------------------------------------------

Interactive jobs are already a child process of ``srun``, therefore, one cannot srun (or mpirun) applications from within them. 
Within standard batch jobs submitted via ``sbatch``, use ``srun`` to launch MPI codes. 
For true interactive MPI, use ``salloc`` in place of srun shown above, then **srun my_mpi.exe** after you get a prompt from salloc (``exit`` to end the salloc interactive allocation).

.. raw:: html

   <details>
   <summary><a><b>interactive MPI, salloc and srun</b> <i>(click to expand/collapse)</i></a></summary>

.. code-block:: terminal

   [arnoldg@dt-login01 collective]$ cat osu_reduce.salloc
   salloc --account=bbka-delta-cpu --partition=cpu-interactive \
     --nodes=2 --tasks-per-node=4 \
     --cpus-per-task=2 --mem=0

   [arnoldg@dt-login01 collective]$ ./osu_reduce.salloc
   salloc: Pending job allocation 1180009
   salloc: job 1180009 queued and waiting for resources
   salloc: job 1180009 has been allocated resources
   salloc: Granted job allocation 1180009
   salloc: Waiting for resource configuration
   salloc: Nodes cn[009-010] are ready for job
   [arnoldg@dt-login01 collective]$ srun osu_reduce

   # OSU MPI Reduce Latency Test v5.9
   # Size       Avg Latency(us)
   4                       1.76
   8                       1.70
   16                      1.72
   32                      1.80
   64                      2.06
   128                     2.00
   256                     2.29
   512                     2.39
   1024                    2.66
   2048                    3.29
   4096                    4.24
   8192                    2.36
   16384                   3.91
   32768                   6.37
   65536                  10.49
   131072                 26.84
   262144                198.38
   524288                342.45
   1048576               687.78
   [arnoldg@dt-login01 collective]$ exit
   exit
   salloc: Relinquishing job allocation 1180009
   [arnoldg@dt-login01 collective]$ 

.. raw:: html

   </details>
|

Interactive X11 Support
-------------------------

To run an X11 based application on a compute node in an interactive session, the use of the **--x11** switch with ``srun`` is needed. 
For example, to run a single core job that uses 1G of memory with X11 (in this case an xterm) do the following:

.. code-block:: terminal

   srun -A abcd-delta-cpu  --partition=cpu-interactive \
     --nodes=1 --tasks=1 --tasks-per-node=1 \
     --cpus-per-task=2 --mem=16g \
     --x11  xterm

|
