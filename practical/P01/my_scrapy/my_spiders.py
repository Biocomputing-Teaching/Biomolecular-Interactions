import scrapy
import json
import time

class myFirstSpider(scrapy.Spider):
    """
    Blank Scrapy Spider to retrieve information for a generic web site. It contains all
    the code to set up a first program to begin scraping from any web site. Just add
    the URL and start select things from the "response" object.

    When the spider has done scrapying, all scraped data stored in the "self.my_dictionary"
    object will be written down into a JSON formatted file. Be mindful that JSON only can
    write string type objects, so you need to convert everything into a string before storing it
    into the dictionary.

    """
    allowed_domains = ['HERE PUT THE DOMAIN OF THE WEB']

    def __init__(self, output_file=None, **kwargs):
        """
        Here we initialize the spider class with our specific variables. The "output_file"
        variable is the name of the file that will be written when we are done scrapying things.
        """

        self.my_dictionary = {}
        self.output_file = open(output_file, 'w')

    def start_requests(self):
        """
        This function defines the first call to the web site of interest uisng scrapy.Request() method.
        """
        yield scrapy.Request('HERE PUT THE SPECIFIC WEB PAGE YOU WANT TO GET DATA FROM')

    def parse(self, response):
        """
        The code here is used to select all you want from the URL by employing CSS or XPATH
        selection syntaxis. The "response" object is where you start selecting things by calling:

        response.css('A CSS SELECTION')
        """

        ## Here we start scrapying things from the url ##
        response #  Remember the response object contains all the HTML data from the Web site.

     def closed(self, spider):
        """
        This functions is executed when the spider has done parsing. It will write the
        "self.my_dictionary" content into a JSON formatted file with the name stored at
        "self.output_file".
        """
        json.dump(self.my_dictionary, self.output_file)
        self.output_file.close()
