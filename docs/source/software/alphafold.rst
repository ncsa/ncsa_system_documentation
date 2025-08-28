AlphaFold
=========

AlphaFold is an artificial intelligence (AI) program originally
developed by Google DeepMind to predict the 3D structure of proteins
from the corresponding amino acid sequences. The latest version,
AlphaFold 3, can predict the structures of a broader range of
biomolecules than just proteins. This includes DNA, RNA, and ligands.
For a broad overview of AlphaFold 3, see `AlphaFold 3 predicts the
structure and interactions of all of life’s
molecules <https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/#life-molecules>`__.
For a more detailed view of the inner workings of AlphaFold 3, see `The
Illustrated
AlphaFold <https://elanapearl.github.io/blog/2024/the-illustrated-alphafold/>`__.

Availability
------------

======= ===== ===
Version Delta ICC
======= ===== ===
3.0.1   X     X
======= ===== ===

AlphaFold 3 is available for all Delta and Illinois Campus Cluster (ICC)
users.

Obtaining model parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~

The AlphaFold 3 model parameters are available under the `AlphaFold 3
Model Parameters Terms of
Use <https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md>`__.
You may not use these model parameters except in compliance with these
Terms of Use. **Read them carefully before using AlphaFold 3.**

To obtain the model parameters, follow the instructions at `Obtaining
Model
Parameters <https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#obtaining-model-parameters>`__.

Using AlphaFold 3
-----------------

The AlphaFold inference pipeline has two stages:

1. The CPU-intensive *data pipeline* stage which generates features from
   input sequences. This involves looking up publicly available sequence
   and structural databases.
2. The GPU-intensive *model inference* stage which predicts the
   structure of the molecule from the generated features. This stage
   requires the model parameters.

You can either run the full pipeline, or the individual stages
separately to better allocate computational resources. The following
Slurm scripts show how you can run AlphaFold 3 on Delta and ICC. We will
use the amino acid sequence of the Disco-interacting protein 2 homolog B
(DIP2B) molecule, stored as a JSON file, as the input for demonstration.

.. code:: json

   {
     "name": "DIP2B_dimer_AF-Q9P265-F1-model_v4",
     "modelSeeds": [
       15545
     ],
     "sequences": [
       {
         "protein": {
           "id": [
             "A"
           ],
           "sequence": "MAERGLEPSPAAVAALPPEVRAQLAELELELSEGDITQKGYEKKRSKLLSPYSPQTQETDSAVQKELRNQTPAPSAAQTSAPSKYHRTRSGGARDERYRSDIHTEAVQAALAKHKEQKMALPMPTKRRSTFVQSPADACTPPDTSSASEDEGSLRRQAALSAALQQSLQNAESWINRSIQGSSTSSSASSTLSHGEVKGTSGSLADVFANTRIENFSAPPDVTTTTSSSSSSSSIRPANIDLPPSGIVKGMHKGSNRSSLMDTADGVPVSSRVSTKIQQLLNTLKRPKRPPLKEFFVDDSEEIVEVPQPDPNQPKPEGRQMTPVKGEPLGVICNWPPALESALQRWGTTQAKCSCLTALDMTGKPVYTLTYGKLWSRSLKLAYTLLNKLGTKNEPVLKPGDRVALVYPNNDPVMFMVAFYGCLLAEVIPVPIEVPLTRKDAGGQQIGFLLGSCGIALALTSEVCLKGLPKTQNGEIVQFKGWPRLKWVVTDSKYLSKPPKDWQPHISPAGTEPAYIEYKTSKEGSVMGVTVSRLAMLSHCQALSQACNYSEGETIVNVLDFKKDAGLWHGMFANVMNKMHTISVPYSVMKTCPLSWVQRVHAHKAKVALVKCRDLHWAMMAHRDQRDVSLSSLRMLIVTDGANPWSVSSCDAFLSLFQSHGLKPEAICPCATSAEAMTVAIRRPGVPGAPLPGRAILSMNGLSYGVIRVNTEDKNSALTVQDVGHVMPGGMMCIVKPDGPPQLCKTDEIGEICVSSRTGGMMYFGLAGVTKNTFEVIPVNSAGSPVGDVPFIRSGLLGFVGPGSLVFVVGKMDGLLMVSGRRHNADDIVATGLAVESIKTVYRGRIAVFSVSVFYDERIVVVAEQRPDASEEDSFQWMSRVLQAIDSIHQVGVYCLALVPANTLPKTPLGGIHISQTKQLFLEGSLHPCNILMCPHTCVTNLPKPRQKQPGVGPASVMVGNLVAGKRIAQAAGRDLGQIEENDLVRKHQFLAEILQWRAQATPDHVLFMLLNAKGTTVCTASCLQLHKRAERIASVLGDKGHLNAGDNVVLLYPPGIELIAAFYGCLYAGCIPVTVRPPHAQNLTATLPTVRMIVDVSKAACILTSQTLMRLLRSREAAAAVDVKTWPTIIDTDDLPRKRLPQLYKPPTPEMLAYLDFSVSTTGMLTGVKMSHSAVNALCRAIKLQCELYSSRQIAICLDPYCGLGFALWCLCSVYSGHQSVLIPPMELENNLFLWLSTVNQYKIRDTFCSYSVMELCTKGLGNQVEVLKTRGINLSCVRTCVVVAEERPRVALQQSFSKLFKDIGLSPRAVSTTFGSRVNVAICLQGTSGPDPTTVYVDLKSLRHDRVRLVERGAPQSLLLSESGKILPGVKVVIVNPETKGPVGDSHLGEIWVNSPHTASGYYTIYDSETLQADHFNTRLSFGDAAQTLWARTGYLGFVRRTELTAATGERHDALYVVGALDETLELRGLRYHPIDIETSVSRIHRSIAECAVFTWTNLLVVVVELCGSEQEALDLVPLVTNVVLEEHYLIVGVVVVVDPGVIPINSRGEKQRMHLRDSFLADQLDPIYVAYNM",
           "modifications": []
         }
       }
     ],
     "bondedAtomPairs": [],
     "dialect": "alphafold3",
     "version": 1
   }

