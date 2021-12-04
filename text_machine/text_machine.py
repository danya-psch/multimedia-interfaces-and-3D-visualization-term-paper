class TextMachine:

    iterator = None
    current_iterator = None

    splitted_text = None
    current_splitted_text = None


    current_word = None

    def __init__(self, text):
        self.text = text
        self.is_started = False
        self.is_Failed = False

        # Init splitting process
        self.process()

    def process(self):
        self.iterator = 0
        self.current_iterator = 0
        self.splitted_text = self.text.split()
        print(self.splitted_text)


    def process_new_text(self, new_text):
        self.rollback()
        self.splitted_text = new_text.split()

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iterator):
        self.iterator = iterator

    def get_current(self):
        return self.current_word

    def get_next(self):
        if self.current_iterator >= len(self.current_splitted_text):
            return None
        return self.current_splitted_text[self.current_iterator]

    def move(self):
        if self.current_iterator >= len(self.current_splitted_text):
            self.current_iterator = len(self.current_splitted_text) - 1
            return self.current_splitted_text[self.current_iterator]

        self.current_word = self.current_splitted_text[self.current_iterator]
        self.current_iterator = self.current_iterator + 1

        return self.current_word

    def start_transaction(self):
        self.current_splitted_text = self.splitted_text
        self.current_iterator = self.iterator

        self.is_started = True
        print('Transaction STARTED')

    def commit(self):
        self.is_started = False

        self.iterator = self.current_iterator
        self.splitted_text = self.current_splitted_text

        print('Transaction COMMITTED')

    def rollback(self):
        self.is_started = False

        self.current_splitted_text = None
        self.current_iterator = self.iterator

        print('Transaction FAILED: Rolled back')

    def has_finished(self):
        return not self.is_started
