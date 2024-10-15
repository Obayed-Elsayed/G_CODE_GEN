# from tkinter import *
# window = Tk()
# window.geometry('960x540')
# window.configure(bg = 'black')

# def drag(event):
#     # print(f'{event.y_root} {window.winfo_rootx()}')
#     print(f'{event.x} {event.y}')
#     updated_location = event.y - window.winfo_rooty()
#     new_y = (updated_location//50)+40
#     event.widget.place( y=new_y,anchor=CENTER)

# card = Canvas(window, width=500, height=40, bg='grey')
# card.grid(row=2,column=0,sticky=W, pady=2)
# # card.place(x=50, y=40,anchor=CENTER)
# # card.bind("<B1-Motion>", drag)

# another_card = Canvas(window, width=500, height=40, bg='grey')
# another_card.grid(row=1,column=0,sticky=W, pady=2)
# another_card.place(x=50, y=80,anchor=CENTER)
# another_card.bind("<B1-Motion>", drag)


# from tkinter import *
# from functools import partial

# def changeOrder(widget1,widget2,initial):
#     target=widget1.grid_info()
#     widget1.grid(row=initial['row'],column=initial['column'])
#     widget2.grid(row=target['row'],column=target['column'])

# def on_click(event):
#     widget=event.widget
#     print(widget) 
#     if isinstance(widget,Label):
#         start=(event.x,event.y)
#         grid_info=widget.grid_info()
#         widget.bind("<B1-Motion>",lambda event:drag_motion(event,widget,start))
#         widget.bind("<ButtonRelease-1>",lambda event:drag_release(event,widget,grid_info))
#     else:
#         root.unbind("<ButtonRelease-1>")

# def drag_motion(event,widget,start):
#     x = widget.winfo_x()+event.x-start[0]
#     y = widget.winfo_y()+event.y-start[1] 
#     widget.lift()
#     widget.place(x=x,y=y)

# def drag_release(event,widget,grid_info):
#     widget.lower()
#     x,y=root.winfo_pointerxy()
#     target_widget=root.winfo_containing(x,y)
#     if isinstance(target_widget,Label):
#         changeOrder(target_widget,widget,grid_info)
#     else:
#         widget.grid(row=grid_info['row'],column=grid_info['column'])

# root = Tk()

# myTextLabel1 = Label(root,text="Label 1",bg='yellow')
# myTextLabel1.grid(row=0,column=0,padx=5,pady=5,sticky=E+W+S+N)

# myTextLabel2 = Label(root,text="Label 2",bg='lawngreen')
# myTextLabel2.grid(row=1,column=0,padx=5,pady=5,sticky=E+W+S+N)

# myButton = Button(root,text="Change order",command=partial(changeOrder,myTextLabel1,myTextLabel2))
# myButton.grid(row=3,column=0,padx=5,pady=5,sticky=E+W+S+N)

# root.bind("<Button-1>",on_click)

# root.mainloop()

# window.mainloop()
# if __name__ == '__main__':
    # main()