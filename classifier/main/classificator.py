from bs4 import BeautifulSoup
import pickle
import re
from nltk.stem import WordNetLemmatizer

class MainClassify:

    def choose_class(string):
        documents = [string]


        #print(documents)

        #Как загрузить модель
        classifier, freq_vector = pickle.load(open("model.sav", "rb"))

        X_train_freq2 = freq_vector.transform(documents)
        result = classifier.predict(X_train_freq2)
        #print("y_pred_2", result)
        return result[0]