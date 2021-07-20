import sys, os
import numpy as np 
import pandas as pd 
#import pingouin as pg

outputPath = input("\n Giving the output directory: ")

# Setting constraint in case someone test it occasionally
errorCount = 0

# Common affine in our lab
AffineDict = {
            "1" : np.array([[-1.50000000e+00,  0.00000000e+00,  0.00000000e+00, 9.00000000e+01],
                            [ 1.99278252e-16,  1.50000000e+00,  2.17210575e-16, -1.26000000e+02],
                            [-1.36305018e-16, -1.38272305e-16,  1.50000000e+00, -7.20000000e+01],
                            [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 1.00000000e+00]]), 

            "2" : np.array([[ 2., 0., 0., -90.],
                            [ 0., 2., 0., -126.],
                            [ 0., 0., 2., -72.],
                            [ 0., 0., 0., 1.]]), 

            "3" : np.array([[ -3., 0., 0.,  78.],
                            [  0., 3., 0., -112.],
                            [  0., 0., 3., -70.],
                            [  0., 0., 0.,  1.]])
            }
while True:
    imgType = input("Select your image Type, \n\n(1) VBM, \n(2) Diffusion, \n(3) Functional \n\n")
    try:
        imgAffine = AffineDict[imgType]
        print(imgAffine)
        break
    except KeyError:
        if not errorCount ==5:
            errorCount += 1 
            print(f"\n\nCheck your input, it should be in range [1,3], \033[31mErrorCount: {errorCount}\033[00m\n\n")
        else:
            sys.exit('Too many errors, sys closed, bye')
        

while True:
    CordinatePath = input("Select the cordinate csv: ")
    try:
        CordinateFile = pd.read_csv(CordinatePath) 
        break
    except :
        if not errorCount ==5:
            errorCount += 1
            print(f"\n\n\033[31mErrorCount: {errorCount}\033[00m,\n\nFile not found, make sure you got the right location toward your data\n\n")
        else:
            sys.exit('Too many errors, sys closed, bye')

CordinateFile = CordinateFile[["x", "y", "z", "constant"]]

# Using linear algengra for quick solving
new_CordinateArray = np.matmul(np.linalg.inv(imgAffine),CordinateFile.values.T).T
new_CordinateFile = pd.DataFrame(new_CordinateArray, columns=["i", "j", "k", "constant"])
outputName = input("\n\033[93mName of the output? \033[00m")
new_CordinateFile.to_csv(os.path.join(outputPath, f"{outputName}.csv"))


#pg.partial_corr(data=df,x = "HAM-D", y ='SA', covar= [ "gender", " age" ,"years of education"])