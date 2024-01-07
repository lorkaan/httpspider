# HTTP Spider

A Spider that works on the HTTP Protocol.

# Goal
This project was created to help me filter though search engine results. Using Google to search specific programming issues was providing answers that was too general and not what I was looking for (How-to's for basic programming, etc.), so this is designed to be run on a web page (such as a Google Search Result) and go though all linked pages to a specified depth and pull out Topical words for each of those pages. The discovered pages and then displayed with the list of topical words. 

# Next Steps
The current definition of Topical word in the system needs to be altered. While common words (and, or, etc.) are ignored, the benchmark frequency for determining if a word is Topical is currently set too high, so it is not uncommon for the system to return no topical words for a page. These settings need to be played with to ensure a more consistent and reliable output.

## How To

`pipenv shell`

If first time:
`nltk.download()`

For help:
`python main.py graph -h` 

Generally
`python main.py graph --root <url> --depth <int>`

if `--depth` > 0, run with maximum given depth
if `--depth` < 0, run until no more links with the same domain as `<url>` is found.

## Notes

### Web Stuff Notes
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
