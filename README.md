404 Error Checker (Python)
========================

A Python tool for checking a list of URLS to find out which ones throw a 404 errror.


## Why use this tool?
This tools is ideal for checking the **404** error list that **Google Webmaster Tools** throws whenever these kind of errors arise for a website.

For **SEO** purposes, it is very bad to have lots of 404 erros exist in your site, and it also could irritate users. 

These errors may arrise as a result of a desing change of a website, website migration, or a small change in an htaccess file.

When the script finishes, it shows you a summary of how many urls were broken and how many were correct.


## Requirements
- Python 2.7

## How to use it
1. Have your input URLs ready. Enter one URL per line.
2. On Linux run this script with: 
	``` 
	python 404-checker.py
	```
	or 
	```
	chmod +x 404-checker.py
	./404-checker.py
	```
	If you are using Windows, just double click the file **404-checker.py** 

3. Type the name of your input file.
4. Wait for the script to finish. 


## Issues
### Why is it so slow?
This script appears to be slow because it is being run only on a single thread, so the URLs are checked one at the time.
For a very long list of URLs, this could take a lot of time.

## Future
- In the future I plan refactor this script to make it multithreaded, so a large list of urls can get checked faster.
- I'm open to suggestions.


