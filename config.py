HUBSPOT_URL = "https://blog.hubspot.com/"
AVAILABLE_BLOGS = [
    "marketing",
    "service",
    "the-hustle",
    "sales",
    "website",
    "ai",
]
UNWANTED_CHARS = ['"', "'", '.', ',', '?']
NUM_OF_ARTICLES = 3

# stop words from nltk.corpus package
STOP_WORDS = {'because', 'more', 'a', 'just', 'on', 'for', 'doesn', 've', 'after', 'be', 'other', 'shan', 'doing',
              'off', 'wouldn', 'where', 'yours', 'only', 'm', 'here', 'd', 'has', 'am', 'were', 'this', "couldnt",
              'hasn', 'yourself', 'whom', 'no', 'will', "wasnt", 's', 'or', 'through', 'nor', 'll', 'didn', 'own',
              'over', 'o', 'he', "doesnt", 'in', 'does', 'your', "that'll", 'not', 'below', "havent", 'why',
              'himself', "mustnt", 'into', 'don', "arent", "she's", 'what', 'before', 'from', 'it', 'myself', 'each',
              'is', "wouldnt", 'down', 'couldn', 'we', 'up', 'isn', 'so', 'by', 'against', 'between', 'during', 'its',
              'their', 'once', "mightnt", "dont", 'out', 'those', 'having', "you'll", 'any', 'have', 'are', 'the',
              'an', 'ma', "you're", 'she', 'that', 'such', 'needn', 'you', 'most', 'than', 'these', "didnt", 'then',
              "neednt", "shouldnt", 'itself', 'his', 'to', 'if', 'been', 'y', 'hers', 'they', 'mightn', 'i', 'while',
              'do', 'again', 'me', 'about', 're', "it's", "you'd", 'should', 'theirs', "hadnt", 'but', 'ain', 'them',
              'my', 'themselves', "wont", 'had', "hasnt", 't', 'now', 'at', 'further', 'of', "should've", 'all',
              'some', 'haven', 'won', 'above', 'was', "you've", 'and', 'ours', 'being', 'which', 'with', 'until', 'him',
              'there', 'yourselves', 'too', "isnt", 'as', 'mustn', "shant", 'when', 'very', 'few', 'our', 'under',
              'both', 'weren', 'shouldn', 'did', 'hadn', 'who', 'how', 'her', 'ourselves', 'wasn', "werent", 'aren',
              'herself', 'same', 'can'}
