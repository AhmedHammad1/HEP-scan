#!/usr/bin/python
import fileinput
import os
import random
import re
import sys
import shutil
import cmath 
import numpy as np
import array
import time
from scan_input import * 
from os import remove
from shutil import move
import tarfile
import glob
path = os.getcwd()
paths = str(pathS)+'/'
##############################################
#while True:
#    try:
#        npoints =int(raw_input('PLEASE ENTER NUMBER OF POINTS YOU WANT TO SCAN OVER :'))
#        break
#    except ValueError:
#        print('PLEASE ENTER AN INTEGER,... ')
#
#while True:
#    try:
#        pathS =str(raw_input('PLEASE ENTER PATH OF SPHENO :'))
#
#        if os.path.exists(str(paths)+('bin/SPheno')):
#            break
#        else:
#            print '"/bin/SPheno" NOT EXIST, PLEASE TYPE make.'
#    except ValueError:
#        print('PLEASE ENTER AN INTEGER,... ')
#
#while True:
#    try:
#        Lesh = str(raw_input('PLEASE ENTER LESHOUCHES FILE NAME :')) #'LesHouches.in.BLSSM' 
#        if os.path.exists(str(paths)+str(Lesh)):
#            break
#        else:
#            print str(paths)+str(Lesh)+' NOT EXIST, PLEASE ENTER VALIED NAME.'
#    except ValueError:
#        print(' PLEASE ENTER AN LESHOUCHES NAME,... ')
#
#while True:
#    try:
#        name = str(raw_input('PLEASE ENTER MODEL NAME :')) #'LesHouches.in.BLSSM' 
#        if os.path.exists(str(paths)+('bin/SPheno')+str(name)):
#            break
#        else:
#            print ' "bin/SPheno'+str(name)+'" NOT EXIST, PLEASE ENTER VALIED NAME.'
#    except ValueError:
#        print('PLEASE ENTER A  MODEL NAME,... ')
##################################################################
if (Vevacious != 0 ):
    if not os.path.exists(str(pathVevacious)+'/'+str(pathIntial_xml)):
        sys.exit (str(pathVevacious)+'/'+str(pathIntial_xml)+' NOT EXIST !!! CHECK IT.. ')
if (npoints  != 0 ):
    if not os.path.exists(str(paths)+('bin/SPheno')):
        sys.exit ('"/bin/SPheno" NOT EXIST, PLEASE TYPE make.')
    if not  os.path.exists(str(paths)+str(Lesh)):
        sys.exit (str(paths)+str(Lesh)+' NOT EXIST, PLEASE ENTER VALIED NAME.')
    if not  os.path.exists(str(paths)+'/bin/SPheno%s'%(str(name))):
        sys.exit (str(paths)+'/bin/SPheno%s'%(str(name))+' NOT EXIST, PLEASE ENTER VALIED MODEL NAME.')
if os.path.exists(str(path)+'/Out_%s'%(str(name))):
    shutil.rmtree(str(path)+'/Out_%s'%(str(name)))
os.mkdir(str(path)+"/Out_%s"%(str(name)))
if os.path.exists(str(path)+'/Spec_out_%s'%(str(name))):
    shutil.rmtree(str(path)+'/Spec_out_%s'%(str(name)))
os.mkdir(str(path)+"/Spec_out_%s"%(str(name)))
if os.path.exists(str(path)+'/Les_out_%s'%(str(name))):
    shutil.rmtree(str(path)+'/Les_out_%s'%(str(name)))
os.mkdir(str(path)+"/Les_out_%s"%(str(name)))
if (TotConstScanned != 0):
    if os.path.exists(str(path)+'/Const_Spec_%s'%(str(name))):
        shutil.rmtree(str(path)+'/Const_Spec_%s'%(str(name)))
    os.mkdir(str(path)+"/Const_Spec_%s"%(str(name)))
