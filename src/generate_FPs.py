import pandas as pd
import numpy as np

from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors


def generate_RDkit_descriptors(smiles_list):
    
    mols = [Chem.MolFromSmiles(i) for i in smiles_list] 

    calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
    
    mol_descriptors = []
    for mol in mols:
        rdkit_descriptors = calc.CalcDescriptors(mol)
        mol_descriptors.append(np.array(rdkit_descriptors))
    desc_names = calc.GetDescriptorNames()
    print(f'Added {len(np.array(rdkit_descriptors))} RDKit descriptors with names:')
    for _ in desc_names:
        print(_)
    return pd.Series(mol_descriptors)



def custom_featurize(smiles_df, columns, mode = ['rdkit'],
                    ): 
    df = smiles_df.copy()
    for col in columns:
        if 'rdkit' in mode:
            df[col+'_rdkit'] = generate_RDkit_descriptors(df[col])
    return df

