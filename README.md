# Naive-Bayes-Text-Classification
Introduction: Naive Bayes is a family  of probabilistic classifiers based on Bayes theorem with relations between the features. It is highly scalable, requiring a number of features in the learning problem. Text classification is a common problem which can be solved using Naive Baye's few of them are Sentiment analysis,  age/gender identification, spam filtering, making decisions about treatment processes etc. A common text classification problem using Naive Bayes looks like this: Given an input document d and a fixed set of classes c={c1,c2,c3} output a predicted class c belongs to C. Text classification is depended upon a simple approach of representing the word document using bag of words approach (preprocessing step). Stopwords are type of words which are usually uninformative, and these need to be removed during the preprocessing. Stemming and Lemmatization are the next steps for converting the words into their root form, however both these steps have a very less impact in the process of text classification.
Now let's look at the common formula for realizing naive bayes approach: P(c|d) =(P(d|c)*P(c))/P(d)
Few of the advantages of using Naive Bayes approach are:
•	It is pretty quick with very low storage requirements.
•	It's robust to irrelevant features. (they get cancelled out)
•	Good in domains with important features
•	Provides a good dependable baseline for text classification

Problem Statement: 
Your code should accomplish the following tasks: 

1) Pre-processing step: 
This first step converts scientific articles into features to be used by a Naive Bayes classifier. You will be using the bag of words approach. The following steps outline the process involved:
	a. Form the vocabulary. The vocabulary consists of the set of all the words that are in the training data with stop words removed (stop words are common, uninformative words such as "a" and "the" that are listed in the file stoplist.txt). The vocabulary will now be the features of your training data. Keep the vocabulary in alphabetical order.
	b. Now, convert the training data into a set of features. Let M be the size of your vocabulary. For each article, you will convert it into a feature vector of size M+1. Each slot in that feature vector takes the value of 0 or 1. For the first M slots, if the ith slot is 1, it means that the ith word in the vocabulary is present in the article; otherwise, if it is 0, then the ith word is not present in the article. Most of the first M feature vector slots will be 0. Since you are keeping the vocabulary in alphabetical order, the first feature will be the first word alphabetically in the vocabulary. The (M+1)th slot corresponds to the class label. An A in this slot means the article is from class “arxiv” while a J in this slot means the article is from class “jdm” and a P in this slot means the article is from class “plos”.
2) Classification step:
	a. In the first phase, which is the training phase, the naive Bayes classifier reads in the training data along with the training labels and learns the parameters used by the classifier.
	b. In the testing phase, the trained naive Bayes classifier classifies the data in the testing data file. You will need to convert the articles in the testing data into a feature vector, just like in the training data where a 1 in the ith slot indicates the presence of the ith word in the vocabulary while a 0 indicates the absence. If you encounter a word in the testing data that is not present in your vocabulary, ignore that word. Note that the feature vector is only of size M because the class labels are not part of the testing data
	c. Output the accuracy of the naive Bayes classifier by comparing the predicted class label of each article in the testing data to the actual class label. The accuracy is the number of correct predictions divided by the total number of predictions.

Implementation:
The python file bayes.py implements the solution for the problem statement accordingly:
•	Initially all the necessary packages are imported (glob, collections, nltk, re etc)
•	After this, all the necessary variables are initialized.
•	Then the createvocabulary function takes in the articles from all three domains and performs stemming and lemmatization on it, also removes all the irrelevant punctuations and symbols.
•	After this, the stopwords file is read and all the unnecessary stopwords from the articles are removed and a vocabulary is created which is arranged alphabetically to finish the first step of preprocessing.
•	This ordered vocabulary is then passed to createfeaturematrix along with the classlabels. This results in creating the feature vector for each class thereby creating the respective key, value pairs based on their occurence thereby finishing the first step of preprocessing.
•	After this, the individual matrices for all the three domains are calculated in the functions matrixarxiv, matrixplos, matrixjdm and then the total summation is calculated inside the function addalllval.
•	The test feature matrix is then created inside the createtestmat in the same way as we did earlier.
•	The function calculatebayesprobability  then takes in input parameters passed and calculates the individual probabilities. Then based on this probability values it classifies the articles into respective classes. These articles are then displayed by representing actual class and classified class.
•	Finally, the output accuracy of Naive Bayes is displayed.
•	Then, the output accuracy of each individual class is displayed.

 

