Sketch version of JS-rendered web-scrapping app.
Uses selenium library for extracting info from http://otworywiertnicze.pgi.gov.pl/
Results open in Chrome browser.

How to:
1. Install Chrome and Selenium library for Python 3.

2. DL project files and last version of chromedriver from http://chromedriver.storage.googleapis.com/index.html

3. Unzip chromedriver and copy path location of the file (e.g. C:\Users\Username\Desktop\projects\boreholes\chromedriver.exe).

4. Launch main.py.

So far:
- input check,
- search by years and depth.

To do:
- add other parameters,
- skip passing operators when parameter is not delivered (no limit 'NL'),
- dl results as .csv or/and .db