In the scripts below we assume the following directory structure:

::

   af3-runs/
   |- inputs/
   |  |- DIP2B_dimer_AF-Q9P265-F1-model_v4.json
   |- outputs/
   |- models/
   |  |- af3.bin
   |- af3.slurm

The ``inputs`` directory contains the JSON file with the sequence
information. The Slurm and AlphaFold 3 outputs will be produced in the
``outputs`` directory. The ``af3.bin`` file in the ``models``
sub-directory contains the model parameters which, as mentioned earlier,
you have to obtain from Google. The ``af3.slurm`` file is the Slurm
script.

Split workflow
~~~~~~~~~~~~~~

Data pipeline with CPU
^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   #!/bin/bash
   #SBATCH --job-name=af3-dip2b-data-pipeline
   #SBATCH --output=outputs/slurm-%j.out
   #SBATCH --error=outputs/slurm-%j.err
   #SBATCH --time=00:30:00
   #SBATCH --nodes=1
   #SBATCH --tasks-per-node=1
   #SBATCH --cpus-per-task=16
   #SBATCH --account=<account_name>
   #SBATCH --partition=<partition_name>
   #SBATCH --mem=80GB

   ROOT=/taiga/ncsa/alphafold/
   DB_DIR=${ROOT}/datasets
   IMAGE=${ROOT}/alphafold3/alphafold3.sif

   apptainer exec \
             --bind ${ROOT}/alphafold3:/root/af3 \
             --bind ${DB_DIR}:/root/public_databases \
             --bind ${PWD}/inputs:/root/af_input \
             --bind ${PWD}/outputs:/root/af_output \
             --bind ${PWD}/models:/root/models \
             ${IMAGE} \
             python /root/af3/run_alphafold.py \
             --model_dir=/root/models \
             --db_dir=/root/public_databases \
             --json_path=/root/af_input/DIP2B_dimer_AF-Q9P265-F1-model_v4.json \
             --output_dir=/root/af_output \
             --norun_inference

On Delta, replace ``<account_name>`` with ``XXXX-delta-cpu`` where
``XXXX`` is your project allocation code, and ``<partition_name>`` with
``cpu``. On ICC, replace ``<account_name>`` with an account available to
you, and ``<partition_name>`` with a CPU partition available to you. On
job completion, you will have the following output:

::

   outputs/
   |- slurm-<job_number>.out
   |- dip2b_dimer_af-q9p265-f1-model_v4_<timestamp>/
   |  |- dip2b_dimer_af-q9p265-f1-model_v4_data.json

The ``dip2b_dimer_af-q9p265-f1-model_v4_data.json`` file contains the
generated features and you can use this file as the input to predict the
structure of the protein.

