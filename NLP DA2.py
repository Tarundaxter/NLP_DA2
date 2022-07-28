Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sent = "Sekiro: Shadows Die Twice is a 2019 action-adventure game developed by FromSoftware and published by Activision. The game follows a shinobi known as Wolf as he attempts to take revenge on a samurai clan who attacked him and kidnapped his lord."
word_tokenize(sent)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    word_tokenize(sent)
NameError: name 'word_tokenize' is not defined
import nltk
word_tokenize(sent)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    word_tokenize(sent)
NameError: name 'word_tokenize' is not defined
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
word_tokenize(sent)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    word_tokenize(sent)
NameError: name 'word_tokenize' is not defined. Did you mean: 'sent_tokenize'?
from nltk.tokenize import word_tokenize
word_tokenize(sent)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    word_tokenize(sent)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\tokenize\__init__.py", line 129, in word_tokenize
    sentences = [text] if preserve_line else sent_tokenize(text, language)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\tokenize\__init__.py", line 106, in sent_tokenize
    tokenizer = load(f"tokenizers/punkt/{language}.pickle")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 750, in load
    opened_resource = _open(resource_url)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 876, in _open
    return find(path_, path + [""]).open()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mpunkt[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('punkt')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mtokenizers/punkt/english.pickle[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
    - ''
**********************************************************************

nltk.download('punkt')
                                                          
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\Tarun\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping tokenizers\punkt.zip.
True
word_tokenize(sent)
                                                          
['Sekiro', ':', 'Shadows', 'Die', 'Twice', 'is', 'a', '2019', 'action-adventure', 'game', 'developed', 'by', 'FromSoftware', 'and', 'published', 'by', 'Activision', '.', 'The', 'game', 'follows', 'a', 'shinobi', 'known', 'as', 'Wolf', 'as', 'he', 'attempts', 'to', 'take', 'revenge', 'on', 'a', 'samurai', 'clan', 'who', 'attacked', 'him', 'and', 'kidnapped', 'his', 'lord', '.']
sent_tokenize(sent)
                                                          
['Sekiro: Shadows Die Twice is a 2019 action-adventure game developed by FromSoftware and published by Activision.', 'The game follows a shinobi known as Wolf as he attempts to take revenge on a samurai clan who attacked him and kidnapped his lord.']
sent.lower()
                                                          
'sekiro: shadows die twice is a 2019 action-adventure game developed by fromsoftware and published by activision. the game follows a shinobi known as wolf as he attempts to take revenge on a samurai clan who attacked him and kidnapped his lord.'
print(stopwords.words('english'))
                                                          
Traceback (most recent call last):
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mstopwords[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('stopwords')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/stopwords.zip/stopwords/[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(stopwords.words('english'))
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mstopwords[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('stopwords')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/stopwords[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

nltk.download('stopwords')
                                            
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\Tarun\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\stopwords.zip.
True
print(stopwords.words('english'))
                                            
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
wtd = word_tokenize(sent)
                                            
str = [word for word in word_tokens if word not in stopword]
                                            
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str = [word for word in word_tokens if word not in stopword]
NameError: name 'word_tokens' is not defined. Did you mean: 'word_tokenize'?
stopword_removal = [word for word in wtd if word not in stopword]
                                            
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    stopword_removal = [word for word in wtd if word not in stopword]
  File "<pyshell#18>", line 1, in <listcomp>
    stopword_removal = [word for word in wtd if word not in stopword]
NameError: name 'stopword' is not defined. Did you mean: 'stopwords'?
stopword_removal = [word for word in word_tokens if word not in str]
                                            
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    stopword_removal = [word for word in word_tokens if word not in str]
NameError: name 'word_tokens' is not defined. Did you mean: 'word_tokenize'?
stopword_removal = [word for word in wtd if word not in str]
                                            
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    stopword_removal = [word for word in wtd if word not in str]
  File "<pyshell#20>", line 1, in <listcomp>
    stopword_removal = [word for word in wtd if word not in str]
TypeError: argument of type 'type' is not iterable
stri = [word for word in wtd if word not in stopword]
                                            
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    stri = [word for word in wtd if word not in stopword]
  File "<pyshell#21>", line 1, in <listcomp>
    stri = [word for word in wtd if word not in stopword]
NameError: name 'stopword' is not defined. Did you mean: 'stopwords'?
stopword = stopwords.words('english')
                                            
stri = [word for word in wtd if word not in stopword]
                                            
print(stri)
                                            
['Sekiro', ':', 'Shadows', 'Die', 'Twice', '2019', 'action-adventure', 'game', 'developed', 'FromSoftware', 'published', 'Activision', '.', 'The', 'game', 'follows', 'shinobi', 'known', 'Wolf', 'attempts', 'take', 'revenge', 'samurai', 'clan', 'attacked', 'kidnapped', 'lord', '.']
from nltk.stem import SnowballStemmer
                                            
stopword = stopwords.words('english')
                                            
snow = SnowballStemmer('english')
                                            
wtd = nltk.word_tokenize(sentence)
                                            
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    wtd = nltk.word_tokenize(sentence)
NameError: name 'sentence' is not defined
wtd = nltk.word_tokenize(sent)
                                            
stem = [snow.stem(word) for word in wtd]
                                            
print(stem)
                                            
['sekiro', ':', 'shadow', 'die', 'twice', 'is', 'a', '2019', 'action-adventur', 'game', 'develop', 'by', 'fromsoftwar', 'and', 'publish', 'by', 'activis', '.', 'the', 'game', 'follow', 'a', 'shinobi', 'known', 'as', 'wolf', 'as', 'he', 'attempt', 'to', 'take', 'reveng', 'on', 'a', 'samurai', 'clan', 'who', 'attack', 'him', 'and', 'kidnap', 'his', 'lord', '.']
from nltk.stem import WordNetLemmatizer
                                            
stopword = stopwords.words('english')
                                            
 wordnetl = WordNetLemmatizer()
                                            
SyntaxError: unexpected indent
wordnetl = WordNetLemmatizer()
                                            
wtd = nltk.word_tokenize(sent)
                                            
lem = [wordnetl.lemmatize(word) for word in wtd]
                                            
Traceback (most recent call last):
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mwordnet[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('wordnet')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/wordnet.zip/wordnet/[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    lem = [wordnetl.lemmatize(word) for word in wtd]
  File "<pyshell#37>", line 1, in <listcomp>
    lem = [wordnetl.lemmatize(word) for word in wtd]
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\stem\wordnet.py", line 45, in lemmatize
    lemmas = wn._morphy(word, pos)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mwordnet[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('wordnet')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/wordnet[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

ntlk.download('wordnet')
                                          
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ntlk.download('wordnet')
NameError: name 'ntlk' is not defined
import nltk
nltk.download('wordnet')
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\Tarun\AppData\Roaming\nltk_data...
True
lem = [wordnetl.lemmatize(word) for word in wtd]
Traceback (most recent call last):
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93momw-1.4[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('omw-1.4')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/omw-1.4.zip/omw-1.4/[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    lem = [wordnetl.lemmatize(word) for word in wtd]
  File "<pyshell#41>", line 1, in <listcomp>
    lem = [wordnetl.lemmatize(word) for word in wtd]
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\stem\wordnet.py", line 45, in lemmatize
    lemmas = wn._morphy(word, pos)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 89, in __load
    corpus = self.__reader_cls(root, *self.__args, **self.__kwargs)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\reader\wordnet.py", line 1176, in __init__
    self.provenances = self.omw_prov()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\reader\wordnet.py", line 1285, in omw_prov
    fileids = self._omw_reader.fileids()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93momw-1.4[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('omw-1.4')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/omw-1.4[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

nltk.download('omw-1.4')
                                          
[nltk_data] Downloading package omw-1.4 to
[nltk_data]     C:\Users\Tarun\AppData\Roaming\nltk_data...
True
lem = [wordnetl.lemmatize(word) for word in wtd]
                                          
print(lem)
                                          
['Sekiro', ':', 'Shadows', 'Die', 'Twice', 'is', 'a', '2019', 'action-adventure', 'game', 'developed', 'by', 'FromSoftware', 'and', 'published', 'by', 'Activision', '.', 'The', 'game', 'follows', 'a', 'shinobi', 'known', 'a', 'Wolf', 'a', 'he', 'attempt', 'to', 'take', 'revenge', 'on', 'a', 'samurai', 'clan', 'who', 'attacked', 'him', 'and', 'kidnapped', 'his', 'lord', '.']
wtag = nltk.word_tokenize(sent)
                                          
postag = nltk.pos_tag(wtag)
                                          
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    postag = nltk.pos_tag(wtag)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\tag\__init__.py", line 165, in pos_tag
    tagger = _get_tagger(lang)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\tag\__init__.py", line 107, in _get_tagger
    tagger = PerceptronTagger()
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\tag\perceptron.py", line 167, in __init__
    find("taggers/averaged_perceptron_tagger/" + PICKLE)
  File "C:\Users\Tarun\AppData\Local\Programs\Python\Python310\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93maveraged_perceptron_tagger[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('averaged_perceptron_tagger')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mtaggers/averaged_perceptron_tagger/averaged_perceptron_tagger.pickle[0m

  Searched in:
    - 'C:\\Users\\Tarun/nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\share\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Local\\Programs\\Python\\Python310\\lib\\nltk_data'
    - 'C:\\Users\\Tarun\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

nltk.download('averaged_perceptron_tagger')
                                                                                               
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\Tarun\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping taggers\averaged_perceptron_tagger.zip.
True
postag = nltk.pos_tag(wtag)
                                                                                               
print(postag)
                                                                                               
[('Sekiro', 'NN'), (':', ':'), ('Shadows', 'NNP'), ('Die', 'NNP'), ('Twice', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('2019', 'CD'), ('action-adventure', 'JJ'), ('game', 'NN'), ('developed', 'VBN'), ('by', 'IN'), ('FromSoftware', 'NNP'), ('and', 'CC'), ('published', 'VBN'), ('by', 'IN'), ('Activision', 'NNP'), ('.', '.'), ('The', 'DT'), ('game', 'NN'), ('follows', 'VBZ'), ('a', 'DT'), ('shinobi', 'JJ'), ('known', 'VBN'), ('as', 'RB'), ('Wolf', 'NNP'), ('as', 'IN'), ('he', 'PRP'), ('attempts', 'VBZ'), ('to', 'TO'), ('take', 'VB'), ('revenge', 'NN'), ('on', 'IN'), ('a', 'DT'), ('samurai', 'NN'), ('clan', 'NN'), ('who', 'WP'), ('attacked', 'VBD'), ('him', 'PRP'), ('and', 'CC'), ('kidnapped', 'VBD'), ('his', 'PRP$'), ('lord', 'NN'), ('.', '.')]
