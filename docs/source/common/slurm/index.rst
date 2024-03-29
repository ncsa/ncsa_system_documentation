.. _slurm:

Job Management with Slurm
============================

Many of the NCSA computer systems use the Slurm software stack for job workload management.

.. _partitions:

Partitions (Queues)
-----------------------

Each resource has partitions (queues) with different specifications including maximum number of nodes, maximum wall time, and memory. 
Consult the resource-specific documentation for more information on a system's queues.

- `Delta Queues <https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/running_jobs.html#partitions-queues>`_
- `Hydro Queues <https://ncsa-hydro-documentation.readthedocs-hosted.com/en/latest/partitions_and_job_policies.html#partitions-queues>`_
- `ICC Queues <https://docs.ncsa.illinois.edu/systems/icc/en/proposed_changes/user_guide/running_jobs.html#queues>`_
- `Nightingale Queues <https://ncsa-nightingale.readthedocs-hosted.com/en/latest/user_guide/running_jobs.html#nightingale-queues>`_

.. _access_nodes:

Accessing the Compute Nodes
-------------------------------

Direct SSH access to a compute node in a running job from a login node is enabled once the job has started:

.. code-block::

   $ squeue --job jobid
                JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                12345       cpu     bash   gbauer  R       0:17      1 cn001

Then in a terminal session:

.. code-block::

   $ ssh cn001
   cn001.delta.internal.ncsa.edu (172.28.22.64)
     OS: RedHat 8.4   HW: HPE   CPU: 128x    RAM: 252 GB
     Site: mgmt  Role: compute
   $

See also, :ref:`mon_node`.

.. toctree::
   :maxdepth: 2

   submit
   monitor
   sample-scripts
