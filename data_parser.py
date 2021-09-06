import pyEX as p

def info(Symbol):
    c = p.Client(api_token='pk_5a5f5dcb73c94f4a9f190e83ca334106', version='stable')

    sym = Symbol
    d = c.quote(symbol = sym)
    return d

def FSM(data, Symbol, s_date, e_date):
    o = []
    c = []
    h = []
    l = []
    da = []
    d = {"error_message" : ""}
    flag = 0
    for i in range(0,len(data)):
        if data[i]['symbol'] == Symbol:
            flag = 1
            if data[i]['date'] >= s_date:
                while(data[i]['date']<=e_date):
                    o.append(data[i]['open'])
                    c.append(data[i]['close'])
                    h.append(data[i]['high'])
                    l.append(data[i]['low'])
                    da.append(data[i]['date'])
                    i+=1
                break
    
    if (flag==0):
        d["error_message"] = "Please enter valid symbol"
    elif(len(o) == 0):
        d["error_message"] = "Data is not available in that period"
    else:
        d["open"] = o
        d["close"] = c
        d["high"] = h
        d["low"] = l
        d["date"] = da
    return d