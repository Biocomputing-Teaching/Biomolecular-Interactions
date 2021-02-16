from scrapy.crawler import CrawlerProcess
from .my_spiders import myFirstSpider
import os
import json

def myScrapingFunction(output_file, overwrite=True):
    """

    This function calls the created spider (myFirstSpider in our case) and sets up
    everything to run scrapy from Python. This is the function we call when we want
    to execute the scrapying protocol.

    The only mandatory attribute is the name of the JSON file where we want
    to write the scraped data.

    Attributes
    ----------
    output_file : str
        Path for the output dictionary storing the retrieved information.
    overwrite : bool
        Do we overwrite the dictionary file if it exists (True)? or do we load
        the information from this file and continue (False)?

    """

    # If the JSON file already exists, read the data from it and do not scrape anything.
    if os.path.exists(output_file) and not overwrite:
        print('Json file %s found.' % output_file)
        print('Reading information from %s file.' % output_file)

    # If the JSON file does not exists then we start scrapying the URL given inside
    # the spider definition (see the my_spiders.py).
    elif not os.path.exists(output_file) or overwrite:
        # Here we create a crawler process (the process of going trough the web pages)
        # with some specified settings. Do not worry about the details here.
        process = CrawlerProcess(
                  {'USER_AGENT': 'scrapy',
                   'LOG_LEVEL': 'ERROR'})

        # Now we call our spider adn give it the output file string to store the dictionary.
        process.crawl(myFirstSpider, output_file=output_file)
        # This is what starts the Scrapying process.
        process.start()

    return None
