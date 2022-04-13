import yfinance as yf
import pandas as pd
import datetime
import plotly.graph_objects as go

today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)

stocks = ("MSFT", "MVIS", "GOOG", "SPOT", "INO",
          "OCGN", "ABML", "RLLCF", "JNJ", "PSFE")

for stock in stocks:
    stockdata = yf.Ticker(stock)
    data = stockdata.history(start=yesterday, end=today, interval='1h')
    df = pd.DataFrame(data['Close'])
    Kichaum = {}
    TIMESTAMP = []
    CLOSEVALUE = []
    STOCKID = []

    for idx, row in df.iterrows():
        jsondata = {
            'stockid': str(stock),
            'timestamp': str(idx),
            'CloseValue': row['Close'],
            '52WeekHigh': stockdata.info["fiftyTwoWeekHigh"],
            '52WeekLow': stockdata.info["fiftyTwoWeekLow"]
        }
        
        TIMESTAMP.append(jsondata["timestamp"])
        CLOSEVALUE.append(jsondata["CloseValue"])
        
        STOCKID.append(jsondata["stockid"])
        Inidv_stocks=set(STOCKID)
        Inidv_stocks_list=list(Inidv_stocks)

        Kichaum['closEvalue'] = CLOSEVALUE
        Kichaum['timEstamp'] = TIMESTAMP
        Kichaum['stockId'] = STOCKID
        
    dff = pd.DataFrame(Kichaum, columns=['stockId', 'timEstamp', 'closEvalue'])
    print(dff)
        
    fig = go.Figure(go.Scatter(x=TIMESTAMP, y=CLOSEVALUE))
    fig.update_layout(title={'text': str(Inidv_stocks_list), 'y': 0.9,'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'})
    fig.show()
