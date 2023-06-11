import tkinter as tk
import requests
import time  

# https://vm.tiktok.com/ZM2hup9Jd/
# https://www.weatherapi.com/docs/
# visualtk.com
API = "23d91b5c50c54673965195833233105"
url = "http://api.weatherapi.com/v1/"
window = tk.Tk()

photo = tk.PhotoImage(file="weather_icon.png")

window.geometry("720x1080")
window.title("Hello Boy")
window.config(background="Black")

photo = tk.PhotoImage(file="weather_icon.png")
def click():
  sc = int(score["text"])
  sc += 1
  score["text"] = f"{str(sc)}"

def clear():
  score["text"] = "0"
  #entry.delete(0, tk.END)
  #entry.delete(len(entry.get())-1, tk.END)
  entry.config(state=tk.DISABLED)

def get_weather():
  try:
    users = entry.get()
    user = "".join(users.split())
    url1 = f"{url}current.json?key={API}&q={user}"
    weather = requests.get(url1)
    #print(weather.json())
    temp = weather.json()["current"]["temp_c"]
    #print(int(temp), "c", label1["text"])
    label1["text"] = f"{int(temp)} C"
  except:
    My_Label["text"] = "Invaild Name"
    time.sleep(3)
    My_Label["text"] = "Hello World"
  
  



My_Label = tk.Label(window,
                    text="Hello World",
                    font=("Arial", 24,
"bold"),
                    fg="green",
                    bg="Black",)

My_Label.pack()

label1 = tk.Label(window,
                  text="",
                  font=("Arial", 24,
"bold"),
                    fg="green",
                    bg="Black",
                    )
label1.pack()

score = tk.Label(window,
                 text="0",
                 font=("Arial", 14),
                 fg="Green",
                 bg="Black")

score.place(x=0, y=0)

button = tk.Button(window,
                  text="Click Me",
                  command=get_weather,
                  font=("Comic Sans", 30),
                  fg="Green",
                  bg="#C0C0C0",

                  activeforeground="Green")

button.pack()

button1 = tk.Button(window,
                    command=clear,
                    text="Lock",
                    font=("Arial", 18),
                    fg="Green",
                    bg="#C0C0C0",
                    activeforeground="Green")
                    
button1.pack()

entry = tk.Entry(window,
                 font=("Arial", 20),
                 fg="Green",
                 bg="black",
                 show="$")
entry.pack()

window.mainloop()
