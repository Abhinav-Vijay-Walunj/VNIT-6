import tkinter as tk;
import tkinter.messagebox as tkmsg

import plotly.graph_objects as go 
import reader
import data_parser

"""
Description part
Type of graph, spikes, cylinder, candlestick

code better

"""
# constant and global variables
data_file = "./Stock List.json"
MAIN_X = 700 
MAIN_Y = 400

# load json file
json_data = reader.input_reader(data_file)

#init main tkinter widget
main_widget = tk.Tk()

# input variables  - can be done only after intializing main_widget
comp_name_var=tk.StringVar()
st_date_var=tk.StringVar()
end_date_var=tk.StringVar()
graph_type = "ohlc"

#input history
inp_history = []
#history text feild
#history_text = tk.Text() # it is initialized later


# function handler for buttons
def dialog_message(msg : str) :
    tkmsg.showinfo("Error", msg)

def search_action() :

    #get input
    comp_name = comp_name_var.get()
    st_date = st_date_var.get()
    end_date = end_date_var.get()

    #add it to history
    inp_history.append(comp_name+" "+st_date+" "+end_date)

    #set input text box blank
    # comp_name_var.set("")
    # st_date_var.set("")
    # end_date_var.set("")
    #print(graph_type)
    # get parsed_data
    parsed_data = data_parser.FSM(json_data, comp_name, st_date, end_date)

    # check for errors
    if parsed_data["error_message"] != "" :
        dialog_message(parsed_data["error_message"])
        return
    elif len(parsed_data["open"]) == 0 :
        dialog_message("No data Found : unknown error")
        return

    comp_ext_data = data_parser.info(comp_name)

    # get description data
    comp_full_name = comp_ext_data["companyName"]


    # make plotting data
    data = None
    if graph_type == "ohlc" :
        data = go.Ohlc(x=parsed_data["date"],
                    open=parsed_data["open"],
                    high=parsed_data["high"],
                    low=parsed_data["low"],
                    close=parsed_data["close"]
                    )
    else :
        data = go.Candlestick(x=parsed_data["date"],
                    open=parsed_data["open"],
                    high=parsed_data["high"],
                    low=parsed_data["low"],
                    close=parsed_data["close"]
                    )

    # draw graph
    fig = go.Figure(data)
    fig.update( 
        layout_xaxis_rangeslider_visible=False
        )
    fig.update_layout(
        title=comp_full_name + " Stock Price Graph",  #+ "Company Type : " + comp_type + "<br>" + comp_desc,
        yaxis_title= comp_name + " Stock",
    )
    fig.show()

def set_history_text():
    history_text_str = "" 
    for i in inp_history :
        history_text_str += i + "\n"
    
    history_text.delete('1.0', tk.END)
    history_text.insert(tk.END, history_text_str)
    pass

def select_ohlc() :
    global graph_type
    graph_type = "ohlc"

def select_candlestrick() :
    global graph_type
    graph_type = "candlestick"


# resize main_wodget
main_geometry = str(MAIN_X)+"x"+str(MAIN_Y)
main_widget.geometry(main_geometry) 

# generating UI elements
comp_name_label = tk.Label(main_widget, text="Enter Company Symbol").grid(row=0, column=0)
comp_name_inp = tk.Entry(main_widget, textvariable = comp_name_var).grid(row=0, column=1, columnspan=2)
st_date_label = tk.Label(main_widget, text="Enter start date").grid(row=1, column=0)
st_date_inp = tk.Entry(main_widget, textvariable=st_date_var).grid(row=1, column=1, columnspan=2)
end_date_label = tk.Label(main_widget, text="Enter End date").grid(row=2, column=0)
end_date_inp = tk.Entry(main_widget, textvariable=end_date_var).grid(row=2, column=1, columnspan=2)

history_text = tk.Text(main_widget, height=5, width=30)
history_text.grid(row=0, column=3, rowspan=4, columnspan=4) 

graph_type_label = tk.Label(main_widget, text="Graph Type").grid(row=3, column=0)
candlestick_button = tk.Radiobutton(main_widget, text="Candlestick", variable=graph_type, value="candlestick", command=select_candlestrick)
candlestick_button.grid(row=3, column=1)
ohlc_button = tk.Radiobutton(main_widget, text="OHLC", variable=graph_type, value="ohlc", command=select_ohlc)
ohlc_button.grid(row=3, column=2)

# search Button
search_button = tk.Button(main_widget, text="Search", command=search_action).grid(row=5, column=0)
# see history button
see_history_button = tk.Button(main_widget, text="See Search history", command=set_history_text).grid(row=5, column=4)


# show the main widget
main_widget.mainloop()
