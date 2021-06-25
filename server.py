import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import en_core_web_sm
import glob
import os,glob
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    from collections import Counter
    lst1=[]
    folder_path = r'C:\Users\user\Desktop\NLP\Data-Science-Assignment\DataSet'
    for filename in glob.glob(os.path.join(folder_path, '*.json')):
        with open(filename, encoding="utf8") as f:
            data=json.load(f)
            #print(data["text"])

            #Tokenization into seneteses 
            words=word_tokenize(data["text"])

            #Stop word filtration 
            stop_words= stopwords.words('english')
    
            filtered_Sentense =[w for w in words if not w.lower() in stop_words]


            filtered_Sentense=" ".join(filtered_Sentense)
            lst=[]

            nlp = en_core_web_sm.load()
            doc=nlp(filtered_Sentense)
            for chunk in doc.noun_chunks:
                lst.append(chunk.text)
            #print(lst)
            for i in lst:
                count=0
                for j in i.split():
                    count=count+1
                if(count==2 or count==3):
                    lst1.append(i)
    Counter = Counter(lst1)
    most_occur = Counter.most_common(10)
    jsonStr = json.dumps(most_occur)
    return (jsonStr)


if __name__ == "__main__":
    app.run(debug=True)