.. _allocations:

NCSA Allocations
===================

.. note::

   :ref:`by-resource` - Start here if you know which resource you want to use.

   :ref:`by-method` - Explore the available allocation programs/methods.

   NCSA XRAS portal guides:

     - :ref:`xras-new`
     - :ref:`xras-renew`

.. toctree::
   :maxdepth: 1
   :hidden:

   by-resource
   by-method
   xras-new
   xras-renew

.. _resource-summary:

NCSA Resources Summary
------------------------

NCSA offers access to a variety of resources, browse the resources below to find one that best fits your research needs.

.. table:: NCSA Resources Summary
   :widths: 10 10 40 40 

   ================================== ================= ================================================================================================= ===================================
   Resource Name                      Resource Type     Primary Use Cases                                                                                 User Documentation and Support
   ================================== ================= ================================================================================================= ===================================
   Delta                              HPC               Supports machine learning frameworks like Pytorch, TensorFlow, and others                         `Delta hardware/storage`_
   Illinois Campus Cluster            Archive Storage   Supports machine learning frameworks like Pytorch, TensorFlow, and others, and others, and others `Campus Cluster hardware/storage`_
   ================================== ================= ================================================================================================= ===================================


.. table:: NCSA Resources Summary
   :widths: 10 10 40 40 

   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Resource Name                   | Resource Type   | Primary Use Cases                                                            | User Documentation and Support                        |
   +=================================+=================+==============================================================================+=======================================================+
   | Delta                           | HPC             | CPU:                                                                         | - `Delta hardware/storage`_                           |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - General purpose computation                                                |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Engineering modeling and simulation                                        | - :ref:`Accessing Delta <allocate-delta>`             |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Data analysis and analytics                                                |                                                       |
   |                                 |                 |                                                                              | - `Delta user documentation`_                         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | GPU:                                                                         |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Accelerated computation                                                    | - `Delta user support`_                               | 
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Transition from CPU-only to GPU                                            |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Transition to hybrid CPU-GPU models                                        |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Supports machine learning frameworks                                       |                                                       |
   |                                 |                 |   like Pytorch, TensorFlow, and others                                       |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Visualization and ray tracing                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | `DeltaAI`_                      | HPC             | Coming Soon!                                                                 | Coming Soon!                                          |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Machine learning frameworks like:                                          |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |   - PyTorch                                                                  |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |   - TensorFlow                                                               |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |   - and others                                                               |                                                       | 
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Granite                         | Archive Storage | - Store infrequently accessed data                                           | - `Granite hardware/storage`_                         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Disaster recovery                                                          | - :ref:`Accessing Granite <allocate-granite>`         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Archive datasets                                                           | - `Granite user documentation`_                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Granite user support`_                             |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | HAL                             | HPC             | - Machine learning frameworks like:                                          | - `HAL hardware/storage`_                             |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |   - PyTorch                                                                  | - :ref:`Accessing HAL <allocate-hal>`                 |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |   - TensorFlow                                                               | - `HAL user documentation`_                           |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |   - and others                                                               | - `HAL user support`_                                 |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Hydro                           | HPC             | Priority use for NFI projects.                                               | - `Hydro hardware/storage`_                           |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - :ref:`Accessing Hydro <allocate-hydro>`             |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Hydro user documentation`_                         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Hydro user support`_                               |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Illinois Campus Cluster         | HPC             | `Campus Cluster use cases <https://campuscluster.illinois.edu/science/>`_    | - `Campus Cluster hardware/storage`_                  |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - :ref:`Accessing Campus Cluster <allocate-icc>`      |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Campus Cluster user documentation`_                | 
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Campus Cluster user support`_                      | 
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Illinois Computes               | JupyterLab      | Coming soon!                                                                 | - `ICRN hardware/storage`_                            |
   |                                 |                 |                                                                              |                                                       |
   | Research Notebooks              |                 |                                                                              | - `Accessing ICRN`_                                   |
   |                                 |                 |                                                                              |                                                       |
   | (ICRN)                          |                 |                                                                              | - `ICRN user documentation`_                          |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `ICRN user support`_                                |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Illinois HTC                    | HTC             | Coming soon!                                                                 | - `Illinois HTC hardware/storage`_                    |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - :ref:`Accessing Illinois HTC <allocate-htc>`        |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Illinois HTC user documentation`_                  |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Illinois HTC user support`_                        | 
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Innovative Systems Lab          |                 | Coming soon!                                                                 | - `ISL info`_                                         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Jade                            | ePHI/CUI Archive| - Store infrequently accessed data                                           | - `Jade hardware/storage`_                            |
   |                                 |                 |                                                                              |                                                       |
   |                                 | Storage         |                                                                              | - :ref:`Accessing Jade <allocate-jade>`               |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Archive datasets                                                           | - `Jade user documentation`_                          |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Jade user support`_                                |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Nightingale                     | HIPAA HPC       | Projects working with:                                                       | - `Nightingale hardware/storage`_                     |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - HIPAA                                                                      | - :ref:`Accessing Nightingale <allocate-nightingale>` | 
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - CUI                                                                        | - `Nightingale user documentation`_                   |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Other protected or sensitive data                                          | - `Nightingale user support`_                         |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Radiant                         | HPC             | `Radiant use cases`_                                                         | - `Radiant hardware/storage`_                         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - :ref:`Accessing Radiant <allocate-nightingale>`     |   
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Radiant user documentation`_                       | 
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Radiant user support`_                             |     
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Research Computing              | Support         | Coming Soon!                                                                 | - `RCCS info`_                                        |
   |                                 |                 |                                                                              |                                                       |
   | Collaborative Services          |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   | (RCCS)                          |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              |                                                       |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Taiga                           | Storage         | - Active Research and Project Data                                           | - `Taiga hardware/storage`_                           |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 | - Visualization data                                                         | - :ref:`Accessing Taiga <allocate-taiga>`             |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Taiga user documentation`_                         |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `Taiga user support`_                               |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | vForge                          | HTC             | Starting point for NCSA’s industry partners                                  | - `vForge hardware/storage`_                          |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - :ref:`Accessing vForge <allocate-vforge>`           |
   |                                 |                 |                                                                              |                                                       |
   |                                 |                 |                                                                              | - `vForge user support`_                              |
   +---------------------------------+-----------------+------------------------------------------------------------------------------+-------------------------------------------------------+

.. _Radiant use cases: https://docs.google.com/spreadsheets/d/1VCg9hZVzsY_qiX_FGY_k0LDLZl_HPPkEJhOgv31YNHo/edit#gid=0

.. _Delta hardware/storage: https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/architecture.html

.. _Delta user documentation: https://docs.ncsa.illinois.edu/systems/delta/

.. _Delta user support: https://docs.ncsa.illinois.edu/systems/delta/en/latest/help.html

.. _DeltaAI: https://www.ncsa.illinois.edu/ncsa-awarded-10-million-for-deltaai/

.. _DeltaAI hardware/storage: https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/architecture.html

.. _DeltaAI user documentation: https://docs.ncsa.illinois.edu/systems/delta/

.. _DeltaAI user support: https://docs.ncsa.illinois.edu/systems/delta/en/latest/help.html

.. _Granite hardware/storage: https://docs.ncsa.illinois.edu/systems/granite/en/latest/user-guide/architecture.html

.. _Granite user documentation: https://docs.ncsa.illinois.edu/systems/granite/

.. _Granite user support: https://docs.ncsa.illinois.edu/systems/granite/en/latest/help.html

.. _HAL hardware/storage: https://wiki.ncsa.illinois.edu/display/ISL20/HAL+cluster

.. _HAL user documentation: https://wiki.ncsa.illinois.edu/display/ISL20/HAL+cluster

.. _HAL user support: https://wiki.ncsa.illinois.edu/display/ISL20/HAL+cluster

.. _Hydro hardware/storage: https://docs.ncsa.illinois.edu/systems/hydro/en/latest/user-guide/architecture.html

.. _Hydro user documentation: https://docs.ncsa.illinois.edu/systems/hydro/

.. _Hydro user support: https://docs.ncsa.illinois.edu/systems/hydro/en/latest/help.html

.. _Campus Cluster hardware/storage: https://campuscluster.illinois.edu/about/system-info/

.. _Campus Cluster user documentation: https://docs.ncsa.illinois.edu/systems/icc/

.. _Campus Cluster user support: https://docs.ncsa.illinois.edu/systems/icc/en/latest/help.html

.. _ICRN hardware/storage: https://docs.ncsa.illinois.edu/systems/icrn/en/latest/user_guide/architecture.html

.. _Accessing ICRN: https://docs.ncsa.illinois.edu/systems/icrn/en/latest/user_guide/accessing.html

.. _ICRN user documentation: https://docs.ncsa.illinois.edu/systems/icrn/

.. _ICRN user support: https://docs.ncsa.illinois.edu/systems/icrn/en/latest/help.html

.. _Illinois HTC hardware/storage: https://docs.ncsa.illinois.edu/systems/iccp-htc

.. _Illinois HTC user documentation: https://docs.ncsa.illinois.edu/systems/iccp-htc/

.. _Illinois HTC user support: https://docs.ncsa.illinois.edu/systems/iccp-htc/en/latest/help.html

.. _ISL info: https://wiki.ncsa.illinois.edu/pages/viewpage.action?pageId=47292973

.. _Jade hardware/storage: https://docs.ncsa.illinois.edu/systems/jade/en/latest/user-guide/architecture.html

.. _Jade user documentation: https://docs.ncsa.illinois.edu/systems/jade/

.. _Jade user support: https://docs.ncsa.illinois.edu/systems/jade/en/latest/help.html

.. _Nightingale hardware/storage: https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/user_guide/architecture.html

.. _Nightingale user documentation: https://docs.ncsa.illinois.edu/systems/nightingale/

.. _Nightingale user support: https://docs.ncsa.illinois.edu/systems/nightingale/en/latest/help.html

.. _Radiant hardware/storage: https://docs.ncsa.illinois.edu/systems/radiant/en/latest/user-guide/architecture.html

.. _Radiant user documentation: https://docs.ncsa.illinois.edu/systems/radiant/

.. _Radiant user support: https://docs.ncsa.illinois.edu/systems/radiant/en/latest/help.html

.. _RCCS info: https://researchit.illinois.edu/get-help/research-computing-collaborative-services

.. _Taiga hardware/storage: https://docs.ncsa.illinois.edu/systems/taiga/en/latest/user-guide/architecture.html

.. _Taiga user documentation: https://docs.ncsa.illinois.edu/systems/taiga/

.. _Taiga user support: https://docs.ncsa.illinois.edu/systems/taiga/en/latest/help.html

.. _vForge hardware/storage: https://www.ncsa.illinois.edu/industry/vforge/

.. _vForge user support: https://www.ncsa.illinois.edu/industry/vforge/

|
