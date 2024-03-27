#################################################################################################################
# Author: Alexander Diedrich
# Initial Date: 05.05.2022
# Updated: 27.03.2024
# Description: Main file to run experiments. All generated files will be written into folder "output".
# Each step generates its own files, which are plaintext and can be inspected. This file performs correlation
# and Granger Causality analysis, and executes diagnosis on simulated (random observations are set to faulty)
# and real fault data (taken from the input process data). 
# NOTE: COMPS.csv must be filled out. Unused Granger and Correlation files can be commented out. 
# All files in "output" folder are generated automatically
#################################################################################################################

import random

#Correlation
import correlation_Simu as corr_Simu
import correlation_IGV as corr_IGV


def runCorrelation():
    #Set here the thresholds that generate outputs
    #thresholds = [0.1, 0.3, 0.5, 0.7, 0.8, 0.9] #Example

    thresholds = [0.9]

    print("Running Correlation Simu")
    path = "../data/four_tanks_stable_res.csv"
    corr_Simu.run_correlationSimu(path, thresholds, prefix="TANKS")

    print("Running Correlation from Jonas Ehrhardt")
    path = "../data/ds1stable.csv"
    corr_Simu.run_correlationSimu(path, thresholds, prefix="DS")


if __name__ == '__main__': 
    random.seed(1337)
    logfile = open("output/diag.log", "w")
    
    #Peform correlation analysis and generate files accordingly
    runCorrelation()

    logfile.close()