Model inference with GPU
^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   #!/bin/bash
   #SBATCH --job-name=af3-dip2b-model-inference
   #SBATCH --output=outputs/slurm-%j.out
   #SBATCH --error=outputs/slurm-%j.err
   #SBATCH --time=00:10:00
   #SBATCH --nodes=1
   #SBATCH --tasks-per-node=1
   #SBATCH --cpus-per-task=16
   #SBATCH --gpus-per-task=1
   #SBATCH --account=<account_name>
   #SBATCH --partition=<partition_name>
   #SBATCH --mem=80GB

   module load cuda/12.6

   ROOT=/taiga/ncsa/alphafold/
   DB_DIR=${ROOT}/datasets
   IMAGE=${ROOT}/alphafold3/alphafold3.sif

   apptainer exec \
             --nv \
             --bind ${ROOT}/alphafold3:/root/af3 \
             --bind ${DB_DIR}:/root/public_databases \
             --bind ${PWD}/inputs:/root/af_input \
             --bind ${PWD}/outputs:/root/af_output \
             --bind ${PWD}/models:/root/models \
             ${IMAGE} \
             python /root/af3/run_alphafold.py \
             --model_dir=/root/models \
             --db_dir=/root/public_databases \
             --json_path=/root/af_output/dip2b_dimer_af-q9p265-f1-model_v4_<timestamp>/dip2b_dimer_af-q9p265-f1-model_v4_data.json \
             --output_dir=/root/af_output \
             --norun_data_pipeline

On Delta, replace ``<account_name>`` with ``XXXX-delta-gpu`` where
``XXXX`` is your project allocation code, and ``<partition_name>`` with
a GPU partition name, such as ``gpuA100x4``. On ICC, replace
``<account_name>`` with an account available to you, and
``<partition_name>`` with a GPU partition available to you.

Notice that in this case we are using the output of the data pipeline
stage as the input (``--json_path``). On job completion, you will have
the following output (arranged anti-chronologically):

::

   outputs/
   |- slurm-<new_job_number>.out
   |- dip2b_dimer_af-q9p265-f1-model_v4_<new_timestamp>/
   |  |- dip2b_dimer_af-q9p265-f1-model_v4_confidences.json
   |  |- dip2b_dimer_af-q9p265-f1-model_v4_data.json
   |  |- ...
   |  |- ranking_scores.csv
   |  |- ...
   |- slurm-<job_number>.out
   |- dip2b_dimer_af-q9p265-f1-model_v4_<timestamp>/
   |  |- dip2b_dimer_af-q9p265-f1-model_v4_data.json

The ``dip2b_dimer_af-q9p265-f1-model_v4_<new_timestamp>`` sub-directory
contains the final model predictions regarding the structure of the
molecule.

Full pipeline
~~~~~~~~~~~~~

.. code:: shell

   #!/bin/bash
   #SBATCH --job-name=af3-dip2b-full-pipeline
   #SBATCH --output=outputs/slurm-%j.out
   #SBATCH --error=outputs/slurm-%j.err
   #SBATCH --time=00:30:00
   #SBATCH --nodes=1
   #SBATCH --tasks-per-node=1
   #SBATCH --cpus-per-task=16
   #SBATCH --gpus-per-task=1
   #SBATCH --account=<account_name>
   #SBATCH --partition=<partition_name>
   #SBATCH --mem=80GB

   module load cuda/12.6

   ROOT=/taiga/ncsa/alphafold/
   DB_DIR=${ROOT}/datasets
   IMAGE=${ROOT}/alphafold3/alphafold3.sif

   apptainer exec \
             --nv \
             --bind ${ROOT}/alphafold3:/root/af3 \
             --bind ${DB_DIR}:/root/public_databases \
             --bind ${PWD}/inputs:/root/af_input \
             --bind ${PWD}/outputs:/root/af_output \
             --bind ${PWD}/models:/root/models \
             ${IMAGE} \
             python /root/af3/run_alphafold.py \
             --model_dir=/root/models \
             --db_dir=/root/public_databases \ 
             --json_path=/root/af_input/DIP2B_dimer_AF-Q9P265-F1-model_v4.json \
             --output_dir=/root/af_output

On Delta, replace ``<account_name>`` with ``XXXX-delta-gpu`` where
``XXXX`` is your project allocation code, and ``<partition_name>`` with
a GPU partition name, such as ``gpuA100x4``. On ICC, replace
``<account_name>`` with an account available to you, and
``<partition_name>`` with a GPU partition available to you. On job
completion, you will have the following output (arranged
anti-chronologically):

::

   outputs/
   |- slurm-<job_number>.out
   |- dip2b_dimer_af-q9p265-f1-model_v4/
   |  |- dip2b_dimer_af-q9p265-f1-model_v4_confidences.json
   |  |- dip2b_dimer_af-q9p265-f1-model_v4_data.json
   |  |- ...
   |  |- ranking_scores.csv
   |  |- ...
