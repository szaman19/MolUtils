from rdkit import Chem

ChargeDict = {'H': 1, 'C': 6, 'N': 7, 'O': 8} 

BondDict = [None,
            Chem.rdchem.BondType.SINGLE,
            Chem.rdchem.BondType.DOUBLE,
            Chem.rdchem.BondType.TRIPLE,
            Chem.rdchem.BondType.AROMATIC]

OrganicDecoder = ['H', "C", 'N', "O"]

def GetIndex(list, element):
  return list.index(element)