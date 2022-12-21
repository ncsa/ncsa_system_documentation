.. container::
   :name: main-header

   .. container:: pagetitle with-breadcrumbs
      :name: title-heading

      .. rubric:: DDT Offline debugging for batch jobs that crash or
         hang
         :name: ddt-offline-debugging-for-batch-jobs-that-crash-or-hang

      .. rubric:: Using DDT in offline node is fairly straightforward.
         DDT will generate a backtrace and also show the local variables
         for the current routine. Follow these steps in your job script
         to get DDTs offline mode to work with a program that crashes
         (as an alternative to Cray's ATP). You could also use this
         technique with a hanging job by sending it a SIGABRT or SIGSEGV
         via qsig or apkill .
         :name: title-text
         :class: with-breadcrumbs

      .. rubric:: Scenario 1: ddt -offline with a MPI cpu-only code
         :name: scenario-1-ddt--offline-with-a-mpi-cpu-only-code

      .. table:: steps to use ddt -offline

         +-----------------------------------------------------------------------+
         | #!/bin/bash                                                           |
         |                                                                       |
         | #PBS -lnodes=2:ppn=32,walltime=00:10:00                               |
         |                                                                       |
         | **. /opt/modules/default/init/bash # enable module commands**         |
         |                                                                       |
         | # unload conflicting modules, disable Cray ATP                        |
         |                                                                       |
         | module unload darshan                                                 |
         |                                                                       |
         | export ATP_ENABLED=0                                                  |
         |                                                                       |
         | # load the ddt module and optionally firefox for viewing              |
         | filename.html from a login node                                       |
         |                                                                       |
         | module load ddt-memdebug                                              |
         |                                                                       |
         | module load firefox # on login node                                   |
         |                                                                       |
         | # replace aprun with "ddt -offline filename -noqueue ... " use        |
         | filename.txt for a text report                                        |
         |                                                                       |
         | # pass extra aprun arguments with the -mpiargs flag and double quotes |
         |                                                                       |
         | export DDT_NODE_SCAN_TIMEOUT=90                                       |
         |                                                                       |
         | export DDT_NO_TIMEOUT=1                                               |
         |                                                                       |
         | export DDT_PROCESS_TIMEOUT=0                                          |
         |                                                                       |
         | cd ${PBS_O_WORKDIR} # the binary was in the directory where job was   |
         | submitted                                                             |
         |                                                                       |
         | ddt -offline myfile.html -noqueue-n 32 -mpiargs "-N 16 -d 1"          |
         | ./hello_world_bug                                                     |
         +-----------------------------------------------------------------------+

      After the program runs, you can copy the html file back to your
      local machine or view it on a login node with firefox. The
      equivalent text file report is also shown:

      .. container::

      .. container::

         |image1|

      .. container::

      .. container::

         .. table:: equivalent output with myfile.txt

            +-----------------------------------------------------------------------+
            | arnoldg@nid00014 13:57 ~/c \___--Cray- $ cat myfile.txt               |
            |                                                                       |
            | message (0-31): Launching program                                     |
            | /mnt/abc/u/staff/arnoldg/c/hello_world_bug                            |
            |                                                                       |
            | message (0-31): at Thu Aug 14 13:54:49 2014                           |
            |                                                                       |
            | message (0-31): Executable modified on Thu Aug 14 08:22:48 2014       |
            |                                                                       |
            | message (0-31): Startup complete.                                     |
            |                                                                       |
            | message (n/a): Select process group All                               |
            |                                                                       |
            | message: Current Stack                                                |
            |                                                                       |
            | message: #1 \__libc_start_main (main=0x401ac0 <main>, argc=1,         |
            | ubp_av=0x7fffffff0a78, init=0x5728e0 <__libc_csu_init>, fini=0x5728a0 |
            | <__libc_csu_fini>, rtld_fini=0, stack_end=0x7fffffff0a68) at          |
            | /usr/src/packages/BUILD/glibc-2.11.3/csu/libc-start.c:201 (at         |
            | 0x0000000000572391)                                                   |
            |                                                                       |
            | message: #0 \__libc_csu_init (argc=1, argv=0x7fffffff0a78,            |
            | envp=0x7fffffff0a88) at                                               |
            | /usr/src/packages/BUILD/glibc-2.11.3/csu/elf-init.c:123               |
            |                                                                       |
            | message (n/a): /mnt/abc/u/staff/arnoldg/c/hello_world_bug.c is not    |
            | tracked by a version control system                                   |
            |                                                                       |
            | message: Stacks                                                       |
            |                                                                       |
            | message: Processes Function                                           |
            |                                                                       |
            | message: 0-31 \__libc_start_main (libc-start.c:201)                   |
            |                                                                       |
            | message: 0-31 \__libc_csu_init (elf-init.c:123)                       |
            |                                                                       |
            | message: Locals                                                       |
            |                                                                       |
            | message: argc: 1 argv: 0x7fffffff0a78 envp: 0x7fffffff0a88 i: 16      |
            |                                                                       |
            | message (0-31): Play                                                  |
            |                                                                       |
            | message (3): Process stopped in main (hello_world_bug.c:25) with      |
            | signal SIGSEGV (Segmentation fault).                                  |
            |                                                                       |
            | message (3): Reason/Origin: address not mapped to object (attempt to  |
            | access invalid address)                                               |
            |                                                                       |
            | message (3): Your program will probably be terminated if you          |
            | continue.                                                             |
            |                                                                       |
            | message (3): You can use the stack controls to see what the process   |
            | was doing at the time.                                                |
            |                                                                       |
            | message: Stacks                                                       |
            |                                                                       |
            | message: Processes Function                                           |
            |                                                                       |
            | message: 3 main (hello_world_bug.c:25)                                |
            |                                                                       |
            | message (n/a): Select process 3                                       |
            |                                                                       |
            | message: Current Stack                                                |
            |                                                                       |
            | message: #0 main (argc=1, argv=0x7fffffff0a78) at                     |
            | /mnt/abc/u/staff/arnoldg/c/hello_world_bug.c:25 (at                   |
            | 0x0000000000401bc9)                                                   |
            |                                                                       |
            | message: Locals                                                       |
            |                                                                       |
            | message: a: argc: 1 argv: 0x7fffffff0a78 core: 1077483333 i: 7404     |
            | len: -933688543 name: "\253\252\252\252\252\252\032@" rank:           |
            | 1431655765 size: 1077548610                                           |
            |                                                                       |
            | message (3): Play                                                     |
            |                                                                       |
            | error (Other): \_pmiu_daemon(SIGCHLD): [NID 00002] [c0-0c0s1n0] [Thu  |
            | Aug 14 13:55:09 2014] PE RANK 3 exit signal Segmentation fault        |
            |                                                                       |
            | error (Other): [NID 00002] 2014-08-14 13:55:10 Apid 238591: initiated |
            | application termination                                               |
            |                                                                       |
            | output (Other): rank 1 of 32 on nid00002 core 1                       |
            |                                                                       |
            | output (Other): rank 0 of 32 on nid00002 core 0                       |
            |                                                                       |
            | output (Other): rank 12 of 32 on nid00002 core 12                     |
            |                                                                       |
            | output (Other): rank 13 of 32 on nid00002 core 13                     |
            |                                                                       |
            | output (Other): rank 8 of 32 on nid00002 core 8                       |
            |                                                                       |
            | output (Other): rank 9 of 32 on nid00002 core 9                       |
            |                                                                       |
            | output (Other): rank 4 of 32 on nid00002 core 4                       |
            |                                                                       |
            | output (Other): rank 15 of 32 on nid00002 core 15                     |
            |                                                                       |
            | output (Other): rank 7 of 32 on nid00002 core 7                       |
            |                                                                       |
            | output (Other): rank 6 of 32 on nid00002 core 6                       |
            |                                                                       |
            | output (Other): rank 3 of 32 on nid00002 core 3                       |
            |                                                                       |
            | output (Other): rank 5 of 32 on nid00002 core 5                       |
            |                                                                       |
            | output (Other): rank 2 of 32 on nid00002 core 2                       |
            |                                                                       |
            | output (Other): rank 14 of 32 on nid00002 core 14                     |
            |                                                                       |
            | output (Other): rank 10 of 32 on nid00002 core 10                     |
            |                                                                       |
            | output (Other): rank 11 of 32 on nid00002 core 11                     |
            |                                                                       |
            | output (Other): rank 25 of 32 on nid00003 core 9                      |
            |                                                                       |
            | output (Other): rank 24 of 32 on nid00003 core 8                      |
            |                                                                       |
            | output (Other): rank 17 of 32 on nid00003 core 1                      |
            |                                                                       |
            | output (Other): rank 21 of 32 on nid00003 core 5                      |
            |                                                                       |
            | output (Other): rank 23 of 32 on nid00003 core 7                      |
            |                                                                       |
            | output (Other): rank 28 of 32 on nid00003 core 12                     |
            |                                                                       |
            | output (Other): rank 29 of 32 on nid00003 core 13                     |
            |                                                                       |
            | output (Other): rank 20 of 32 on nid00003 core 4                      |
            |                                                                       |
            | output (Other): rank 22 of 32 on nid00003 core 6                      |
            |                                                                       |
            | output (Other): rank 18 of 32 on nid00003 core 2                      |
            |                                                                       |
            | output (Other): rank 19 of 32 on nid00003 core 3                      |
            |                                                                       |
            | output (Other): rank 16 of 32 on nid00003 core 0                      |
            |                                                                       |
            | output (Other): rank 31 of 32 on nid00003 core 15                     |
            |                                                                       |
            | output (Other): rank 30 of 32 on nid00003 core 14                     |
            |                                                                       |
            | output (Other): rank 26 of 32 on nid00003 core 10                     |
            |                                                                       |
            | output (Other): rank 27 of 32 on nid00003 core 11                     |
            |                                                                       |
            | message (n/a): Every process in your program has terminated.          |
            |                                                                       |
            | output (aprun): Application 238591 exit codes: 139                    |
            |                                                                       |
            | output (aprun): Application 238591 resources: utime ~2s, stime ~21s,  |
            | Rss ~6592, inblocks ~12876, outblocks ~28782                          |
            |                                                                       |
            | message (n/a): Select process 0                                       |
            |                                                                       |
            | arnoldg@nid00014 13:57 ~/c \___--Cray- $                              |
            +-----------------------------------------------------------------------+

         .. rubric:: Scenario 2: ddt -offline with MPI cpu+gpu code
            :name: scenario-2-ddt--offline-with-mpi-cpugpu-code

         With ddt version 4.2.2 or later, the -offline option supports
         gpu debugging. The following launch command was used in the
         batch script to trace a kernel invocation and variable on the
         gpu. A snapshot of the resulting .html output follows.

         +-----------------------------------------------------------------------+
         | ddt -offline test1.html -noqueue -n 1 \\                              |
         |                                                                       |
         | -trace-at simpleMPI.cu:42,output[tid] \\                              |
         |                                                                       |
         | ./simpleMPI                                                           |
         +-----------------------------------------------------------------------+

         .. image:: /image/image_gallery?uuid=858ab7e0-ff5f-476f-b159-6d1dfd47e037&groupId=10157&t=1412879532476

         See also:

         http://www.allinea.com/user-guide/forge/OfflineDebugging.html#x20-21200016

.. |image1| image:: /image/image_gallery?uuid=24df3689-d5c4-4dd3-a0b2-dcb5fe11bc29&groupId=10157&t=1409164417544
