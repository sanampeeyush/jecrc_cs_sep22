import tkinter as ttk
import pandas as pd
model = pd.read_pickle('housePrice.pickle')

app = ttk.Tk()
app.configure(background='white')
app.geometry('300x300')
app.title('House Price Predictor')

income = ttk.Variable(app)
ttk.Label(app, text='Income',padx=15,pady=15, background='white').grid(row=0,column=0)
ttk.Entry(app, textvariable=income, width=10).grid(row=0, column=1)

house_age = ttk.Variable(app)
ttk.Label(app, text='House Age',padx=15,pady=15, background='white').grid(row=1,column=0)
ttk.Entry(app, textvariable=house_age, width=10).grid(row=1, column=1)

num_rooms = ttk.Variable(app)
ttk.Label(app, text='Number of Rooms',padx=15,pady=15, background='white').grid(row=2,column=0)
ttk.Entry(app, textvariable=num_rooms, width=10).grid(row=2, column=1)

population = ttk.Variable(app)
ttk.Label(app, text='Population',padx=15,pady=15, background='white').grid(row=3,column=0)
ttk.Entry(app, textvariable=population, width=10).grid(row=3, column=1)

def prediction():
    global model
    query_data = {
        'Avg. Area Income':[eval(income.get())], 
        'Avg. Area House Age':[eval(house_age.get())], 
        'Avg. Area Number of Rooms':[eval(num_rooms.get())], 
        'Area Population':[eval(population.get())]
    }
    price = model.predict(pd.DataFrame(query_data))
    result.set(round(price[0],2))

ttk.Button(app, text='Predict', command=prediction,font=('Arial',20)).grid(row=4,column=0,columnspan=2)

result = ttk.Variable(app)
result.set('0')
ttk.Label(app, textvariable=result, pady=15, font=('Arial',20), background='white').grid(row=5,column=0,columnspan=2)

app.mainloop()


#
# Use on CMD (exe/pkg)
#       python -m pip install pyinstaller
#
#       pyinstaller --onefile -w day22_gui_house_price_startup_profit.py
#
