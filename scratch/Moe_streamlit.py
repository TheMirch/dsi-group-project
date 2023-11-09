import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE

## for nltk
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

header = st.container() # Creating containers
dataset = st.container()
features = st.container()
TSNE_visulization = st.container()
model_training = st.container()


wn = WordNetLemmatizer()
def custom_lemmatize(word, tag):
    mapper = {
        'J': wordnet.ADJ,
        'V': wordnet.VERB,
        'N': wordnet.NOUN,
        'R': wordnet.ADV
    }
    pos = mapper.get(tag[0])
    
    return wn.lemmatize(word, pos) if pos else word

with header:
    st.title(' Project 5: Group Project ')
    st.text(' Problem statement here') 

with dataset:
    st.header("NTSB Dataset ")
    st.text('Accident Data Statistical Reviews Safety Research Reports')


    av_df = pd.read_csv('D:\\World\\DSI\\lesson\\706-lesson-streamlit\\data\\aviation_data.csv')
    st.write(av_df.head())

    sel_col, disp_col = st.columns(2)
    state = sel_col.selectbox('State',  av_df['State'].unique())

    state_data = av_df[av_df['State'] == state]
    df = av_df[av_df['State'] == state] ## Concatenate
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True      )
     
    #calculate
    total_events = len(state_data)
    event_type_distribution = state_data['EventType'].value_counts()
    weather_condition_distribution = state_data['WeatherCondition'].value_counts()
    safety_rec_distribution = state_data['HasSafetyRec'].value_counts()
    highest_in = state_data['HighestInjuryLevel'].value_counts()
    #aircraft_distribution = state_data['AirCraft'].value_counts()
    aircraft_damage = state_data['AirCraftDamage'].value_counts()
    st.write(total_events, event_type_distribution, weather_condition_distribution, safety_rec_distribution,highest_in,aircraft_damage) #aircraft_distribution ,

        

with features:
    st.header("The features we used")
    columns_to_drop = ['NtsbNo', 'Mkey', 'ReportNo', 'EventID', 'City', 'State', 'Country', 'ReportType', 
                   'OriginalPublishDate', 'AirportID', 'AirportName', 'FAR', 'Operator', 'ReportStatus', 
                   'DocketUrl', 'DocketPublishDate', 'Unnamed: 37', 'N', 'EventType', 'EventDate', 'HasSafetyRec', 
                   'RepGenFlag']
    df.drop(columns=columns_to_drop, inplace=True)
    col_name = pd.DataFrame(df.columns).reset_index(drop=True)
    st.text(f'{col_name}')





    df_lem = df['ProbableCause'].apply(lambda cause : ' '.join([custom_lemmatize(word, tag) for word, tag in nltk.pos_tag(cause.split())]))
    cvec = CountVectorizer(stop_words='english', ngram_range=(5,5))
    df_cvec = cvec.fit_transform(df_lem)
    freq_ngarms = pd.DataFrame(df_cvec.todense(), columns = cvec.get_feature_names_out()).sum().sort_values( ascending = False).head(50)
    plt.figure(figsize=(10,12))
    freq_ngarms.sort_values(ascending = True).plot.barh()
    st.pyplot(plt)

    df['Make']= df['Make'].str.lower()
    make_air = pd.DataFrame(df['Make'].unique())
    top_causes = df['Make'].value_counts().head(50)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_causes.values, y=top_causes.index, palette="viridis")
    plt.title("Top 50 Aircraft Makes")
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Make")
    st.pyplot(plt.gcf())  # Use plt.gcf() to get the current figure
  
with TSNE_visulization:
    st.header('TSNE Visulization')
    #n = sel_col.selectbox('n', range(3))
    n=3


    df.reset_index(drop=True, inplace=True)
    color_palette = [ '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']
    ##==3d==##
    # def tsne_viz(df, n, stop='english'):
    
    #     cvec = TfidfVectorizer(ngram_range=(n,n), stop_words=stop)
    #     vectorized_matrix = cvec.fit_transform(df_lem)
        
    #     tsne = TSNE(n_components=3, random_state=42)
    #     tsne_results = tsne.fit_transform(vectorized_matrix.toarray())
        
    #     fig = plt.figure(figsize=(9,4))
    #     ax = fig.add_subplot(111, projection='3d')
        
    #     scatter = ax.scatter(tsne_results[:,0], tsne_results[:,1], tsne_results[:,2], 
    #                         c=pd.factorize(df['HighestInjuryLevel'])[0], cmap="viridis", s=60)
        
    #     legend1 = ax.legend(*scatter.legend_elements(), title="Highest Injury Level")
    #     ax.add_artist(legend1)
        
    #     ax.set_title('3D t-SNE Visualization')
    #     ax.set_xlabel('t-SNE Dimension 1')
    #     ax.set_ylabel('t-SNE Dimension 2')
    #     ax.set_zlabel('t-SNE Dimension 3')
        
    #     plt.show()
    #     st.pyplot(plt.gcf()) 

    def tsne_viz_2d(df, n, stop='english'):
    
        cvec = TfidfVectorizer(ngram_range=(n,n), stop_words=stop)
        vectorized_matrix = cvec.fit_transform(df_lem)
        
        tsne = TSNE(n_components=2, random_state=42)
        tsne_results = tsne.fit_transform(vectorized_matrix.toarray())
        
        fig, ax = plt.subplots(figsize=(9,6))
        
        scatter = ax.scatter(tsne_results[:,0], tsne_results[:,1], 
                            c=pd.factorize(df['HighestInjuryLevel'])[0], cmap="viridis", s=60)
        
        legend1 = ax.legend(*scatter.legend_elements(), title="Highest Injury Level")
        ax.add_artist(legend1)
        
        ax.set_title('2D t-SNE Visualization')
        ax.set_xlabel('t-SNE Dimension 1')
        ax.set_ylabel('t-SNE Dimension 2')
        
        st.pyplot(fig)
    
   

    tsne_viz_2d(df, n, stop='english')

with model_training:
    st.header("The models we trained")
    st.text('Logistic Regression Model')

    X = df['ProbableCause']
    y = df['HighestInjuryLevel']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_train = cvec.transform(X_train)
    X_test = cvec.transform(X_test)
    X_train_df = pd.DataFrame(X_train.todense(), columns=cvec.get_feature_names_out())

    lr = LogisticRegression(penalty = 'l1', solver='liblinear')
    lr.fit(X_train, y_train)

    preds = lr.predict(X_test)
    score_train = lr.score(X_train, y_train)
    score_test = lr.score(X_test, y_test)
    st.text(f'score train: {score_train} , score test: {score_test}' )
    


# NLP for pilot vs engin vs train vs weather condition