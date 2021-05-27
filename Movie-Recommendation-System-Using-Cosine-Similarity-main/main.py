#Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications
from tkinter import * 
from tkinter import ttk         #ttk is a module that is used to style the tkinter widgets

#importing our model
import recommendSystem as model


class recommendTextManager:
    def __init__(self, text):
        self.text = text



def textGet():
    widgetText = Text(fr, font='Arial 12 bold', cursor='arrow', bg='lightblue', height=19, width=60)
    hlink = recommendTextManager(widgetText)
    widgetText.tag_configure('tag-left', justify='left')
    textQuery = widgetCombo1.get()  # getting input from widgetCombo1 widget
    text = model.recommendGET(textQuery)
    if text is None:  # if recommendations not found
        text = "Recommendation not found!!\n"
        widgetText.insert(1.0, text, 'tag-center')
        widgetText.insert(END, '\nTry:\n\n Select from dropdown\n '
                                'check for spelling mistakes', 'tag-left')
    else:  
        #iterate over the dataframe if found to show the recommendations in the widget
        widgetText.delete(1.0, END)  # clearing previous entries
        for index, title, imdb_url in text.itertuples():  # iterate dataframe as tuples
            widgetText.insert(END, title)  # insert recommended movies in widget
            if index != 10:  # if not the last index, insert a new line after the previous entry
                widgetText.insert(END, '\n')
                widgetText.insert(END, '\n')
    widgetText.place(x=185, y=310)
# creating gui window(master window)
root = Tk()  
root.title("Movie Recommendation System by Adarsh")
root.geometry('900x700') 
bg = PhotoImage(file = "pT7r5aK6c.png")
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0) 
# creating a frame to place the widgets
fr = Frame(root, height=499, width=749, bg='').place(x=85, y=69)
label2 = Label( fr, image = bg)
label2.place(x = 0, y = 0) 
# creating widgets
l1 = Label(fr, font='Arial 13 bold', text='    choose any movie or tv show !', height=4, width=55,bg='lightblue')
data = model.get_movie_data()  # database movie names
widgetCombo1 = ttk.Combobox(fr, width=48, font=("Arial", 12), values=data)

b1 = Button(fr, text='Show Recommendations', font='Arial 13 bold ', bg='lightblue', width=35, command=textGet)

l1.place(x=190, y=150)
widgetCombo1.place(x=230, y=213, height=32)
b1.place(x=270, y=260)

# main loop
if __name__ == '__main__':
    #root. mainloop() is a method on the main window which we execute when we want to run our application. This method will loop forever,
    #  waiting for events from the user, until the user exits the program – either by closing the window,
    #  or by terminating the program with a keyboard interrupt in the console.
    root.mainloop()
