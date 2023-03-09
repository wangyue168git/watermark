__version__ = '1.0.0'


class Notes:
    def __init__(self):
        self.show = True

    def print_notes(self):
        if self.show:
            print(f'''
Welcome to use dca-watermark, version = {__version__}`
            ''')
            self.close()

    def close(self):
        self.show = False


bw_notes = Notes()
