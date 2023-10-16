import numpy as np
from rdkit.Chem import rdDetermineBonds, MolFromXYZBlock
from Config import OrganicDecoder

def Generate_XYZ(coordinate_matrix, 
                 atom_type_vector):
  xyz_str = ""

  return xyz_str


def XYZ_to_Mol(xyz_block):
  try:
    conformed_mol = MolFromXYZBlock(xyz_block)
    rdDetermineBonds.DetermineBonds(conformed_mol)
  except ValueError as e:
    print("Failed to determine bonds \n", e)
  except Exception as e:
    print("Other error", e)
  return conformed_mol


def get_xyz_strings(one_hot,
                    positions,
                    node_mask,
                    decoder=OrganicDecoder):

  atomsxmol = torch.sum(node_mask, dim=1)
  n_atoms = int(atomsxmol[0])
  xyz_str = f"{n_atoms}\n\n"
  atoms = torch.argmax(one_hot[0], dim=1)
  for atom_i in range(n_atoms):
    a = atoms[atom_i]
    atom = decoder[a]
    xyz_str += f"{atom}"
    for axis in range(3):
      xyz_str += f" {positions[0, atom_i, axis]:.9f}"
      xyz_str += '\n'
  return xyz_str
