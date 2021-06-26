# Data-Science-Assignment-

# Overview:
  The goal of this assignment is to develop a noun-chunk based keyword extraction pipeline from
  unstructured text data. The final deliverable is a REST API that takes in a batch of 20 news
  articles as input and returns the top 10 noun chunks encountered in this batch of articles.


# API:
  You can develop this REST API in Flask and deploy it on your local machine to test via Postman.
  The request and response of the API will be in JSON format. Below are details on the format of
  the API and will help you structure it better:

  `Route`: nc_keyword_extraction
  
  `Request`: {"data": ["News Article 1", "News Article 2", "News Article 3" ... "News Article 20"]}
  
  `Response`: {"noun_chunks": {"nc": "Trump Administration", "COVID Vaccine", ... "Crypto trading"}}

# Processing Pipeline:
  To power the API, you'll need to develop a core module that processes the news articles data
  and finds the top 10 noun chunks you need to return to the Flask server. It will have the following
  general components:
    
    1. Noun Chunk extraction engine: You'll need to write a method for finding noun chunks in
    each article. You only need to focus on bigrams and trigrams for now. Unigrams and
    >3-grams can be left out.

    2. Finding top noun chunks: Here, ideally a model (TFIDF/CV) is best suited to find the best
    noun chunks among all the ones extracted in each article. Brownie points for innovating
    with models or approaches  in this section.
    
    3. Eliminating bad noun chunks: Sometimes, you'll get almost duplicate noun chunks or
    ones that do not make sense. You'll need a small post-processing engine to discard or
    deduplicate noun chunks.
