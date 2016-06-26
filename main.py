import Tkinter
import ttk
import collections


# ListItem = collections.namedtuple(
#     'ListItem', ['id', 'order', 'status', 'title', 'description'])


todo_list = [
    ListItem(1, 2, 'Done', 'go shopping', 'get items at grocery store.'),
    ListItem(2, 3, 'In Progress', 'wash car', 'complete washing the car.'),
    ListItem(3, 1, 'Done', 'feed cat', 'feed the cat at 7:00 pm.')
]


# class ItemFrame(ttk.Frame):

#     def __init__(self, parent, item=None):
#         ttk.Frame.__init__(self, parent)

#         self.pack()


class ItemModel(object):

    def __init__(
            self, id=None, order=None, status=None, title='', description=''):
        self.id = Tkinter.IntVar()
        self.id.set(id)


class ListFrame(ttk.Frame):

    def __init__(self, parent, item_list=None):

        ttk.Frame.__init__(self, parent)
        self.pack()
        self.item_list = []
        if item_list:
            for item in item_list:
                self.add_item(item)

    def add_item(self, item):

        self._add_item(item)
        row = len(self.item_list) - 1
        ttk.Label(self, text=item.status).grid(row=row, column=0)
        ttk.Label(self, text=item.title).grid(row=row, column=1)
        ttk.Label(self, text=item.description).grid(row=row, column=2)
        # ttk.Label(self, text=item['status']).grid(row=row, column=0)
        # ttk.Label(self, text=item['title']).grid(row=row, column=1)
        # ttk.Label(self, text=item['description']).grid(row=row, column=2)

    def _add_item(self, item):

        self.item_list.append(item)


class ToDoListApp(ttk.Frame):

    def __init__(self, parent, item_list=None):

        ttk.Frame.__init__(self, parent)
        self.pack()
        self.list_frame = ListFrame(self, item_list)
        self.create_widgets()

    def create_widgets(self):

        self.list_frame.pack(side=Tkinter.TOP, fill=Tkinter.X)

        self.title_entry = Tkinter.StringVar()
        self.desc_entry = Tkinter.StringVar()

        entry_frame = ttk.Frame(self)
        title_frame = ttk.Frame(entry_frame)
        desc_frame = ttk.Frame(entry_frame)

        ttk.Label(title_frame, text='Title').pack(side=Tkinter.LEFT)
        ttk.Entry(title_frame, textvariable=self.title_entry).pack(side=Tkinter.LEFT)
        title_frame.grid(row=1, column=1)

        ttk.Label(desc_frame, text='description').pack(side=Tkinter.LEFT)
        ttk.Entry(desc_frame, textvariable=self.desc_entry).pack(side=Tkinter.LEFT)
        desc_frame.grid(row=1, column=2)

        ttk.Button(
            entry_frame, text='add',
            command=self.add_item).grid(row=1, column=3)

        entry_frame.pack(side=Tkinter.BOTTOM)

    def add_item(self):

        item = ListItem(
            '', '',
            'In Progress',
            self.title_entry.get(),
            self.desc_entry.get())

        self.list_frame.add_item(item)


if __name__ == '__main__':

    root = Tkinter.Tk()
    root.geometry('{x}x{y}+0+0'.format(x=450, y=1000))
    app = ToDoListApp(parent=root, item_list=todo_list)
    root.mainloop()
