def info():             # функция для вывода пользователю подсказки, что можно делать.
    print(
        '''Make choose:
        print notes
        add
        earliest
        latest
        longest
        shortest
        ''')

def add(notes: list):            # функция добавления текста в список заметки
    note = input('Enter your note:')
    note_lan = len(note)
    notes.append({'note': note, 'lan': note_lan})
    return notes


def earliest(notes: list):
    for note in notes:
        print(data['note'])


def

if __name__ == '__main__':
    info()
    source_notes = list()
    while True:
        user_input = input('>')
        if user_input == 'add':
            source_notes = add(source_notes)
        elif user_input == 'earliest':
            pass
        elif user_input == 'latest':
            pass
        elif user_input == 'longest':
            pass
        elif user_input == 'shortest':
            pass
        elif user_input == 'print notes':
            print(source_notes)
        elif user_input == 'exit':
            print('Thanks, buy!')
            break
        else:
            info()