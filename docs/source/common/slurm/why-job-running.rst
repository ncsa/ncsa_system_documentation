Why Jobs (Don't) Run: Scheduling, Priority, FairShare
==========================================================

This page discusses generally why jobs get run in the order that they do on NCSA systems, why your job might or might not run in a certain amount of time, and what you can do about it.  

The scheduler on each system runs jobs with a strategy to keep the system well-utilized.  Job priority, which may take into factor things like the age of the job or the size of the job also plays a factor.  Sysadmins sometimes adjust priority factors on the fly to keep jobs flowing through the system, so sometimes the apparent priority of a job will shift.  

The best way to get your jobs to run is to request the resources they need, but not very much more.  Jobs that are smaller in nodes and shorter in time are easier to schedule.  For instance, if you have an application that runs between 4 and 5 hours, write your job script to request 5.5 or maybe 6 hours, not 12 or 24.  A job requesting 6 hours of run time is much easier to schedule than one that requests 12 hours, and is consequently likely to run sooner.  

Reasons a Pending Job Isn't Running
-------------------------------------

Use the following command to get a list of your jobs (replace ``<username>`` with your username):

.. code-block::
   
   squeue -u <username>

The right column will contain a reason for each of the pending jobs. 

Priority
~~~~~~~~~~~

**There is at least one pending job with a higher priority than this job.** 
The priority for a job depends on a couple of factors, the biggest of which is recent usage. 
You are most likely seeing this reason after running some combination of a large number of jobs, jobs using a lot of resources, or jobs that run for a long time. 
The recent usage factor slowly decays in a two-week period, which means any usage prior to two weeks before the job was submitted will not impact the priority of the job. 
You can `check your recent HAL usage <https://go.illinois.edu/halfairshare>`_.

Jobs that are pending for this reason may remain pending for a long time if the recent usage factor has reduced your priority below most of the active users. 
If there is a sufficient difference between someone's recent usage and yours, and the difference in the recent usage factor is large enough to exceed the waiting time factor, their job may receive a higher priority and run before your job, even if it is submitted after your job.

ReqNodeNotAvail
~~~~~~~~~~~~~~~~~

**Some of the nodes specifically requested by the job aren't available.** The nodes could be unavailable for one of the following reasons:

- Running jobs with a higher priority.
- Reserved in a reservation.
- Manually drained by an administrator for maintenance.
- Unavailable due to some issues. 

This job will run when all the requested nodes become available.

Resources
~~~~~~~~~~~

**This job is at the front of the queue, but there are not enough resources for it to start running.** 
This job will start running as soon as enough resources become available. 
The priority calculation favors large jobs, so when resources gradually become available, smaller jobs with a similar recent usage factor won't run before this job and take away the available resource. 
Note that if someone has much lower recent usage than you do, their jobs can still run before your job, because the bonus from their recent usage factor can exceed the bonus from your job size factor.

AssocGrpGRES
~~~~~~~~~~~~~~

**This means you have reached the limit of resources that can be allocated to one user at any given time.** 
There are three limits in place: 

- Maximum of 5 running jobs.
- Maximum of 5 nodes running jobs.
- Maximum of 16 GPUs running jobs. 

This job will run as soon as some of your running jobs finish and free up the resources.
