# Overview

Selenium powered web scraper for acquiring Vivino wine app reviews from the Google App Store. Results are used 
for needfinding exercises for 'M' assignments in Georgia Tech's CS6750 'Human-Computer Interaction' course, spring
2020 semester. 

# Quickstart

Make sure you have the appropriate Chromedriver version installed and that is available on your path.
From a command prompt, type:

```bash
python VivinoScraper.py --max_reviews 500
```

Scraper results will be written to a timestamped JSON file in the current
directory. The format of the JSON is like the below example:

```json
[{'date': 'January 15, 2020',
  'name': 'Dasha Tuzova',
  'stars': (5, 5),
  'text': 'Super easy to use and very practical. I love wine and I love GOOD '
          "wine but I'm new in this business and so like to experience "
          'different types. If you want to experiment a bit or just do a quick '
          "search of the wines you're contemplating about, this is the app! "
          "Also it has a lot of useful features like sales and 'wine news'",
  'vivino_response': ''},
 {'date': 'January 27, 2020',
  'name': 'Paul de Cort',
  'stars': (4, 5),
  'text': 'Overall I like the app. However one niggle relates to adding the '
          'location where I purchased the wine. Why can I not specify a '
          'location for the wine I purchase, without allowing access to my '
          "current location? I don't usually add wines to my list at the "
          'supermarket when I buy the wines... so the location at at when I '
          'drink them is irrelevant to where I purchased the wines. Please '
          'allow of to search and add locations without the need for the app '
          'to know my current location. Thanks!',
  'vivino_response': ''}]

```

# Troubleshooting

If you have issues downloading the ```spacy``` NLP models, you can download them manually
from [this link](https://spacy.io/models/en), then install them using ```pip```:

```bash
pip install /local/path/to/en_core_web_sm-2.1.0.tar.gz

```

# References

* [LDA Topic Modeling](https://www.analyticsvidhya.com/blog/2018/10/mining-online-reviews-topic-modeling-lda/)