os.chdir(paths)
oldrunfile = open(str(Lesh),'r+')
oldrunfile.close()
for xx in range(0,npoints):
    print ('''-------------------------------------------
NUMBER OF SCANNED POINTS SPheno = \t''')+(''' %i'''%(xx+1))+('''
-------------------------------------------''')
    newrunfile = open('newfile','w')
    oldrunfile = open(str(Lesh),'r+')
    for line in oldrunfile:
        NewlineAdded = 0
        for yy in range(0,TotVarScanned):
            if str(VarLabel[yy]) in line:
                value = VarMin[yy] + (VarMax[yy] - VarMin[yy])*random.random()
                valuestr = str("%.4E" % value)
                newrunfile.write(VarNum[yy]+'   '+valuestr +str('     ')+ VarLabel[yy]+'\n')
                NewlineAdded = 1
        if NewlineAdded == 0:
            newrunfile.write(line)
    newrunfile.close()
    oldrunfile.close()
    os.remove(str(Lesh))
    os.rename('newfile',str(Lesh))
    os.system('./bin/SPheno'+str(name)+' '+str(Lesh)+' spc.out'+' >  out.txt')
    out = open(str(paths)+'out.txt','r+')
    for l in out:
        #print l
        if str('Finished!') in l:
                    os.rename('spc.out','SPheno.spc.%s_%i'%(str(name),(xx+1)))
                    shutil.move('SPheno.spc.%s_%i'%(str(name),(xx+1)),path+"/Spec_out_%s/"%(str(name)))
                    os.rename(str(Lesh),str(Lesh)+'%i'%(xx+1))
                    shutil.copy(str(Lesh)+'%i'%(xx+1),path+"/Les_out_%s"%(str(name)))
                    os.rename(str(Lesh)+'%i'%(xx+1),str(Lesh))
    os.remove('out.txt')
if not os.listdir(path+"/Spec_out_%s/"%(str(name))) == []:
    tar_spec = tarfile.open(path+"/Out_%s/Spectrum_%s.tar.gz"%(str(name),str(name)), "w:gz")
    tar_spec.add(path+"/Spec_out_%s/"%(str(name)), arcname="Spectrum_%s"%(str(name)))
    tar_spec.close()
    print '******************************************'
    print "Spectrum_%s.tar.gz , GENERATED."%(str(name))
else:
    sys.exit(str(path)+"/Spec_out_%s/  EMPTY. NO SPECTRUM GENERATED."%(str(name)))
if not os.listdir(path+"/Les_out_%s/"%(str(name))) == []:
    tar_les = tarfile.open(path+"/Out_%s/Leshouches_%s.tar.gz"%(str(name),str(name)), "w:gz")
    tar_les.add(path+"/Les_out_%s/"%(str(name)), arcname="Leshouches_%s"%(str(name)))
    tar_les.close()
    print "Leshouches_%s.tar.gz , GENERATED."%(str(name))
    print '******************************************'
else:
    sys.exit(str(path)+"/Les_out_%s/  EMPTY. NO SPECTRUM GENETRAED."%(str(name)))
os.chdir(path)
######################################

if (TotConstScanned != 0 ):
    print 'GENERATING CONSTRAINTED SPECTRUM,......'
    scan = open ('Const.py','w')
    scan.write('''#!/usr/bin/python
import os
import sys
import shutil
import numpy as np
path = os.getcwd()
import tarfile
import glob
from scan_input import *
def loop_func():
    files=glob.glob(str(path)+'/Spec_out_%s/*'%(str(name)))
    for file in files:     
        f=open(file, 'r')  
        for x in f:       ''' ) 
    for zz in range(0,TotConstScanned):
        scan.write('''
            if str('%s     ' and '%s') in x:
                r_%i = x.rsplit()
                l_%i = int(float(r_%i[1]))
                if (l_%i not in np.linspace(%i,%i)):
                    return '''%(str(ConstNum[zz]),str(ConstLabel[zz]),(zz+1),(zz+1),(zz+1),(zz+1),(ConstMin[zz]),(ConstMax[zz])))
    scan.write('''
            else: 
                shutil.copy(file,path+"/Const_Spec_%s/"%(str(name)))
                if not os.listdir(path+"/Const_Spec_%s/"%(str(name))) == []:
                    tar_les = tarfile.open(path+"/Out_%s/Constraint_Spec_%s.tar.gz"%(str(name),str(name)), "w:gz")
                    tar_les.add(path+"/Const_Spec_%s/"%(str(name)), arcname="Constraint_Spec_%s"%(str(name)))
                    tar_les.close()
                                       
                else:
                    sys.exit(str(path)+"/Constraint_Spec_%s/  EMPTY. NO SPECTRUM GENETRAED."%(str(name)))
    
                      
loop_func()''')
    scan.close()
    os.system('chmod -u+xrw Const.py') 
    os.system('./Const.py')
    os.remove('Const.py')
    if (Vevacious == 0 ):
        shutil.rmtree(str(path)+'/Const_Spec_%s'%(str(name)))
