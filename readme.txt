
This project is created solely using python 3.

-------------------------------------------------------------
Modules Used : 
tkinter : for GUI
plotly : for plotting graph
json : for parsing json file
pyEX : to get data via IEX Cloud API

-------------------------------------------------------------
UI Designing & UI Methods:

UI designing is done in most rudimentory way. 
All the graphical elements were arranged with grid layout in tkinter,
by using row and column values and by using rowspan and colspan

For PushButtons and RadioButton, specific hadler methods are methods are written

dialog_message() :
print error message as dialog box

search_action() :
Get data from parser, and plot the graph when user press search button

set_history_text() :
Shows user search history in History Text Box

select_ohlc() :
Set Graph type as ohlc

select_candlestrick() :

Set Graph type as candlestrick
-------------------------------------------------------------
Data Structers :

Dynamic Array (python list) :
for saving user command history

Hash Table(python dictionary) :
To parse data file, and to get graph data from parsed object

-------------------------------------------------------------
Backend Methods :

Module parser :
info() :
return information about a specific company

FSM() :
search in data dictionary and return required data for graph.
Parameter : company symbol, start date, end date
return : dictionary containing 5 lists for stock price and corresponding dates
and a string error_message

Module reader :

input_reader() :
convert json file to python dictionary, using json package.



