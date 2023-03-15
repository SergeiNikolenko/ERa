import os
import glob
fld=str(input('Type a name of directory where ligand files stored '))
print (fld)
os.chdir(fld)
print (os.getcwd())
amount=int(input('How many receptors are you going to use?'+' '))
tries=int(input('How many tries per ligand are you going to use?'+' '))
nt=int(input('How many threads do you want to use?'+' '))
xtn=int(input('What exhaustiveness do you want to use? '))
vinastart=open('vinastart.sh', 'w')
vinastart.write('#!/bin/bash'+'\n')
mols=glob.glob('./*.pdbqt')
count=len(mols)
h=1
print (mols)
#print (name)
cx=input ('Type center x'+ ' ')
cy=input ('Type center y'+ ' ')
cz=input ('Type center z'+ ' ')
sx=input ('Type size in x dimension'+ ' ')
sy=input ('Type size in y dimension'+ ' ')
sz=input ('Type size in z dimension'+ ' ')
for h in range (0, amount):
    receptor=input('Type rig receptor name'+ ' ')
    i=0
    for i in range (0, count):
        t=1
        while t<=tries:
            f=open(mols[i])
            #line=f.readline()
            NAME=str(mols[i])
            name=(NAME[2:-6])
            print (name)
            config=open(receptor+"_"+name+'_'+str(t)+'.cfg', 'w')
            config.write('receptor='+receptor+'.pdbqt'+'\n'+'ligand='+name+'.pdbqt'+'\n'+' '+'\n'+'center_x='+cx+'\n'+'center_y='+cy+'\n'+'center_z='+cz+'\n'+' '+'\n'+'size_x='+sx+'\n'+'size_y='+sx+'\n'+'size_z='+sz+'\n'+' '+'\n'+'exhaustiveness='+str(xtn)+'\n'+'num_modes=20'+'\n'+'energy_range=20'+'\n'+'cpu='+str(nt)+'\n'+' '+'\n'+'out='+receptor+'_'+name+'_'+str(t)+'_out.pdbqt'+'\n'+'log='+receptor+'_'+name+'_'+str(t)+'_out.log')
            config.close()
            print ('Config file for '+mols[i]+' '+'is written!')
            vinastart.write('vina'+' '+'--config'+' '+receptor+'_'+name+'_'+str(t)+'.cfg'+'\n')
            print ('Run command for '+mols[i]+' '+'is written to vinastart!')
            t+=1
vinastart.close()
print ('Config files generation is comlete!')
print ('The vinastart is ready to run!')

