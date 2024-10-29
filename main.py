import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# TODO:
# Add two buttons to change position of sections ▲▼
# add a number indicating position of said section as a label
# the padding is kinda bad tbh 
class SectionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x540")
        self.root.title("GCODE generator")

        # Dictionary to store sections by ID and a list to maintain visual order
        self.entries = {}
        self.sections = {}
        self.section_order = []
        self.section_id_counter = 0  

        # Main Frame with scrollbar
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.root.bind("<MouseWheel>", self.on_mouse_wheel)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Button to add sections
        self.add_button = tk.Button(root, text="Add Section", command=self.add_section)
        self.add_button.pack(anchor="se", padx=10, pady=10)

        # Button to generate the gcode
        self.add_button = tk.Button(root, text="Generate GCODE", command=self.generate_gcode, bg='darkred')
        self.add_button.pack(side=tk.TOP,anchor="ne", padx=10, pady=10)

        # Button to generate the gcode
        self.add_button = tk.Button(root, text="Add Range", command=lambda:print("Not currently working"), bg='lightgrey')
        self.add_button.pack(side=tk.TOP,anchor="ne", padx=10, pady=10)

        # Adding a template Section to copy from

        template_frame = tk.Frame(self.scrollable_frame, borderwidth=1.5, relief="solid", padx=15, pady=15, bg="darkgrey")

        label0 = tk.Label(template_frame, text="Template:")
        label0.grid(row=0, column=0, padx=5, pady=5)
        label1 = tk.Label(template_frame, text="Position:")
        label1.grid(row=0, column=1, padx=5, pady=5)
        self.entry1 = tk.Entry(template_frame)
        self.entry1.grid(row=0, column=2, padx=5, pady=5)
 

        label2 = tk.Label(template_frame, text="Speed:")
        label2.grid(row=0, column=3, padx=5, pady=5)
        self.entry2 = tk.Entry(template_frame)
        self.entry2.grid(row=0, column=4, padx=5, pady=5)

        # Range functionallity frame
        range_frame = tk.Frame(self.scrollable_frame, borderwidth=1.5, relief="solid", padx=15, pady=15, bg="darkgrey")
        label3 = tk.Label(range_frame, text="Pos range:")
        label3.grid(row=0, column=5, padx=5, pady=5)
        self.entry3 = tk.Entry(range_frame)
        self.entry3.grid(row=0, column=6, padx=5, pady=5)

        self.entry4 = tk.Entry(range_frame)
        self.entry4.grid(row=0, column=7, padx=5, pady=5)

        label4 = tk.Label(range_frame, text="Speed range:")
        label4.grid(row=0, column=8, padx=5, pady=5)
        self.entry5 = tk.Entry(range_frame)
        self.entry5.grid(row=0, column=9, padx=5, pady=5)

        self.entry6 = tk.Entry(range_frame)
        self.entry6.grid(row=0, column=10, padx=5, pady=5)

        label5 = tk.Label(range_frame, text="Iterations:")
        label5.grid(row=0, column=11, padx=5, pady=5)
        self.entry7 = tk.Entry(range_frame)
        self.entry7.grid(row=0, column=12, padx=5, pady=5)


        range_frame.pack(fill="none", pady=5)
        template_frame.pack(fill="none", pady=5)

    def on_mouse_wheel(self, event):
        """Scroll the canvas with the mouse wheel."""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    def add_section(self):
        # Generate a unique ID for the new section
        section_id = self.section_id_counter
        self.section_id_counter += 1

        # Create a new section frame
        section_frame = tk.Frame(self.scrollable_frame, borderwidth=1, relief="solid", padx=10, pady=5)
        
        # Label and Entry fields for the section
        label1 = tk.Label(section_frame, text="Position:")
        label1.grid(row=0, column=0, padx=5, pady=5)
        entry1 = tk.Entry(section_frame)
        entry1.grid(row=0, column=1, padx=5, pady=5)
        if(self.entry1.get()):
            entry1.insert(0,self.entry1.get())

        label2 = tk.Label(section_frame, text="Speed:")
        label2.grid(row=0, column=2, padx=5, pady=5)
        entry2 = tk.Entry(section_frame)
        entry2.grid(row=0, column=3, padx=5, pady=5)
        if(self.entry2.get()):
            entry2.insert(0,self.entry2.get())

        id_label = tk.Label(section_frame, text=f"id: {section_id}")
        id_label.grid(row=0, column=4, padx=5, pady=5)
        # Button to remove a section
        remove_button = tk.Button(section_frame, text="Remove", command=lambda: self.remove_section(section_id))
        remove_button.grid(row=0, column=5, padx=5, pady=5)

        self.entries[section_id] = (entry1,entry2)

        section_frame.pack(fill="x", pady=5)
        self.sections[section_id] = section_frame  
        self.section_order.append(section_id)      

    def remove_section(self, section_id):
        # Remove section by ID from dictionary and list, then destroy the frame
        if section_id in self.sections:
            self.sections[section_id].destroy()   
            del self.sections[section_id]         
            del self.entries[section_id]
            self.section_order.remove(section_id) 

    def generate_gcode(self):
        START_GCODE = "G1 X-190 F=10000\n$AN_SLTRACE=1\n"
        END_GCODE = "G90\nACC[X]=100\nG90\n$AN_SLTRACE=2\nRET"
        mid_code = ""
        for id,values in self.entries.items():
            # need checks to make sure they are numbers
            pos_entry = values[0].get().strip()  
            speed_entry = values[1].get().strip()  

            if not pos_entry or not speed_entry:  # Check if the input is empty
                # Show a warning message
                messagebox.showwarning(title= "Missing Input", message=f"You forgor at section number: {id} 💀")
                return
            try:
                int(values[0].get())
                int(values[1].get())
            except:
                messagebox.showwarning(title= "Invalid Input", message=f"Added an extra letter perhaps at: {id}")
            #  add auto conversion on distance from -300 to 300
            mid_code+= f"G1 X{clamp(int(values[0].get()),-300,300)} F={values[1].get()}\n"
        # print(all_entries)

        finalized_code = START_GCODE + mid_code + END_GCODE
        with open("output.txt", "w") as file:
            file.write(finalized_code)


def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 

if __name__ == "__main__":
    root = tk.Tk()
    app = SectionApp(root)
    root.mainloop()