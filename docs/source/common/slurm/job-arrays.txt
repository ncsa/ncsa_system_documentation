.. _jobarrays:

Job Arrays
=============

If you need to submit the same job to the batch system multiple times, instead of issuing one ``sbatch`` command for each individual job, you can submit a job array. 
Job arrays allow you to submit multiple jobs with a single job script using the ``‑‑array`` option to ``sbatch``. 
An optional ``slot limit`` can be specified to limit the number of jobs that can run concurrently in the job array. 
See the ``sbatch`` man page for details. 
The file names for the input, output, and so on, can be varied for each job using the job array index value defined by the Slurm environment variable ``SLURM_ARRAY_TASK_ID``.

A sample batch script that makes use of job arrays is available in the Campus Cluster system at ``/projects/consult/slurm/jobarray.sbatch``.

**A few things to keep in mind:**

  -  Valid specifications for job arrays are:
   
     ``‑‑array 1-10``
   
     ``‑‑array 1,2,6-10``
   
     ``‑‑array 8``
   
     ``‑‑array 1-100%5`` (a limit of 5 jobs can run concurrently) 

  \

  -  You should limit the number of batch jobs in the queues at any one time to 1,000 or less (each job within a job array is counted as one batch job.)

  \

  -  Interactive batch jobs are not supported with job array submissions.

  \

  -  To delete job arrays, see the `Slurm scancel documentation <https://slurm.schedmd.com/job_array.html#scancel>`_.

  \

  - See the `Slurm job arrays documentation <https://slurm.schedmd.com/job_array.html>`_ for more information.

|