if (Vevacious == 0 ):
    shutil.rmtree(str(path)+'/Spec_out_%s'%(str(name)))
    shutil.rmtree(str(path)+'/Les_out_%s'%(str(name)))
if (Vevacious != 0 ):
    print 'PREPARING VEVACIOUS,...'
    time.sleep(40)
    files_Spec=glob.glob(str(path)+'/Spec_out_%s/*'%(str(name)))
    count = 0
    for file in files_Spec:
        count = count+1
        print ('''-------------------------------------------
NUMBER OF SCANNED POINTS Vevacious = \t''')+(''' %i'''%(count))+('''
-------------------------------------------''')
        os.chdir(pathVevacious)
        newfile = open('newrunfile','w')
        oldfile = open(str(pathIntial_xml),'r+')
        for line in oldfile :
            NewlineAdded = 0
            if str('<slha_file>') in line :
                newfile.write('<slha_file>    ' + str(file) + "\n")
                NewlineAdded = 1
            if NewlineAdded == 0:
                newfile.write(line)
        newfile.close()
        oldfile.close()
        os.remove(str(pathIntial_xml))
        os.rename('newrunfile',str(pathIntial_xml))
        os.system('./bin/Vevacious.exe  ' + str(pathIntial_xml)+ '   > out')
        veva = open ('out')
        for c in veva :
            if str('was not produced!')  in c :
                os.remove(file)
                continue
        os.remove('out')
    os.chdir(path)
    if os.path.exists(str(path)+'/Veva_out_%s'%(str(name))):
        shutil.rmtree(str(path)+'/Veva_out_%s'%(str(name)))
    os.mkdir(str(path)+"/Veva_out_%s"%(str(name)))
    files_Spec=glob.glob(str(path)+'/Spec_out_%s/*'%(str(name)))
    for file in files_Spec:
        shutil.copy(file,str(path)+"/Veva_out_%s/"%(str(name)))
    tar_les = tarfile.open(path+"/Out_%s/Vevacious_out_%s.tar.gz"%(str(name),str(name)), "w:gz")
    tar_les.add(path+"/Veva_out_%s/"%(str(name)), arcname="Vevacious_out_%s"%(str(name)))
    tar_les.close()
    shutil.rmtree(str(path)+'/Spec_out_%s'%(str(name))) 
    shutil.rmtree(str(path)+'/Les_out_%s'%(str(name)))
    if TotNoResult == 0 :
        shutil.rmtree(str(path)+'/Veva_out_%s'%(str(name)))
    

if TotNoResult != 0:
    f = open(str(path)+'/Out_%s/Vevacious_Result.txt'%(str(name)),'w')
    files_Veva=glob.glob(str(path)+'/Veva_out_%s/*'%(str(name)))
    if os.listdir(path+"/Veva_out_%s/"%(str(name))) == []:
        sys.exit(str(path)+'/Veva_out_%s/  FILE EMPTY, NO VEVACIOUS FILES GENERATED'%(str(name)))
    for vv in range(0,TotNoResult) :
        f.write(ResLabel[vv]+'     ') 
    f.write('\n') 
    
        #f.write('\n') 
    for file in files_Veva:
        for vv in range(0,TotNoResult) :
            l = open (file,'r')
            for line in l:
                if str(ResLabel[vv]) in line :
                    x = line.rsplit()
                    mm = float(x[ResOpt[vv]]) 
                    f.write(str(mm)+ '   ') 
        f.write('\n') 
    f.close()
    shutil.rmtree(str(path)+'/Veva_out_%s'%(str(name)))






print '''
--------------------------------------------------
ALL OUTPUT STORED IN %s/Out_%s
--------------------------------------------------'''% (str(path),str(name)) 
