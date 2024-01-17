Frequently Asked Questions
============================

Why isn't my job running?
---------------------------

There are a few common reasons that your job may not be running. If your issue isn't resolved by any of the below, submit a support request (:ref:`help`).

System Reservation Overlap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
Slurm will block your job from starting if there is a reservation scheduled to start before your job would finish. 
If a reservation is blocking your job from starting, the ``squeue`` command will return a message like ``ReqNodeNotAvail, Reserved for maintenance`` for your job. 
You may be able to shorten the runtime of your job to fit in before the reservation starts.

