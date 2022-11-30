# Project 3 

For Project 3, I created a scrypt that searches for breweries in a given city in alphabetical order

<h2>
  How To Use
</h2> 
<p>  
  Before beginning, import these libraries: 

```python
pip install flask
pip install requests
```

 To start, run the "start.py" file. This will create a locl server on port 5000<br>
 If no errors are thrown and the scrypt is still running, you're good to go <br>
  
 Now in a browser, go to http://localhost:5000<br>
  
 Once there, Two options will appear in the tab. The first one is for the city that you want to search and the second is for the number of breweries want.<br>
</p>  
<h3> 
  Example
</h3> 
<p>
  Put "Cincinnati" in the first box and "5" in the second (minus the "). Then click the button<br>
  the next page should show this:
</p>
<ul>
  <li>13 Below Brewery - micro - 7391 Forbes Rd</li>
  <li>Bad Tom Smith Brewing - micro - 4720 Eastern Ave</li>
  <li>Big Ash Brewing Company - planning - None</li>
  <li>Boston Beer Co - DBA Samuel Adams Brewing Co - regional - 1625 Central Pkwy</li>
  <li>Brink Brewing Company - micro - 5905 Hamilton Ave </li>
</ul>

<h2>
  Note
</h2>
</p>
  The list can only go in alphabetical order<br>
  
  The reason that there is a "Number" field is that there is no way to say "give them all" so if you want to see all of them, continually increase the number untill the error "The number is out of range" is thrown, then work backwards. 
</p>

<h2>
  Refrences
</h2>
<ul>
  <li>https://www.openbrewerydb.org/documentation. Open Brewery Database (API)</li>
  <li>https://stackoverflow.com/questions/70677136/how-to-print-list-in-python-flask-jinja2-html</li>
  <li>https://getbootstrap.com/. Bootstrp</li>
  <li>https://it3038c.github.io/IT3038C/modules/12</li>
</ul>

