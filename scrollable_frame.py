import Tkinter
import ttk
import ttkstyles


class ScrollableFrame(ttk.Frame):

    def __init__(self, parent, **kwargs):

        ttk.Frame.__init__(self, parent, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.y_scrollbar = ttk.Scrollbar(self)
        self.y_scrollbar.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)

        self.canvas = Tkinter.Canvas(
            self, bd=0, yscrollcommand=self.y_scrollbar.set,
            bg=ttk.Style().lookup(self['style'], 'background'))
        self.canvas.grid(
            row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.W+Tkinter.E)
        self.canvas.bind('<Configure>', self.on_canvas_change)

        self.list_frm = ttk.Frame(self.canvas, style=self['style'])
        self.list_frm_id = self.canvas.create_window(
            (2, 2), window=self.list_frm, anchor=Tkinter.N+Tkinter.W)
        self.list_frm.bind('<Configure>', self.on_list_change)

        self.y_scrollbar.configure(command=self.canvas.yview)

    def add(self, widget):

        widget.pack(in_=self.list_frm, fill=Tkinter.X, expand=1)

    def on_canvas_change(self, event):

        self.canvas.itemconfigure(self.list_frm_id, width=event.width - 2)

    def on_list_change(self, event):

        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


def main():

    root = Tkinter.Tk()
    root.geometry('{x}x{y}+0+0'.format(x=500, y=800))
    ttkstyles.load_styles()

    frm = ScrollableFrame(root, style='List.TFrame')
    frm.pack(fill=Tkinter.BOTH, expand=1)

    def add_frm():

        frm.add(ttk.Frame(root, height=20))

    button = ttk.Button(root, text='add', command=add_frm)
    button.pack()

    root.mainloop()

if __name__ == '__main__':

    main()
