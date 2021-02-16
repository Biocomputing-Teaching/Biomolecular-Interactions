# Scraping data from databases

### Requirements

* Setting up your computer with a Linux or macOS operating system (see course repository)

* Install Conda and Jupyter Lab (see course repository)

* Complete the "Learn the Basics" entries in the Python Tutorial

* Install the scrapy library. Open up a terminal and write:

```
conda install -c anaconda scrapy
```

* Install the Google Chrome navigator if you have not already installed it:

[Get Chrome](https://www.google.com/chrome/)

If you have doubts please read the following for Ubuntu:
[How to install Chrome on Ubuntu](https://linuxize.com/post/how-to-install-google-chrome-web-browser-on-ubuntu-20-04/)

* We need Chrome since we will make use of the selector gadget. Please add it to your Chrome extensions:

[Selector gadget for Chrome](https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb)

### Introduction

In this tutorial we will use a pre-setup library for getting data automatically
from any web-based database. We will employ the scrapy library for navigating automatically
through any web site and we will use a powerful CSS selection method. Don't worry now about
how CSS works we will use a tool to help us out to get the rigth selection. However, it is a good
idea to get familiar with some basics on how a web site is structured, so please review
the introduction page of the following link:

[What is HTML?](w3schools.com/html/html_intro.asp)
