import streamlit as st
import base64
import pickle 
import re
import string
import nltk
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from textblob import TextBlob
import pickle
import pandas as pd
import json
import re
import random
import nltk
from nltk.corpus import stopwords
import gensim
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.simplefilter('ignore')

data = pd.read_pickle('data.pkl')

# title

html_temp = """
   
    <div style="background-color:orange;padding:10px">
    <h1 style="color:blue;text-align:center;">DAT-SCI ---> Data Science Question Answer ChatBot </h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

main_bg = "new.jpg"
main_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# get input text

#form = st.form(key='my-form')
#sentence = form.text_input('Enter input')
#submit = form.form_submit_button('Submit')
sentence = st.text_input("USER :","")   

    
model = pd.read_pickle('model.pkl')
#data_language = pd.read_pickle('data_language.pkl')
model_ml = gensim.models.KeyedVectors.load("chatbot_word2vec_machine learning.bin")
model_stat = gensim.models.KeyedVectors.load("chatbot_word2vec_statistics.bin")
model_dl = gensim.models.KeyedVectors.load("chatbot_word2vec_deep learning.bin")
model_da = gensim.models.KeyedVectors.load("chatbot_word2vec_data analytics.bin")
model_nlp = gensim.models.KeyedVectors.load("chatbot_word2vec_nlp.bin")
model_bds = gensim.models.KeyedVectors.load("chatbot_word2vec_basic data science.bin")

data_language_ml = pd.read_pickle('data_language_ml.pkl')
data_language_stat = pd.read_pickle('data_language_stat.pkl')
data_language_dl = pd.read_pickle('data_language_dl.pkl')
data_language_da = pd.read_pickle('data_language_da.pkl')
data_language_nlp = pd.read_pickle('data_language_nlp.pkl')
data_language_bds = pd.read_pickle('data_language_bds.pkl')

GREETING_INPUTS = ("hello", "hi", "greetings", "hello i need help", "good day", "hey", "i need help", "who are you?")
GREETING_RESPONSES = ["Hey, My name is DAT-SCI, Data Science Question Answer ChatBot. How can i help you?  Please select one of the topic you want to know in Data Science from the top options"]
            

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        
        
def lemmatize_text(questions):
    stop_words = stopwords.words("english")
    questions = [re.sub('[^a-z(c++)(c#)]', ' ', x.lower()) for x in questions]
    questions_tokens = [nltk.word_tokenize(t) for t in questions]
    questions_stop = [[t for t in tokens if (t not in stop_words) and (3 < len(t.strip()) < 15)]
                      for tokens in questions_tokens]
    
    questions_stop = pd.Series(questions_stop)
    return questions_stop

def talk_to_bot(data_language, model):
    sentence_pp = lemmatize_text(pd.Series(sentence)) 
    cosines = []
    try:
        question_vectors = []
        for token in sentence_pp:
            try:
                vector = model.wv[token]
                question_vectors.append(vector)
            except:
                continue
        question_ap = list(pd.DataFrame(question_vectors[0]).mean())
        for t in data_language['Average_Pooling']:
            if t is not None and len(t) == len(question_ap):
                val = cosine_similarity([question_ap], [t])
                cosines.append(val[0][0])
            else:
                cosines.append(0)
    except:
        pass
            
    if len(cosines) == 0:
        not_understood = "OOPS, I don't understand. Can you rephrase it?"
        return not_understood  
    else: 
        index_s =[]
        score_s = []
        for i in range(len(cosines)):
            x = cosines[i]
            if x >= 0.5:
                index_s.append(i)
                score_s.append(cosines[i])
        reply_indexes = pd.DataFrame({'index': index_s, 'score': score_s})
        reply_indexes = reply_indexes.sort_values(by="score" , ascending=False)
        r_index = int(reply_indexes['index'].iloc[0])
        r_score = float(reply_indexes['score'].iloc[0])
        reply = str(data_language.iloc[:,2][r_index])  
    return reply


# return response
st.button("Send")

menu = ["machine learning","statistics","deep learning","data analytics","nlp","basic data science"]
choice = st.radio("PLEASE SELECT THE TOPICS YOU WANT TO KNOW IN DATA SCIENCE",menu, key = "<uniquevalueofsomesort>")

if choice == "machine learning":
    with st.spinner("Thinking ..."):
        if(sentence.lower() != 'bye'):
            if(greeting(sentence.lower()) != None):
                st.text_area("DAT-SCI :", greeting(sentence.lower()))
            else:
                reply = talk_to_bot(data_language_ml,model_ml)
                st.text_area("DAT-SCI :", reply)
        else:
            st.text_area("DAT-SCI :", 'Bye! Hope that I am useful to you. Have a nice day.')
elif choice == "statistics":
    with st.spinner("Thinking ..."):
        if(sentence.lower() != 'bye'):
            if(greeting(sentence.lower()) != None):
                st.text_area("DAT-SCI :",greeting(sentence.lower()))
            else:
                reply = talk_to_bot(data_language_stat,model_stat)
                st.text_area("DAT-SCI :",reply)    
        else:
            st.text_area("DAT-SCI :",'Bye! Hope that I am useful to you. Have a nice day.')
elif choice == "deep learning":
    with st.spinner("Thinking ..."):
        if(sentence.lower() != 'bye'):
            if(greeting(sentence.lower()) != None):
                st.text_area("DAT-SCI :",greeting(sentence.lower()))
            else:
                reply = talk_to_bot(data_language_dl,model_dl)
                st.text_area("DAT-SCI :",reply)
        else:
            st.text_area("DAT-SCI :",'Bye! Hope that I am useful to you. Have a nice day.')
elif choice == "data analytics":
    with st.spinner("Thinking ..."):
        if(sentence.lower() != 'bye'):
            if(greeting(sentence.lower()) != None):
                st.text_area("DAT-SCI :",greeting(sentence.lower()))
            else:
                reply = talk_to_bot(data_language_da,model_da)
                st.text_area("DAT-SCI :",reply)   
        else:
            st.text_area("DAT-SCI :",'Bye! Hope that I am useful to you. Have a nice day.') 
elif choice == "nlp":
    with st.spinner("Thinking ..."):
        if(sentence.lower() != 'bye'):
            if(greeting(sentence.lower()) != None):
                st.text_area("DAT-SCI :",greeting(sentence.lower()))
            else:
                reply = talk_to_bot(data_language_nlp,model_nlp)
                st.text_area("DAT-SCI :",reply) 
        else:
            st.text_area("DAT-SCI :",'Bye! Hope that I am useful to you. Have a nice day.')  
elif choice == "basic data science":
    with st.spinner("Thinking ..."):
        if(sentence.lower() != 'bye'):
            if(greeting(sentence.lower()) != None):
                st.text_area("DAT-SCI :",greeting(sentence.lower()))
            else:
                reply = talk_to_bot(data_language_bds,model_bds)
                st.text_area("DAT-SCI :",reply)
        else:
            st.text_area("DAT-SCI :",'Bye! Hope that I am useful to you. Have a nice day.')

        
