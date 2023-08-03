# ERDAS-batch-script
"batch_automate.py" is a simple script used to create a text file that can be used for batch processing in ERDAS IMAGINE. 
This scripit is useful in instances where you need to perform zonal statistics or operations of any kind on stacked raster having more than 100 layers.
The example in the script generates batch commands to calculate mean from daily rainfall (366 images) in the area provided in shapefile. 

# How to use
Step2- Go to ERDAS IMAGINE. Select the operation (Eg: zonal statistics Union/Mean/Sum) - Select the required inputs - Select the output folder
Step3- Go to "batch" option. Copy the command
Step4- Go to script. Enter the __PATH TO YOUR SHAPE FILE___ , __PATH TO YOUR RASTER IMAGE__, ____YOUR SHAPE FILE EXTENT____  from the copied coomand. Write the number layers in your raster in "nof" variable
Step5- Run the script. A text file is generated in current working directory. Open and save as __NAME.bcf__
Step6- In ERDAS batch load the file from "LOAD" option. Run your operation.


