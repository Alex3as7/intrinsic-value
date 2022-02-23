# intrinsic-value


Kivy is utilised in order to provide simple and sustainable GUI components to the program
Uses the Yahoo Finance Api and BeautifulSoup4 to analyse financial data and calculate the intrinsic value of a valid stock using an adjusted Benjamin Graham formula, which is:

V = (EPS * (7 x g) * AAA)/Y 

Where:
V = the value expected from the growth formulas over the next 5 years

EPS = the company’s last 12-month earnings per share

7 = P/E base for a no-growth company

g = reasonably expected 5 year growth rate

AAA = the average yield of AAA corporate bonds in 1962 (Graham did not specify the duration of the bonds, though it has been asserted that he used 20 year AAA bonds as his benchmark for this variable)

Y = the current yield on AAA corporate bonds.


TO USE:
Make sure all requirements listed above are installed, and add the API key of your yahoo finance account to the 'api_key.json' file.
