import findClassifiers as fc
import findHelperTools as fh

def findTheBestAny(dataSet,dataSetTest,allPossibleFeatureCombos,Classifier=0, singleXFeatureOn = 0, singleXFeature = ""):
    #Classifiers: 0:linReg, 1:
    #singleXFeatureOn: 0:finds best of all 1:finds best of singleXFeature
    #singleXFeature: put the featue you want to determine here or leave blank to test all
    
    #todo list
    #stats for Linreg
    #binaryClassifier
    #svm
    #pca
    #tree classifier
    #poly svm
    #decisionTreeClassifier
    #randomForrestClassifier
    #StochiasticGradientDescentClassifier
    
    #if we are looking with a single x feature then we will use findTheBest instead of findTheBestAny
    if (singleXFeatureOn==0):
        return(findTheBest(dataSet,dataSetTest,allPossibleFeatureCombos,Classifier))

    #set highs, lows, and holders for bests
    bestR2 = 0
    bestR2MSE = 0
    bestAccuracyScore =0
    bestF1Score =0
    bestxy=[]
    reg = ""
    y = dataSet[singleXFeature]
    #itterate through all possibilities
    for i in range(len(allPossibleFeatureCombos)):
        #grabs current possible combo
        
        myXes =list(allPossibleFeatureCombos[i])

        
        x = dataSet[myXes]
        
        
        
        #this makes sure y isnt in x. that would make this pointless if it was not done
        skipStep = 0
        for k in allPossibleFeatureCombos[i]:
            if(k == singleXFeature):
                skipStep = 1
        
        # calls classifiers and records stats
        if (skipStep == 0):
            #linear regression
            if(Classifier==0):    
                regressionList = fc.LinearRegressionClassifier(x,y,bestR2,bestR2MSE,bestxy,i,allPossibleFeatureCombos,singleXFeature,reg)
                reg = regressionList[0]
                bestR2 = regressionList[1]
                bestR2MSE = regressionList[2]
                bestxy = regressionList[3]
            #Binary Classifier
            if(Classifier==1):
                regressionList = fc.BinaryClassifier(x,y)
                reg = regressionList[0]
                bestAccuracyScore = regressionList[1]
                bestF1Score = regressionList[2]
                bestxy = regressionList[3]
            # SVM Classifier
            if(Classifier==2):
                svmSkip = 0
                ClassCounts = list(dataSet[singleXFeature].value_counts())
                if len(ClassCounts)<2:
                    svmSkip = 1
                if svmSkip == 0:
                    regressionList = fc.SVMClassifier(x,y,bestAccuracyScore,bestF1Score,bestxy,i,allPossibleFeatureCombos,singleXFeature,reg,myXes,dataSetTest)
                    reg = regressionList[0]
                    bestAccuracyScore = regressionList[1]
                    bestF1Score = regressionList[2]
                    bestxy = regressionList[3]
            
    #print and return
    if(Classifier==0): 
        print("the best scoring R2 is ", bestR2, " with the x and y being ",bestxy, " and the MSE being ", bestR2MSE , ".")
    if(Classifier==1):
        print(bestAccuracyScore)
        print(bestF1Score)
        #binary Classifier stats prints
    if(Classifier==2): 
        print("the best scoring accuracy is ", bestAccuracyScore)
        print("best f1 score is ", bestF1Score)
        print("the best x and y are: " , bestxy)
        #svc classfieier stats here
    return(reg)# this returns the actual classifier for later stats


#this findTheBest finds the best set of xes and ys to acheive the highest stats for the particular classifier
def findTheBest(dataSet,dataSetTest,allPossibleFeatureCombos, Classifier =0):
    #set highs, lows, and holders for bests
    bestR2 = 0
    bestR2MSE = 0
    bestAccuracyScore =0
    bestF1Score =0
    bestxy=[]
    reg = ""
    
    #Grab all features
    ListOfFeatures = fh.grabFeatures(dataSet)
    #itterate through all possibilities
    for i in range(len(allPossibleFeatureCombos)): #itterate through all possible combos of features
        myXes =list(allPossibleFeatureCombos[i])
        #print("**********************************************")
        #print(myXes)
        x = dataSet[myXes]
        
        for j in ListOfFeatures: # itterate thorugh list of single features to be determined
            skipMe = 0
            
            # make buckets if using svm classifier
            

            # if using any classifier other than 2
            if skipMe == 0:
                y = dataSet[j]
            
            #make sure y isnt in x and vice versa
            skipStep = 0
            for k in allPossibleFeatureCombos[i]:
                if(k == j):
                    skipStep = 1
            
            #calls classifiers and records stats
            if (skipStep == 0):
                #linear Regression
                if(Classifier==0):    
                    regressionList = fc.LinearRegressionClassifier(x,y,bestR2,bestR2MSE,bestxy,i,allPossibleFeatureCombos,j,reg)
                    reg = regressionList[0]
                    bestR2 = regressionList[1]
                    bestR2MSE = regressionList[2]
                    bestxy = regressionList[3]
                #binary classifier
                if(Classifier==1):
                    reg = fc.BinaryClassifier(x,y)
                #SVM Classifier
                if(Classifier==2):
                    svmSkip = 0
                    ClassCounts = list(y.value_counts())
                    if len(ClassCounts)<2:
                        svmSkip = 1               
                    if svmSkip == 0:
                        # do the bucket function to the data set test dataset.
                        regressionList = fc.SVMClassifier(x,y,bestAccuracyScore,bestF1Score,bestxy,i,allPossibleFeatureCombos,j,reg,myXes,dataSetTest)
                        reg = regressionList[0]
                        bestAccuracyScore = regressionList[1]
                        bestF1Score = regressionList[2]
                        bestxy = regressionList[3]

    #print and return
    if(Classifier==0): 
        print("the best scoring R2 is ", bestR2, " with the x and y being ",bestxy, " and the MSE being ", bestR2MSE , ".")
    if(Classifier==1):
        print("the best scoring accuracy is ", bestAccuracyScore)
        print("best f1 score is ", bestF1Score)
        print("the best x and y are: " , bestxy)
        #binary Classifier stats prints
    if(Classifier==2): 
        print("the best scoring accuracy is ", bestAccuracyScore)
        print("best f1 score is ", bestF1Score)
        print("the best x and y are: " , bestxy)
        #svc classfieier stats here
    return(reg)
