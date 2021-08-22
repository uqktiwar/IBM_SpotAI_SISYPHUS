# IBM_AISpot_SISYPHUS
Submission for the IBM CFC AI Spot Challenge

# Solution Description
For the AI Spot Challenge we utilized an appropriate hybrid data-management strategy. 
We tested multiple supervised machine learning algorithms using the Cloud Pak Auto AI service with our ground-up built dataset. 
We are exploring Watson Studio & Cloud Pak for future unsupervised ML (e.g., dimensionality reduction) with our multicloud data platform. 
We can scale the data architecture across government, professional and community stakeholders for needed capabilities to drive smarter mitigation planning decisions and prioritize project implementation. 

Our ultimate aim is to reliably predict the flood risk associated with properties in New Orleans (our pilot city for this project) and deliver the results 
to different stake holders (home-owners, government officials etc.) in an interactive manner combining the power of machine learning/AI and augmented reality. 
For the IBM CFC Global challenge, we submitted a web app (https://github.com/trungvu08/CFC_SISYPHUS_Global_Systems) that utilizes ArcGIS maps and WebXR to provide different users 
with an immersive augmented reality experience of assessing their properties' flood risks, and viewing their city's green and grey infrastructure. 
The immersive experiences in that solution were provided as demonstrations.

For the AI Spot challenge, we took the first step towards completing the back end code to enable automated predictions of flood risk for individual properties.
Since, we are not currently at liberty to release data from indivdual properties, we aggregated the data according to census blocks. 
We used this test dataset (flood_risk_binary_rm_ufeats_labels.csv) describing various attributes (land use, water area, tree count, no. of buildings, repetitive flood loss etc.) of these census blocks to predict the FIRM score.
The FIRM score represents a "Flood insurance rating" issued by the Federal Emergency Management Agency (FEMA), with a high FIRM score indicative of a high flood risk. 

# About the Dataset
## The following variables were used as predictors in our model:

LOTCNT= Total number of lots per census block group

GRADEDLOTS= number of lots we survey in research

STRUCTURE= number of structure (building) per census block group

VACANT= number of vacant lot per census block group

VACANT%= percentage of vacant 

SLAB= number of slab structure per census block group

CRAWLSP= number of crawlspace structure per census block group

RAISED= number of raised structure per census block group

FREEBRD= number of freeboard structure per census block group (important: these are structure that are mitigated)

RLPROP= number of Repetitive floor loss properties per census block group (important: these till how many properties flood repeatedly)

CLAIMSTL= total number of flood claims per census block group

AVECLAIMS= Average number of claims per Repetitive flood loss property

LOTTOTACRES= census block group total area in acres

LOTAVEACRES= lot average area in acres

LOTSTDEV= lot average area standard deviation 

BLKGRPACRES= block average area in acres

BLKCOUNT= block per census block group

LOT/BLK= average number of lots per block

ROADAREAACRES= road area in meter square

ROAD/LOT= road to lot ratio

TREECNT= total number of trees per census block group

TREE/ACRE=trees per acre

HISTZONE= historic zone land use (1 good to 7 bad)

## The following attribute was predicted:

FIRM_BINARY = [Low_Risk, High_Risk]

# Methodology
## Training and Selecting the Best ML Model

We used the IBM Auto AI Service to test multiple machine learning algorithms to finally select the "Extra Trees Classifier" as the best algorithm for modelling our data. 

**Model information**

**Prediction column:** FIRM_BIN

**Algorithm:** Extra Trees Classifier

**Number of features:** 45

**Number of evaluation instances:** 45

**Created on:** 8/22/2021, 2:49:52 PM

**Model URL:** https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f9b11549-b397-4e77-aa21-d8eaff21c64c/predictions?version=2021-08-22

**Model Evaluation** The accuracy score for the model was 0.835

**ROC Curve**

![ROC Curve](https://raw.githubusercontent.com/uqktiwar/IBM_SpotAI_SISYPHUS/main/ModelROC.png)

**Confusion Matrix**

![Confusion Matrix](https://raw.githubusercontent.com/uqktiwar/IBM_SpotAI_SISYPHUS/main/ConfusionMatrix.png)

It is evident above that the model can be improved further, which we are continuing work on. 


# To run our submission

Our final submission for this challenge is a Flask based webapp that uses the above built model for predicting the Flood Risk given input data. 

**To successfully run the web app:**

*Important prerequisite - Python 3.6 or higher must be installed on your system* 

1. Clone this repository to your local system

       git clone https://github.com/uqktiwar/IBM_SpotAI_SISYPHUS.git

       or

       download the directory as a ZIP archive and unzip

2. Navigate into the IBM_SpotAI_SISYPHUS-main directory

        cd IBM_SpotAI_SISYPHUS-main

3. Install the required python modules using:
        
        pip install -r requirements.txt
     
4. Run the web app by:
        
        python floodriskapp.py

**The address of the server on which the app is deployed will be included in the output of this command, for ex. http://172.26.73.253:5000/**

5. The first page of the app will look something like this:

![APP INPUT PAGE](https://raw.githubusercontent.com/uqktiwar/IBM_SpotAI_SISYPHUS/main/inpPage.png)

Before submitting the form, please adjust the values for each variable using the up/down arrow buttons that appear when you hover over an input field 

6. The output page should look as follows: 

![APP OUTPUT PAGE](https://raw.githubusercontent.com/uqktiwar/IBM_SpotAI_SISYPHUS/main/predPage.png)














