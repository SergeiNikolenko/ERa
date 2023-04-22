import MDAnalysis as mda
import prolif as plf
import numpy as np
from prolif.plotting.network import LigNetwork
import glob


step=int(input("Chose a step in degrees to rotate the picture "))
traj=glob.glob('./*.xtc')[0][2:]
top=glob.glob('./*.tpr')[0][2:]
NAME=traj[0:-11]

u = mda.Universe(top, traj)
prot = u.select_atoms("protein")
lig = u.select_atoms("resname 116")
lmol = plf.Molecule.from_mda(lig)
pmol = plf.Molecule.from_mda(prot)

fp_l = plf.Fingerprint()
fp_l.run(u.trajectory[40000:45000:10], lig, prot)
df_l = fp_l.to_dataframe(return_atoms=True)
df=fp_l.to_dataframe(return_atoms=False)
D=df.groupby(level=["ligand", "protein"], axis=1, sort=False).sum().astype(bool).mean()
un_lig=D.index.get_level_values("protein").unique().tolist()
un_lig.sort()
lst1=[]
for el in un_lig:
    lst1.append(el[0:3]+str(int(el[3:])+306))

mapping=dict(zip(un_lig, lst1))

df_l=df_l.rename(mapping, axis='columns')
D=df_l

for j in range (0, 360, step):
    net_l = LigNetwork.from_ifp(df_l, lmol, kind="aggregate", threshold=0.5, rotation=j)
    net_l.save(f'{NAME}_ints_{j}.html')

df_n2=fp_l.to_dataframe(return_atoms=False)
df_n2=df_n2.rename(mapping, axis='columns')

occ2=df_n2.mean()
E=occ2.loc[occ2 > 0.5]
E=E.round(decimals=1)
E.to_csv(NAME+'_ints.csv', sep=',')

