# About
<__"batch_automate.py"__> is a simple script used to create a text/bcf file that can be used for batch processing in ERDAS IMAGINE. 
This script is helpful if you need to do zonal statistics or any other operations on a stacked raster with more than 100 layers. The script's sample here creates batch commands to compute the average from daily rainfall (366 images) for the area specified in the shapefile. You also find "***bas_rf_2002.bcf***" file created using the script in this repository

# How to use
 ***Step1*** - Go to ERDAS IMAGINE. Select the operation (Eg: zonal statistics Union/Mean/Sum) - Select the required inputs - Select the output folder  
***Step2***- Go to "batch" option. Copy the command  
***Step3***- Go to script. Enter the ___ __PATH TO YOUR SHAPE FILE__ ___ ,___ __PATH TO YOUR RASTER IMAGE__ ___, ___ ____YOUR SHAPE FILE EXTENT____ ___  from the copied coomand. Write the number layers in your raster in "nof" variable  
***Step4***- Run the script. A text file is generated in current working directory. Open and save as ***__name.bcf__***  
***Step5***- In ERDAS batch load the file from "LOAD" option. Run your operation.  

