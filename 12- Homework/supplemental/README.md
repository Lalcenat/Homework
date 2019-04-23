# Supplementary Notes For Lesson 12
## Disclaimer
All supplementary notes are in relation to your Data Visualization course only. As some of these concepts branch into Computer Science, I want to keep your understanding simple and may omit details which are too complicated at this point.

## 12.2
### Objectives
* Learn webscraping and storing them into a NoSQL database

### Pre-lesson installation

Please install them into your local machine before class begins.

#### Python HTML parser - Beautiful Soup
Parses HTML elements into objects for Python

Documentation: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```
pip install bs4
```

#### Python Requests
Allows you to connect with URLs and get or post data with code.

Documentation: [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)
```
pip install requests
```

#### Selenium & Splinter
Software to manipulate web browser clients

Selenium Doc: [https://seleniumhq.github.io/selenium/docs/api/py/api.html](https://seleniumhq.github.io/selenium/docs/api/py/api.html)
Splinter Doc: [https://splinter.readthedocs.io/en/latest/](https://splinter.readthedocs.io/en/latest/)

```
conda install -c conda-forge selenium
conda install -c clinicalgraphics selenium-chromedriver
pip install splinter
```