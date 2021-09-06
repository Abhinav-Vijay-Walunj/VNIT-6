# VNIT-6
				*******************
				*** OHLC Engine ***
				*******************

**INSTALLATION
---------------
This project is created solely using python 3.

Requirements :
+ Python 3 installed
+ Following python module installed :
    tkinter, json, plotly, pyEX 

To check which modules are installed, use command : 
"pip list"

Note : To install tkinter, use "pip install tk"

How to run :
run 'run_project.py' file using python interpreter.
1. Open command prompt/terminal in the directory containing project files in your local machine
2. run 'pyhton run_project.py' command 
3. Input company symbol and start, end data .
4. Click on search and graph will show in the browser window.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Please Enter company symbol in UPPERCASE.

Please Enter Data strictly in "YYYY-MM-DD" format.

Since we are using http calls, it may take a while(~10sec) to run .

** Functionality
-----------------
This app is preloaded with a dataset of 'Stock List' and it is based on an anlytical server.

INTPUT:JSON Format comprising of certain attributes.

OUTPUT:Report on timely basis in the form of charts.


** MODULE LIST
-------------
tkinter : for GUI

plotly : for plotting graph

json : for parsing json file

pyEX : to get data via IEX Cloud API

** DESIGN
-----------
UI designing is done in most rudimentory way. 

All the graphical elements were arranged with grid layout in tkinter, by using row and column values and by using rowspan and colspan.


** METHODS
-----------
Front End Methods: 
+ dialog_message() :
print error message as dialog box.

+ search_action() :
Get data from parser, and plot the graph when user press search button.

+ set_history_text() :
Shows user search history in History Text Box.

+ select_ohlc() :
Set Graph type as ohlc.

+ select_candlestrick() :
Set Graph type as candlestrick.

Back End Methods:

Module parser :
+ info() :
return information about a specific company.

+ FSM() :
search in data dictionary and return required data for graph.
Parameter : company symbol, start date, end date.
Return : dictionary containing 5 lists for stock price and corresponding dates
and a string error_message.

Module reader :
+ input_reader() :
convert json file to python dictionary, using json package.



**DATA STRUCTURES
------------------
+ Dynamic Array (python list) :
for saving user command history.

+ Hash Table(python dictionary) :
To parse data file, and to get graph data from parsed object.

**ANALYSIS
-----------
       + 
