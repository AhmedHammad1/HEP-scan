########################################################################
# python script to scan over SPheno and Vevacious.
#                  By A.Hammad
# To run 
# 1- Set both files scan_general.py and scan_input.py in any directory
# 2- chmod -u+xrw scan_general.py
# 3- ./scan_general.py 
#   Note : the variables that not declared here will kept fixed 
#          with its values in the Leshouches file.
########################################################################

VarMax =[] 
VarMin =[] 
VarLabel =[]
VarNum =[]
ConstMax =[]
ConstMin =[]
ConstLabel =[]
ConstNum =[]
ResLabel = []
ResNum = []
ResOpt = []
#################################
npoints = 100000                  #Number of points you want to scan over
pathS ='/usr/work/HAZ_140/SPheno-3.3.3' # Path to SPheno directory between, please set it between the qutes
Lesh ='LesHouches.in.BLSSMIS'     # Name of Leshouches file between,please set it between the qutes
name ='BLSSMIS'                   # Model name between, please set it between the qutes

#################################
VarMin.append(1000) # define the minimum value of varible 
VarMax.append(2000) # define the maximum value of varible 
VarLabel.append('# m0') # define the label of varible from Leshouches file 
VarNum.append('1')  # Leshouches number of variable in Leshouches file 

VarMin.append(1000) 
VarMax.append(2000) 
VarLabel.append('# m12') 
VarNum.append('2')

VarMin.append(10) 
VarMax.append(30)
VarLabel.append('# TanBeta') 
VarNum.append('3')


VarMin.append(-800) 
VarMax.append(-2000) 
VarLabel.append('# Azero') 
VarNum.append('5')


VarMin.append(1500)
VarMax.append(5500)
VarLabel.append('# MZp')
VarNum.append('8')


#VarMin.append(0.5)
#VarMax.append(0.9)
#VarLabel.append('# gBLinput')
#VarNum.append('9')


VarMin.append(0.5)
VarMax.append(0.9)
VarLabel.append(r'# Yx(1,1)')
VarNum.append('1 1     ')

VarMin.append(0.5)
VarMax.append(0.9)
VarLabel.append(r'# Yx(2,2)')
VarNum.append('2 2     ')

VarMin.append(0.5)
VarMax.append(0.9)
VarLabel.append(r'# Yx(3,3)')
VarNum.append('3 3     ')

VarMin.append(0.5)
VarMax.append(0.9)
VarLabel.append(r'# Yv(1,1)')
VarNum.append('1 1     ')

VarMin.append(0.5)
VarMax.append(0.9)
VarLabel.append(r'# Yv(2,2)')
VarNum.append('2 2     ')

VarMin.append(0.5)
VarMax.append(0.9)
VarLabel.append(r'# Yv(3,3)')
VarNum.append('3 3     ')

TotVarScanned = 11  # Total number of variables scanned. Note: by setting TotVarScanned= 0 no scan over SPheno occurs.
###############################################################################
# Here to define the constraint spectrum you want out of SPheno               #
# by switching TotConstScanned on -----> if you placed it to zero you will get# 
#                                        all spectrum files with out selection#
###############################################################################
ConstMin.append(124)   # define the minimum value of constraint variable  
ConstMax.append(126)   # define the maximum value of constraint variable
ConstLabel.append('# hh_1') # define the label of constraint from Leshouches file 
ConstNum.append('25') # Leshouches number of constaint variable in Leshouches file 

ConstMin.append(5) 
ConstMax.append(50)
ConstLabel.append('# TanBeta') 
ConstNum.append('3')

ConstMin.append(0) 
ConstMax.append(0)
ConstLabel.append('# Sd_1') 
ConstNum.append('1000001')


TotConstScanned = 0 # Total number of constraint variables scanned.
#Note: by setting TotVarScanned= 0 you will get 
#all spectrum files with out selection

#################################
Vevacious = 0    # 0 or 1 to trun on and off Vevacious link
pathVevacious = '/usr/work/Vevacious-1.1.02/' # Vevacious path 
pathIntial_xml= 'VevaciousInitialization.xml' #Name of Intialization file. Note:should be in the main dir of Vevacious

################################################################
# Define the varaibles you want to get in txt file for drawing #
# These files are out of Vevacious   and stored in             #
#                    Vevacious_Result.txt                      #
################################################################

ResLabel.append('# TanBeta') # define the label of varaibles from Leshouches file 
ResNum.append('3')  # Leshouches number of constaint variable in Leshouches file 
ResOpt.append(1) #  =1 if Leshouches number consists of one number 
                 #  =2 if Leshouches number consists of two numbers like yukawas vevs below 



ResLabel.append('# m0') 
ResNum.append('1')
ResOpt.append(1)

ResLabel.append('# m12') 
ResNum.append('2')
ResOpt.append(1)


ResLabel.append('vSvR1    # DSB vacuum VEV') 
ResNum.append('1   1')
ResOpt.append(2)


TotNoResult = 0   # Total number of variables for drawing. if it equales 0 then no output.






