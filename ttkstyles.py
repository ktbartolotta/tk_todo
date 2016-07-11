import ttk


def load_styles():

    font_family = 'Segoe UI'

    list_title_font = (font_family, 15, 'bold')

    style = ttk.Style()

    style.configure('.', font=(font_family, 10))

# For KanBan app styles ----------------------------------------------

    style.configure(
        'ListsFrame.TPanedwindow',
        background='black')

    style.configure(
        'Staged.Title.TLabel',
        background='#700600',
        foreground='#ffccd6',
        font=list_title_font)

    style.configure(
        'Staged.ListContainerFrame.TFrame',
        background='#ff476a')

    style.configure(
        'Staged.Item.TFrame',
        background='#facfcd')

    style.configure(
        'Staged.Item.TLabel',
        background='#facfcd')

    style.configure(
        'InProgress.Title.TLabel',
        background='#00055c',
        foreground='#dbfeff',
        font=list_title_font)

    style.configure(
        'InProgress.ListContainerFrame.TFrame',
        background='#000df5')

    style.configure(
        'InProgress.Item.TFrame',
        background='#98daee')

    style.configure(
        'InProgress.Item.TLabel',
        background='#98daee')

    style.configure(
        'Complete.Title.TLabel',
        background='#053d00',
        foreground='#d1ffcc',
        font=list_title_font)

    style.configure(
        'Complete.ListContainerFrame.TFrame',
        background='#0bad00')

    style.configure(
        'Complete.Item.TFrame',
        background='#91d88a')

    style.configure(
        'Complete.Item.TLabel',
        background='#91d88a')

# ---------------------------------------------------


class ListTitle():

    def __init__(self, name='', style=''):

        self.name = name
        self.style = style


class ItemStyle():

    def __init__(
            self, frame='', frame_label='', frame_entry='',
            frame_button='', step=None):

        self.frame = frame
        self.frame_label = frame_label
        self.frame_entry = frame_entry
        self.frame_button = frame_button
        self.step = step


class StepStyle():

    def __init__(self, frame, checkbox, entry, button):

        self.frame = frame
        self.checkbox = checkbox
        self.entry = entry
        self.button = button
