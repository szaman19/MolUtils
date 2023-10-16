import numpy as np
from rdkit import Chem
from Config import ChargeDict


def SmilesToGraph(smiles_string: str,
                  removeHs=True,
                  dense=False):
  _mol = Chem.MolFromSmiles(smiles_string)

  if _mol == None:
    raise ValueError('Inavlid smiles string')
  
  _mol = _mol if removeHs else Chem.AddHs(_mol)

  num_atoms = _mol.GetNumAtoms()
  charges = np.array([ChargeDict[x] for x in _mol.GetAtoms()])
  
  





