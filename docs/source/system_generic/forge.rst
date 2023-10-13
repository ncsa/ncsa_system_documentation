.. _forge_interactive:

Forge (formerly known as DDT: Distributed Debugging Tool
========================================================

Description
~~~~~~~~~~~

Forge from ARM (formerly Allinea Software) is a parallel debugger that
can be used for scalar, multi-threaded and large-scale parallel
applications. The `Allinea
DDT <http://www.allinea.com/products/ddt-support>`__ web page and `users
guide <http:content.allinea.com/downloads/userguide.pdf>`__ is a good
resource for learning more about some of the advanced DDT features.
Helpful `videos <http://www.allinea.com/videos>`__ and
`blogs <http://www.allinea.com/blog>`__ are available from the Allinea
website.

-  DDT Interactive Use (:ref:`forge_interactive`)
-  DDT Offline (:ref:`forge_offline`)
-  DDT Remote (:ref:`forge_remote`)

How to use Forge/DDT
~~~~~~~~~~~~~~~~~~~~

Prerequisites
^^^^^^^^^^^^^

Since Forge/DDT is GUI-based and does not provide command line interface
X11 forwarding must be enabled for your login session. This can be done
by passing -Y flag to ssh:

::

   > ssh -Y bw-duo.ncsa.illinois.edu

NOTE: for **memory debugging** load the memory debugging module for
Forge/DDT BEFORE linking

> module load forge # no memory debugging

or

> module load ddt-memdebug # with memory debugging

Compilation
^^^^^^^^^^^

Add -g flag to enable the generation of debugging information used by
DDT, then (re)compile your program:

Fortran example

::

   > ftn -g test.f90 -o test

C example:

::

   > cc -g test.c -o test

Starting a debug session with DDT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  submit a job through DDT
-  manually launch a program with DDT
-  attach DDT to a running program
-  start a debug session from inside an interactive job

The first three ways begin by loading the ddt module and starting DDT:

::

   > module unload altd ; module unload xalt
   > module load ddt-memdebug # (note the use of the ddt-memdebug module from above)
   > export DDT_NODE_SCAN_TIMEOUT=90
   > export DDT_NO_TIMEOUT=1
   > export DDT_PROCESS_TIMEOUT=0
   > forge

.. image:: ddt-welcome.png

Submit a job through Forge/DDT
''''''''''''''''''''''''''''''

Submits a job, waits until the job is scheduled, and starts a debug
session.

Click on Run and Debug a Program . A new window with expandable tabs
will appear, click on Details... to expand a tab.

.. image:: ddt-run.png

**Application** tab is used to select a program binary, working
directory, arguments and input file.

**MPI**, **OpenMP**, **CUDA** and **Memory Debugging** tabs are used to
allow respective features and set parameters (e.g., number of nodes and
processes per node for an MPI program).

**Queue Submission Parameters** tab is used to change job parameters
such as wall clock time, target queue, etc.

Clicking on Submit button will submit a job to the scheduler, DDT will
wait for the job to start.

.. image:: ddt-submitted.png

DDT will start a debug session automatically as soon as the job starts.

.. image:: ddt_session.png

Manually launch a program
'''''''''''''''''''''''''

Manual launch allows debugging multi-process and multi-executable
programs.

To launch a program manually click on Manually Launch a Program button.

.. image:: ddt-manual.png

Select how many processes you want to debug and click on Listen . At
this point start a program or programs using the following command:

::

   > forge-client <path-to-program-binary>

Note, *ddt-client* command must be issues for each process selected at
the previous window. The above command can also be used in a job
submission script.

.. image:: ddt_connecting1.png

.. image:: ddt_connecting2.png

Forge/DDT will automatically start debugging session once all requested
programs have been launched manually.

Attach to a running program
'''''''''''''''''''''''''''

To attach to a program that is already running, click on the "ATTACH -
Attach to an already running program" button.

(With nodes=256 or more, start ddt from the command line with:
DDT_NODE_SCAN_TIMEOUT=90 ddt )

DDT will scan each of the 64 mom nodes and locate all of the active jobs
that you own, which will appear in the "Automatically-detected jobs"
tab. Select the desired job, and click on the "Attach to [job name]"
button.

.. image:: ddt-attach2.png

Alternatively, you can attach to a specific process that you own on the
"List of all processes" tab.

.. image:: ddt-attach.png

If you are unable to attach to running jobs or processes (e.g., if they
aren't listed), clear out all previously saved Forge settings by
removing the ~/.allinea directory, quit Forge and reload it, and then
try attaching again.

Start a debug session from inside an interactive job
''''''''''''''''''''''''''''''''''''''''''''''''''''

To start DDT from an interactive job, X11 forwarding must be enabled
(*-X* flag):

::

   > qsub -I -X

Once the job has started load the ddt module and start DDT with
*-noqueue* flag:

::

   > module load ddt-memdebug
   > forge -noqueue

Click on Run and Debug a Program . A new window with expandable tabs
will appear. Tabs **Application**, **MPI**, **OpenMP**, **CUDA** and
**Memory Debugging** are the same as described above.

.. image:: ddt-run-noqueue.png

Click on Run button to start a debug session.

.. toctree::

   offline
   remote
