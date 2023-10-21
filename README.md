# HTTP Spider

A Spider that works on the HTTP Protocol.

## How To

`pipenv shell`

If first time:
```
pipenv install
nltk.download()
```

For help:
`python main.py graph -h` 

Generally
`python main.py graph --root <url> --depth <int>`

if `--depth` > 0, run with maximum given depth
if `--depth` < 0, run until no more links with the same domain as `<url>` is found.

## Notes

### Web Stuff Note
- Currently treats www.domain.com differently from domain.com
- Only handles the basic Http(s) urls
    - E.g. does not handle mailto: links
- While URLs with parameters are processed as normal, the spider will strip the parameters from the url when storing it as an "already-processed" url and will not
process that page again if found with different parameters.

### NLP Notes
- Natural Language Processing is currently very basic (just word frequecy) and is hardcoded to be any word that is used in 10% of the document
- Lemmatization is done on the words processed.
- Punctuation is ignored, as are function words (the, and, or, etc.)

## Natural Language Processing

Currently, uses the nltk to perform word frequency analysis.

Note: In order to avoid lookup errors and have the natural language analysis done right, the comaand nltk.download() had to run.

(Setup script coming soon)
