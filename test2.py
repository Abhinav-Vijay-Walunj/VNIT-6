import tkinter as tk;
import tkinter.messagebox as tkmsg

import plotly.graph_objects as go 
import submodule_1
import submodule_2

data_file = "Stock List.json"

json_data = submodule_1.input_reader(data_file)

# constants
MAIN_X = 500
MAIN_Y = 300

main_widget = tk.Tk()

main_geometry = str(MAIN_X)+"x"+str(MAIN_Y)
main_widget.geometry(main_geometry) 

# input variables
comp_name_var=tk.StringVar()
st_date_var=tk.StringVar()
end_date_var=tk.StringVar()


def dialog_message() :
    tkmsg.showinfo("Attention", "Search Button Clicked")

def search_action() :
    comp_name = comp_name_var.get()
    st_date = st_date_var.get()
    end_date = end_date_var.get()

    print(comp_name, st_date, end_date) 

    #comp_name_var.set("")
    #st_date_var.set("")
    #end_date_var.set("")

    parsed_data = submodule_2.FSM(json_data, comp_name, st_date, end_date)

    data = go.Ohlc(x=parsed_data["date"],
                    open=parsed_data["open"],
                    high=parsed_data["high"],
                    low=parsed_data["low"],
                    close=parsed_data["close"]
                    )

    fig = go.Figure(data)

    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.show()



# UI elements

#define lable
comp_name_label = tk.Label(main_widget, text="Enter Company Name").grid(row=0, column=0)

#define text imput
comp_name_inp = tk.Entry(main_widget, textvariable = comp_name_var).grid(row=0, column=1)

#define lable
st_date_label = tk.Label(main_widget, text="Enter start date").grid(row=1, column=0)
st_date_inp = tk.Entry(main_widget, textvariable=st_date_var).grid(row=1, column=1)

#define lable
end_date_label = tk.Label(main_widget, text="Enter End date").grid(row=2, column=0)
end_date_inp = tk.Entry(main_widget, textvariable=end_date_var).grid(row=2, column=1)

#define Button
search_button = tk.Button(main_widget, text="Search", command=search_action).grid(row=3, column=0)


main_widget.mainloop()