
# Chatbot-for-Data-Science-Interview-Questions

This project fills the void of a chat option by presenting a consolidated platform for Data Science interview preparation. It offers a curated collection of interview questions with expert answers, providing a streamlined solution for obtaining comprehensive insights into Data Science interview topics.

## Business Problem 

Unavailability of chat option to get your data science interview questions with your answers, for a one stop solution on your seeking Data Science interview answers for your questions.

## Objective

Unavailability of chat option to get your data science interview questions with your answers, for a one stop solution on your seeking Data Science interview answers for your questions.

## Project Architecture

Data Collections ---> Preprocessing ---> EDA ---> Word Embedding ---> Model Building ---> Deployment

## Python Libraries 

![NumPy](https://img.shields.io/badge/-NumPy-05122A?style=flat&logo=NumPy)&nbsp;
![Pandas](https://img.shields.io/badge/-Pandas-05122A?style=flat&logo=Pandas)&nbsp;
![Matplotlib](https://img.shields.io/badge/-Matplotlib-05122A?style=flat&logo=Matplotlib)&nbsp;
![Seaborn](https://img.shields.io/badge/-Seaborn-05122A?style=flat&logo=Seaborn)&nbsp;
![NLTK](https://img.shields.io/badge/-NLTK-05122A?style=flat&logo=NLTK)&nbsp;
![Scikit-Learn](https://img.shields.io/badge/-ScikitLearn-05122A?style=flat&logo=scikit-learn)\
![Imblearn](https://img.shields.io/badge/-Imblearn-05122A?style=flat&logo=Imblearn)&nbsp;
![Transformers](https://img.shields.io/badge/-Transformers-05122A?style=flat&logo=Transformers)&nbsp;

## Data Collection 

Data science related questions and answers based on topics are extracted from the website https://www.edureka.co/blog/interview-questions/data-science-interview-questions/ using web Harvey tool and newspaper3k
It is saved as an excel file containing 3 columns topics, questions and answers 
It contain 110 questions and answers and 6 unique topics 

## Preprocessing

To preprocess the text, follow these steps: 
convert to lowercase, remove punctuation, digits, and special characters, eliminate stop words, tokenize the text, and perform lemmatization.
We can use Word cloud is another to find the most frequent word.

## EDA

Find the unique topics and number of questions in each topics 
Length of questions and answers in the dataset 
Performed Bigram and Word Cloud for questions and answers  in the dataset 
Performed Bigram and Word Cloud for the first 3 topics i.e. machine learning, deep learning and statistics

## Model Building 

Build a model using Genism Word2vec module and have to import Word2vec from Genism.
![image](https://github.com/nithu24/Chatbot-for-Data-Science-Interview-Questions-/assets/92521223/9be23902-2781-4322-a55b-44cc5a8aadda)


## Python Framework to talk to bot 

![image](https://github.com/nithu24/Chatbot-for-Data-Science-Interview-Questions-/assets/92521223/f6afd012-ba70-4874-8753-62161f860a57/width=100/height=100)
![image](https://github.com/nithu24/Chatbot-for-Data-Science-Interview-Questions-/assets/92521223/ab721228-489e-4ffa-ace1-7d3d74a1cb35/width=100/height=100)


## Deployment

I opted for Streamlit to deploy the solution, recognizing its capability to rapidly transform data scripts into accessible web applications. By simply providing the running script to the tool, it seamlessly converted my work into a user-friendly web app, offering an efficient way to showcase and share the results.
![image](https://github.com/nithu24/Chatbot-for-Data-Science-Interview-Questions-/assets/92521223/11ea174c-948d-4eac-9413-ca127ac26da0)
![image](https://github.com/nithu24/Chatbot-for-Data-Science-Interview-Questions-/assets/92521223/7bcc795e-9a7e-4558-939c-3441a2d75017)


## Challenges 

1) Need more corpus i.e. questions and answers to train the model 
2) If the corpus contains more data then the chatbot can be worked as a intelligent chatbot 
3) Somethings need to rephrase a sentence to get the output even though the trained dataset contains the tokenized questions 
