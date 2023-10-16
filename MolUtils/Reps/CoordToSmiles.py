from rdkit import Chem


def mol2smiles(mol):
  check_mol = None
  try:
    check_mol = Chem.SanitizeMol(mol)
  except ValueError:
    return None, None
  if check_mol is not None:
    mol_frags = Chem.rdmolops.GetMolFrags(mol, asMols=True)
    largest_mol = max(mol_frags, default=mol, key=lambda m: m.GetNumAtoms())
    try:
      check_mol = Chem.SanitizeMol(largest_mol)
      return Chem.MolToSmiles(largest_mol), largest_mol
    except ValueError:
      return None, None


