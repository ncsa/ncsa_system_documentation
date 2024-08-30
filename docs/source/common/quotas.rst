.. _quotas:

Quotas
=======

When you run the ``quota`` command, there are **soft quota** and **hard limit** columns. On some systems, these have the same value, and on others, they are different. 

When the soft quota and hard limit are the **same**, this is the limit that you are not allowed to exceed. If you reach it, you will not be able to write to that filesystem area until you reduce the usage to below the limit.

When the soft quota and hard limit are **different**:

- If you exceed the **soft quota**, there is a grace period to reduce the usage below that quota (the default grace period is 7 days, unless otherwise noted for a system).
- If, after the grace period, you are still exceeding the **soft quota**, you will not be able to write to that filesystem area until you reduce the usage to below the **soft quota**.
- You are not allowed to exceed the **hard limit** (there is no grace period). If you reach it, you won't be able to write to that filesystem area until you reduce the usage to below the limit.

The following is a ``quota`` output example from Delta; this example user has access to two projects (bbka and bbkw). Notice that on Delta, the soft quotas and hard limits are different.

.. code-block:: terminal

   [username@dt-login03 ~]$ quota
   Quota usage for user username:
   -----------------------------------------------------------------------------------------------
   |        Directory Path        |  User   |  User   |  User   |   User   |   User   |   User   |
   |                              |  Block  |  Soft   |  Hard   |   File   |   Soft   |   Hard   |
   |                              |  Used   |  Quota  |  Limit  |   Used   |   Quota  |   Limit  |
   -----------------------------------------------------------------------------------------------
   | /u/username                  | 2520M   | 90600M  | 95368M  | 84734    | 490k     | 500k     |
   -----------------------------------------------------------------------------------------------
   
   Quota usage for allocations user username is a member of:
   --------------------------------------------------------------------------------------------------------------
   |        Directory Path        | Allocation | Allocation | Allocation | Allocation | Allocation | Allocation |
   |                              |   Block    |    Soft    |    Hard    |    File    |    Soft    |    Hard    |
   |                              |   Used     |    Quota   |    Limit   |    Used    |    Quota   |    Limit   |
   --------------------------------------------------------------------------------------------------------------
   | /projects/bbka               | 1.275T     | 1.953T     | 2.002T     | 308133     | 750000     | 3000000    |
   | /projects/bbkw               | 44k        | 500G       | 550G       | 11         | 375000     | 412500     |
   --------------------------------------------------------------------------------------------------------------
   | /scratch/bbka                | 6.44T      | 46.57T     | 51.22T     | 5050378    | 85000000000 | 93500000000 |
   | /scratch/bbkw                | 27.99M     | 500G       | 550G       | 45         | 850000     | 935000     |
   --------------------------------------------------------------------------------------------------------------
   [username@dt-login03 ~]$ 

|
