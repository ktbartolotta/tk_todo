import Tkinter
import ttk
import ttkstyles
import scrollable_frame


# class EntryFrame(ttk.Frame):

#     def __init__(self, parent, **kwargs):

#         ttk.Frame.__init__(self, parent, **kwargs)

#         self.title_frm = ttk.Frame(self)
#         self.desc_frm = ttk.Frame(self)

#         ttk.Label(self.title_frm, text='Title').pack(side=Tkinter.LEFT)
#         ttk.Entry(self.title_frm).pack(side=Tkinter.LEFT)
#         self.title_frm.grid(row=1, column=1)

#         ttk.Label(self.desc_frm, text='Description').pack(side=Tkinter.LEFT)
#         ttk.Entry(self.desc_frm).pack(side=Tkinter.LEFT)
#         self.desc_frm.grid(row=1, column=2)

#         ttk.Button(
#             self, text='add').grid(row=1, column=3)


class ItemContainerFrame(ttk.Frame):

    def __init__(self, parent, **kwargs):

        ttk.Frame.__init__(self, parent, **kwargs)
        self.configure(padding=4)

        self.grid_columnconfigure(2, weight=1)

        ttk.Label(self, text='item').grid(row=1, column=1)
        title_entry = ttk.Entry(self)
        title_entry.grid(row=1, column=2, sticky=Tkinter.W+Tkinter.E)
        title_entry.bind('<Button-1>', self.toggle_ttk_state)

        self.expand_frm = ttk.Frame(self, padding=2, style=self['style'])
        self.expand_frm.grid_columnconfigure(2, weight=1)
        self.expand_frm.grid(
            row=2, column=1, columnspan=3, sticky=Tkinter.W+Tkinter.E)

        ttk.Label(self.expand_frm, text='steps').grid(row=1, column=1)
        self.steps_frm = ttk.Frame(self.expand_frm, style=self['style'])
        self.steps_frm.grid(row=1, column=2, sticky=Tkinter.W+Tkinter.E)

        self.add_step_frm = ttk.Frame(self.expand_frm, style=self['style'])
        self.add_step_button = ttk.Button(
            self.add_step_frm, text='+step', width=5, command=self.add_step)
        self.add_step_button.pack(side=Tkinter.LEFT)
        self.add_step_frm.grid(
            row=2, column=2, columnspan=3, sticky=Tkinter.W+Tkinter.E)

        self.expand_btn = ttk.Button(
            self, text='+', width=3, command=self.toggle_frame)
        self.expand_btn.grid(row=1, column=3)

        self.expand_frm.grid_remove()

    def toggle_ttk_state(self, event):

        return (event.widget.configure(state='disabled')
                if event.widget.cget('state') == 'enabled'
                else event.widget.configure(state='enabled'))

    def add_step(self):

        step_entry_frm = ttk.Frame(self.steps_frm)
        step_entry_frm.grid_columnconfigure(2, weight=1)
        ttk.Checkbutton(step_entry_frm).grid(row=1, column=1)
        step_entry = ttk.Entry(step_entry_frm)
        step_entry.grid(row=1, column=2, sticky=Tkinter.W+Tkinter.E)
        step_entry.bind('<Button-1>', self.toggle_ttk_state)
        step_entry_frm.pack(fill=Tkinter.X, expand=1)

    # def toggle_text_state(self, event):

    #     return (event.widget.configure(state=Tkinter.DISABLED)
    #             if event.widget.cget('state') == Tkinter.NORMAL
    #             else event.widget.configure(state=Tkinter.NORMAL))

    def toggle_frame(self):

        if self.expand_btn['text'] == '+':
            self.expand_btn.configure(text='-')
            self.expand_frm.grid()
        else:
            self.expand_btn.configure(text='+')
            self.expand_frm.grid_remove()


class ListFrame(ttk.Frame):

    def __init__(self, parent, **kwargs):

        ttk.Frame.__init__(self, parent, **kwargs)


# Test
class ItemText(Tkinter.Text):

    def __init__(self, parent, **kwargs):

        self.parent = parent
        Tkinter.Text.__init__(self, parent, **kwargs)


class ListContainerFrame(ttk.Frame):

    def __init__(
            self, parent, title=ttkstyles.ListTitle(),
            item_style='', **kwargs):

        ttk.Frame.__init__(self, parent, **kwargs)
        self.item_style = item_style

        ttk.Label(self, text=title.name, style=title.style).pack(
            fill=Tkinter.X)

        self.list_frm = scrollable_frame.ScrollableFrame(self, style=self['style'])
        self.list_frm.pack(fill=Tkinter.BOTH, expand=1)

        add_button_frm = ttk.Frame(self, style=self['style'])
        ttk.Button(
            add_button_frm, text='+item', width=5, command=self.add_item).pack(
                side=Tkinter.LEFT)
        add_button_frm.pack(fill=Tkinter.X)

    def add_item(self):

        self.list_frm.add(
            ItemContainerFrame(self.list_frm, style=self.item_style))


class ListsFrame(ttk.PanedWindow):

    def __init__(self, parent, **kwargs):

        ttk.PanedWindow.__init__(self, parent, **kwargs)
        self.add(
            ListContainerFrame(
                self,
                title=ttkstyles.ListTitle(
                    name='Staged', style='Staged.Title.TLabel'),
                item_style='Staged.Item.TFrame',
                style='Staged.ListContainerFrame.TFrame'),
            weight=1)
        self.add(
            ListContainerFrame(
                self,
                title=ttkstyles.ListTitle(
                    name='In Progress', style='InProgress.Title.TLabel'),
                item_style='InProgress.Item.TFrame',
                style='InProgress.ListContainerFrame.TFrame'),
            weight=1)
        self.add(
            ListContainerFrame(
                self,
                title=ttkstyles.ListTitle(
                    name='Complete', style='Complete.Title.TLabel'),
                item_style='Complete.Item.TFrame',
                style='Complete.ListContainerFrame.TFrame'),
            weight=1)


class ToDoListApp(ttk.Frame):

    def __init__(self, parent):

        ttk.Frame.__init__(self, parent)
        self.pack(fill=Tkinter.BOTH, expand=1)
        ListsFrame(
                self, orient=Tkinter.HORIZONTAL,
                style='ListsFrame.TPanedwindow').pack(
                    fill=Tkinter.BOTH, expand=1)


if __name__ == '__main__':

    root = Tkinter.Tk()
    ttkstyles.load_styles()
    root.geometry('{x}x{y}+0+0'.format(x=1000, y=1000))
    app = ToDoListApp(parent=root)
    root.mainloop()
