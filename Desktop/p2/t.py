
# # n = 0
# # while n < 12:
# #     print("la valeur de n es " + str(n))
# #     n = n + 1
# #     mdp = input("entre ton mdpi")
# #     1
# aget = 0

# while aget == 0:
#     age = input("entre votre age")
    
#     try:
#         aget =  int(age) + 1
#     except:
#         print("la valeur n'est pas correct")

# print("vous avez " + str(age) + " ans")
# print("l'an prochain vous devez avoir " + str(aget))
import tkinter as tk

def click(event):
    global screen_var
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen_var.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Erreur")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculatrice")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=10, relief=tk.SUNKEN)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_texts = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

buttons = []
for i, text in enumerate(button_texts):
    button = tk.Button(root, text=text, font="Arial 20", relief=tk.RAISED, height=1, width=3)
    button.grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5)
    button.bind("<Button-1>", click)
    buttons.append(button)

root.mainloop()