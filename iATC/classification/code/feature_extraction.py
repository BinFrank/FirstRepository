# 特征提取
from rdkit import Chem
from rdkit.Chem import AllChem
from .data_process import get_drug_json
from .data_process import datasets_classification


# 通过某一类的药物编号获取相应的SMILES列表
def get_smiles_by_code(col):
    smiles_list = []
    drug_smiles_dict = get_drug_json()
    drug_code_col = datasets_classification(col)
    for code, smiles in drug_smiles_dict.items():
        for drug_code in drug_code_col:
            if code == drug_code and smiles is not None:
                smiles_list.append(smiles)

    return smiles_list


def drug_data_test():
    # 药物数据测试

    # 载入分子库
    # drugbank = Chem.SDMolSupplier('../data/structures.sdf')
    drugbank = AllChem.SupplierFromFilename('../data/structures.sdf')
    mols = [x for x in drugbank if x is not None]
    print(len(mols))

    # 读入查询分子，计算指纹
    nicotine = Chem.MolFromSmiles('O=C(C)Oc1ccccc1C(=O)O')
    nicotine_fingerprint = AllChem.GetMorganFingerprint(nicotine, 2)
    print(nicotine_fingerprint)


# col = 1
# from rdkit import DataStructs
# # mol = AllChem.MolFromSmiles('NC(c1cccn(C3OC(C(C3O)O)COP(OP(OCC2OC(N5CNc4c(ncnc54)N)C(C2O)O)(=O)O)(=O)O)c1)=O')
# mol2 = AllChem.MolFromSmiles('OCC1OC(C(C(C1O)O)O)O')
# nicotine = AllChem.MolFromSmiles('c1(c(C)n(c2c1cc(cc2)OC)C(=O)c1ccc(cc1)Cl)CC(=O)O')
# nicotine_fingerprint = AllChem.GetMorganFingerprint(nicotine, 2)
# # fp1_morgan = AllChem.GetMorganFingerprint(mol, 2)
# fp2_morgan = AllChem.GetMorganFingerprint(mol2, 2)
# score = DataStructs.TanimotoSimilarity(nicotine_fingerprint, fp2_morgan)
# print(score)

