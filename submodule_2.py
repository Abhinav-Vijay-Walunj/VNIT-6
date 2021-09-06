
# def check(data, Symbol, s_date, e_date):
import datetime


def FSM(data, Symbol, s_date, e_date):
    o = []
    c = []
    h = []
    l = []
    da = []
    d = {}
    # end_date = datetime.date(e_date)
    # print(end_date)
    for i in range(0,len(data)):
        if data[i]['symbol'] == Symbol:
            if data[i]['date'] >= s_date:
                while(data[i]['date']<=e_date):
                    o.append(data[i]['open'])
                    c.append(data[i]['close'])
                    h.append(data[i]['high'])
                    l.append(data[i]['low'])
                    da.append(data[i]['date'])
                    i+=1
                break
    d["open"] = o
    d["close"] = c
    d["high"] = h
    d["low"] = l
    d["date"] = da
    return d