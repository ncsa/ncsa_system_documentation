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

NCSA offers access to a variety of compute, storage, and support resources; browse the summary table to find the resource that best fits your needs.

.. table:: NCSA Resources Summary
   :widths: 12 12 12 32 32 

   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Name                            | Type            | Target Users [#f1]_ | Primary Use Cases                                                            | User Documentation and Support                        |
   |                                 |                 | [#f2]_              |                                                                              |                                                       |
   +=================================+=================+=====================+==============================================================================+=======================================================+
   | Delta                           | HPC             | Campus,             | CPU:                                                                         | - `Delta hardware/storage`_                           |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System,          | - General purpose computation                                                |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | National            | - Engineering modeling and simulation                                        | - :ref:`Accessing Delta <allocate-delta>`             |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - Data analysis and analytics                                                |                                                       |
   |                                 |                 |                     |                                                                              | - `Delta user documentation`_                         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | GPU:                                                                         |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - Accelerated computation                                                    | - `Delta user support`_                               | 
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - Transition from CPU-only to GPU-only or hybrid CPU-GPU models              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - Machine learning frameworks like PyTorch and TensorFlow                    |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - Visualization and ray tracing                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | DeltaAI                         | HPC             | Campus,             | Coming soon!                                                                 | - `DeltaAI hardware/storage`_                         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System,          |                                                                              | - :ref:`Accessing DeltaAI <allocate-deltaai>`         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | National            |                                                                              | - `DeltaAI user documentation`_                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `DeltaAI user support`_                             |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Granite                         | Archive Storage | Campus,             | - Store infrequently accessed data                                           | - `Granite hardware/storage`_                         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System,          | - Disaster recovery                                                          | - :ref:`Accessing Granite <allocate-granite>`         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | National,           | - Archive datasets                                                           | - `Granite user documentation`_                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | Industry            |                                                                              | - `Granite user support`_                             |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | HAL                             | HPC             | Campus,             | Machine learning frameworks like PyTorch and TensorFlow.                     | - `HAL hardware/storage`_                             |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System           |                                                                              | - :ref:`Accessing HAL <allocate-hal>`                 |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `HAL user documentation`_                           |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `HAL user support`_                                 |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Hydro                           | HPC             | Campus,             | Priority use for NFI projects.                                               | - `Hydro hardware/storage`_                           |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | `NFI`_              |                                                                              | - :ref:`Accessing Hydro <allocate-hydro>`             |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Hydro user documentation`_                         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Hydro user support`_                               |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Illinois Campus Cluster         | HPC             | Campus,             | `Campus Cluster use cases <https://campuscluster.illinois.edu/science/>`_.   | - `Campus Cluster hardware/storage`_                  |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System           |                                                                              | - :ref:`Accessing Campus Cluster <allocate-icc>`      |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Campus Cluster user documentation`_                | 
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Campus Cluster user support`_                      | 
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Illinois Computes               | JupyterLab      | Campus              | Coming soon!                                                                 | - `ICRN hardware/storage`_                            |
   | Research Notebooks              |                 |                     |                                                                              |                                                       |
   | (ICRN)                          |                 |                     |                                                                              | - `Accessing ICRN`_                                   |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `ICRN user documentation`_                          |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `ICRN user support`_                                |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Illinois HTC                    | HTC             | Campus,             | Coming soon!                                                                 | - `Illinois HTC hardware/storage`_                    |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System           |                                                                              | - :ref:`Accessing Illinois HTC <allocate-htc>`        |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Illinois HTC user documentation`_                  |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Illinois HTC user support`_                        | 
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Innovative Systems Lab          | Emerging        | Campus              | Deploys, manages, and evaluates emerging hardware and software systems of    | - `ISL info`_                                         |
   |                                 | Technology      |                     | interest to the NCSA and campus scientific computing community.              |                                                       |
   |                                 | Exploration     |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Jade                            | ePHI/CUI Archive| Campus,             | - Store infrequently accessed data                                           | - `Jade hardware/storage`_                            |
   |                                 | Storage         |                     |                                                                              |                                                       |
   |                                 |                 | UI System,          |                                                                              | - :ref:`Accessing Jade <allocate-jade>`               |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | National,           | - Archive datasets                                                           | - `Jade user documentation`_                          |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | Industry            |                                                                              | - `Jade user support`_                                |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Nightingale                     | HIPAA HPC       | Campus,             | Projects working with:                                                       | - `Nightingale hardware/storage`_                     |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System           | - HIPAA                                                                      | - :ref:`Accessing Nightingale <allocate-nightingale>` | 
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - CUI                                                                        | - `Nightingale user documentation`_                   |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     | - Other protected or sensitive data                                          | - `Nightingale user support`_                         |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Radiant                         | HPC             | Campus              | `Radiant use cases`_.                                                        | - `Radiant hardware/storage`_                         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - :ref:`Accessing Radiant <allocate-radiant>`         |   
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Radiant user documentation`_                       | 
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `Radiant user support`_                             |     
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Research Computing              | Support         | Campus              | Coming Soon!                                                                 | - `RCCS info`_                                        |
   | Collaborative Services          |                 |                     |                                                                              |                                                       |
   | (RCCS)                          |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              |                                                       |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | Taiga                           | Storage         | Campus,             | - Active Research and Project Data                                           | - `Taiga hardware/storage`_                           |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | UI System,          | - Visualization data                                                         | - :ref:`Accessing Taiga <allocate-taiga>`             |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | National,           |                                                                              | - `Taiga user documentation`_                         |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 | Industry            |                                                                              | - `Taiga user support`_                               |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+
   | vForge                          | HTC             | Industry            | Starting point for NCSA’s industry partners.                                 | - `vForge hardware/storage`_                          |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - :ref:`Accessing vForge <allocate-vforge>`           |
   |                                 |                 |                     |                                                                              |                                                       |
   |                                 |                 |                     |                                                                              | - `vForge user support`_                              |
   +---------------------------------+-----------------+---------------------+------------------------------------------------------------------------------+-------------------------------------------------------+

.. _Radiant use cases: https://docs.google.com/spreadsheets/d/1VCg9hZVzsY_qiX_FGY_k0LDLZl_HPPkEJhOgv31YNHo/edit#gid=0

.. _Delta hardware/storage: https://docs.ncsa.illinois.edu/systems/delta/en/latest/user_guide/architecture.html

.. _Delta user documentation: https://docs.ncsa.illinois.edu/systems/delta/

.. _Delta user support: https://docs.ncsa.illinois.edu/systems/delta/en/latest/help.html

.. _DeltaAI hardware/storage: https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/user-guide/architecture.html

.. _DeltaAI user documentation: https://docs.ncsa.illinois.edu/systems/deltaai/

.. _DeltaAI user support: https://docs.ncsa.illinois.edu/systems/deltaai/en/latest/help.html

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

.. _NFI: https://newfrontiers.illinois.edu/about/

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

.. rubric:: Footnotes

.. [#f1]    
   Campus - affiliates of the University of Illinois Urbana-Champaign. 

   UI System - affiliates of the University of Illinois System.

   National - academic researchers outside of the University of Illinois System. 

   Industry - non-academic applications.

.. [#f2]
   If you are interested in a resource but are outside of the target user group(s), please :ref:`submit a support request <general-support>` to discuss your options.

|
