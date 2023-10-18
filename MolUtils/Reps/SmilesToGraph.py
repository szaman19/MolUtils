import numpy as np
from rdkit import Chem
from Config import ChargeDict


def SmilesToGraph(smiles_string: str,
                  atom_embedding_func,
                  bond_embedding_func,
                  removeHs=True,
                  dense=False):
  _mol = Chem.MolFromSmiles(smiles_string)

  if _mol == None:
    raise ValueError('Inavlid smiles string')
  
  data = {}
  _mol = _mol if removeHs else Chem.AddHs(_mol)

  num_atoms = _mol.GetNumAtoms()
  data['num_atoms'] = num_atoms

  charges = np.array([ChargeDict[x] for x in _mol.GetAtoms()])
  data['charge'] = charges
  
  atom_mat = np.array([atom_embedding_func(x.GetSymbol()) for x in _mol.GetAtoms()])
  data['atoms'] = atom_mat

  if len(_mol.GetBonds()) > 1:
    edge_mat = []
    if dense:
      adj_mat = np.zeros((num_atoms, num_atoms))
      edge_mat = []
    else:
      # Return COO format connectivity
      edge_list = []
    
    for bond in _mol.GetBonds():
      i = bond.GetBeginAtomIdx()
      j = bond.GetEndAtomIdx()
      if dense:
        adj_mat[i,j] = 1
        edge_mat[i,j] = bond_embedding_func(bond)
      else:
        edge_list.append([i, j])
        edge_mat.append(bond_embedding_func(bond))
    
    data['edge_type'] = edge_mat
    if dense:
      data['edge_mat'] = adj_mat
    else:
      data['edge_list'] = edge_list

  return data
  





