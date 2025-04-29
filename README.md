# ‘Crystallization cocktails’ for X-ray diffraction analysis of liquids
Official implementation of:

**‘Crystallization cocktails’ for X-ray diffraction analysis of liquids**

Anastasia Danshina, Ivan Zlobin, Svetlana Solov’eva, Nikolai Rekut, Yulia V. Nelyubina

https://doi.org/...

**Abstract**: ‘Crystallization cocktails’ based on organic sulfonic acids (such as p-toluenesulfonic and 1,5 naphtalenedisulfonic acids) and amines (such as p-phenylenediamine, 4,4′-oxydianiline and 4,4′-diamino-3,3′-dichlorodiphenylmethane) of various geometries were proposed as crystalline matrices that may adapt to different guests owing to ‘labile’ hydrogen bonds and weak van-der-Waals interactions for crystal structure determination of liquids. The guest-to-host ratio in the co-crystals with model liquid phenols (2,4-dimethyl-, and 2-isopropyl- and 2-ethylphenol) – produced by simple mixing and co-solvent evaporation – depended on the size of the individual components of the ‘crystallization cocktails’ that is transferable between the co-crystals. These ‘crystallization cocktails’ that can be ‘mixed to order’ – if boosted by a machine learning algorithm to limit the list of their components to a few most suitable ones for a successful co-crystallization – pave the way towards routine structure determination of liquids or other poorly crystallizing substances by X-ray diffraction, streamlining the search for new chemical compounds and identification of ‘old’ ones in natural products, waste and natural waters and living organisms.

The training and acquired experimental data can be found in the "data/raw" folder of this repository. Trained XGBoost model is saved in "saved_models" folder, while "predictions" folder contain model's classification results for featurized test dataset. The "src" folder contains scripts for data preprocessing and model training. You can train and test classification models using corresponding Jupyter Notebook files.
