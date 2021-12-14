
# Timelog

* Leveraging Language Formality for Sensitivity Classification
* Jack McKechnie
* 2319658M
* Graham McDonald

## Guidance

* This file contains the time log for your project. It will be submitted along with your final dissertation.
* **YOU MUST KEEP THIS UP TO DATE AND UNDER VERSION CONTROL.**
* This timelog should be filled out honestly, regularly (daily) and accurately. It is for *your* benefit.
* Follow the structure provided, grouping time by weeks.  Quantise time to the half hour.

## Week 2

### 27 September 2021
 - 1 hour - Writing inital contact email to Graham McDonald, creating [GitHub repository](https://github.com/JackMcKechnie/Leveraging-Language-Formality-for-Sensitivity-Classification) , reading project moodle and gathering ideas. 

### 28 September 2021
 - 1 hour - [Reading](https://cs.brown.edu/people/epavlick/papers/formality.pdf) and researching 
 - 1 hour - Project session 1
 - 1 hour - Project session 2

### 29 September 2021
 - 0.5 hours - [Reading](https://aclanthology.org/C10-2011.pdf)
 - 1.5 hours - Experimenting with and exploring the dataset from [here](https://cs.brown.edu/people/epavlick/papers/formality.pdf)
 - 1 hour - Reading

### 1 October 2021
 - 1.5 hours - Creating F-Score and adjective density functions

### 3 October 2021
 - 1 hour - Preparation for 3/10/21 meeting

## Week 3

### 4 October 2021
 - 0.5 hours - Weekly meeting
 - 1.5 hours - Reading from Graham McDonald's suggested reading list and experimenting with spellcheck vs formality score correlation

### 5 October 2021
 - 1.5 hours - Reading from Graham McDonald's suggested reading list and experimenting with spellcheck and grammar check vs formality score correlation
 - 2 hours - Reading,  collating a list of features and what papers used which ones, thinking about using readability scores, thinking about adverb usage and learning about K-fold cross validation

### 6 October 2021
 - 1 hour - Summarising papers for easier access later on
 - 1 hour - Reading and experimenting with SciKit Learn's MLPRegressor

### 7 October
- 0.5 hours - Creation of document for next week's meeting 
- 0.5 hours - Reading of how to collect some of the features

### 9 October 2021
 - 3 hours - Collecting as many of the extended dataset features as possible for now. Created and exported heatmap and table of corelation between the features. Reran the MLP regressor and got a score of 0.9986938379261381. Unsure of this score. 

## Week 4

### 11 October 2021
 - 0.5 hours - Weekly meeting

### 12 October 2021
 - 3 hours - Creating table of models and their score for a baseline

### 14 October 2021
 - 1 hour - Reading about clustering

### 15 October 2021
 - 3 Hours - Clustering and reading about topic modelling

## Week 5

### 18 October 2021
 - 2 Hours - Writing first topic modelling code

### 19 October 2021
 - 0.5 Hours - Weekly meeting

### 20 October 2021
 - 3 Hours - Gathering together features categorised by lexical, scores, reading and NLP. Most done but the next ones are more difficult to collect. 

### 21 October 2021
 - 5 Hours <br>
           - Gathering together the other features possible <br>
           - Making sure that there is justification for all of them <br>
           - Making function to run all regression approaches and create table of the results <br>
           - Running and saving results of the above function with the different categories of features <br>
## Week 6

### 25 October 2021
 - 0.5 Hours - Weekly meeting
 - 3 Hours - Tuning regression approaches with GridSearchCV and outputting the results in a table

### 26 October 2021
 - 6.5 Hours - Exploring Keras / Tensorflow and making first deep learning solution

### 27 October 2021
 - 2.5 Hours - Creating LSTM and RNN first attemps

### 28 October 2021 
 - 1.5 Hours - Trying to improve scores on the above

### 29 October 2021
 - 0.5 Hours - Writing formal requirements

### Throughout the week 
 - Reading about things to change / add based on literature from other areas

## Week 7

### 3 November 2021
 - 0.5 Hours - Weekly meeting
 - 2.5 Hours - Getting BERT embeddings working

### 5 November 2021
 - 3 Hours - Getting BERT embeddings working with attention and writing up research questions

### 6 November 2021
 - 3 Hours - Getting BERT working using Hugging Face and using attention layer 
 
### 8 November 2021
 - Reading about side information and writing up research questions

## Week 8

### 10 November 2021
 - 0.5 Hours - Weekly meeting

### 11 November 2021
 - 2 Hours <br>
              - Implementing BERT embeddings to previous models <br>
              - Rerunning old tests with the same train / test split

### 12 November 2021
 - 1 Hour - Rerunning old tests with the same train / test split

### 13 November 2021 
 - 4 Hours <br>
              - Reading about side information <br>
              - Implementing LSTM model for inclusion of side information

### 15 November 2021
 - 1 Hour - Rerunning old tests with the same train / test split

### 16 November 2021
 - 1 Hour - Rerunning old tests with the same train / test split

## Week 9 

### 17 November 2021
 - 4 Hours 
            - Weekly meeting <br>
            - Significance testing of traditional models
            - Rerunning 20 epochs for original side information model
 
 ### 18 November 2021
  - 1.5 Hours - Significance testing and running side model by itself

### 23 November 2021
 - 3 Hours - Significance testing and running new, simpler side model


## Week 10

### 24 November 2021
 - 4 Hours 
            - Weekly meeting <br>
            - Significance testing of traditional models

### 25 November 2021
 - 2.5 Hours - Creating normalised, pretrained and average side information models

### 29 November 2021 
 - 1 Hour - Reading about other possible avenues to look at 

### 30 November 2021
 - 2 Hours - Creating document and trying out some intial tests on new ideas

## Week 11

### 1 December 2021
 - 1 Hour - Setting up and running BERT large with 20 epochs and early stopping
 - 2 Hours - Reading about sensitivity classification

### 2 December 2021
 - 1 Hour - Reading about sensitivity classification

### 3 December 2021
 - 3 Hours - 'Literature review' of sensitivity classification papers
 - 2 Hours - Sorting out saving the previous best model

### 6 December 2021
 - 1 Hour - First attempt at text classification / Research on how to not privelege long documents

### 7 December 2021
 - 1.5 Hours - First attempt at using BERT embeddings for text classification on IMDB Movie Review dataset 

## Week 12

### 8 December 2021
 - 0.5 Hours - Weekly meeting
 - 5.5 Hours - Creating SVM TF-IDF baseline and attempting GLOVE embeddings LSTM model 

### 9 December 2021
 - 6 Hours - GLOVE embeddings LSTM model and Longformer reading / attempt

### 10 December 2021
- 7 Hours - Longformer attempt and BERT chunking attempt

### 13 December 2021
- 4 Hours - BERT chunking and BERT start and end truncated attempt
- 2 Hours - Status report

### 14 December 2021
 - 3 Hours - Redoing BERT start and end truncated with AdamW optimiser 
 - 0.5 Hours - Status report
 - 2 Hours - Longformer attempt 2 (Batch size 1)
 - 0.5 Hours Status report
