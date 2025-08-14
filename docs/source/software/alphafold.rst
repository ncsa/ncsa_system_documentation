Alphafold
==============

AlphaFold is an artificial intelligence (AI) program originally developed by Google DeepMind to predict the 3D structure of proteins from the corresponding amino acid sequences. The latest version, AlphaFold 3, can predict the structures of a broader range of biomolecules than just proteins. This includes DNA, RNA, and ligands. For a broad overview of AlphaFold 3, see `AlphaFold 3 predicts the structure and interactions of all of life’s molecules <https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/#life-molecules>`__. For a more detailed view of the inner workings of AlphaFold 3, see `The Illustrated AlphaFold <https://elanapearl.github.io/blog/2024/the-illustrated-alphafold/>`__.

The AlphaFold inference pipeline can be broadly divided into two stages:

#. Data pipeline (CPU intensive): generate features from input sequence
#. Model inference (GPU intensive): predict molecule structure from generated features

The data pipeline stage involves looking up publicly available sequence and structural databases. The model inference step requires pre-trained model weights.

NCSA hosts AlphaFold 3 for Delta and Illinois Campus Cluster (ICC) users. This includes the software package, available as an Apptainer container, and the public databases. **You must obtain the pre-trained model weights from Google DeepMind directly.** Fill and submit `this form <https://docs.google.com/forms/d/e/1FAIpQLSfWZAgo1aYk0O4MuAXZj8xRQ8DafeFJnldNOnh_13qAx2ceZw/viewform?pli=1>`__ to request the model weights from Google DeepMind. Please ensure that you have read the terms and conditions mentioned in the form and that you can comply with them.
