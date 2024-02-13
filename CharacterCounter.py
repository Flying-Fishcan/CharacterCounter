import PySimpleGUI as sg
import pyperclip

sg.theme('SystemDefault1')

layout = [
    [sg.Multiline(key='notepad', enable_events=True, default_text="", pad=((0,0),(0,0)))],
    [sg.Button('Copy'), sg.Button('Paste'), sg.Button('Save'),  sg.Button('Load'), sg.Text('Characters: 0', size=(40,1), key='count')]
    ]

window = sg.Window('CharacterCounter', layout, margins=(0,0), resizable=True, finalize=True) #ウィンドウサイズを可変にする
window['notepad'].expand(expand_x=True, expand_y=True) #テキストボックスの大きさを可変にする

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED: #xボタンを押すとプログラムを終了する
        break

    if event == 'Copy':
        copy_text = values['notepad']
        pyperclip.copy(copy_text) #メモ帳のデータをクリップボードにコピー

    if event == 'Paste':
        paste_text = pyperclip.paste()
        window['notepad'].print(paste_text)

    if event == 'Save':
        directory = sg.popup_get_folder('Select folder') #フォルダーを選択
        file_name = sg.popup_get_text('Enter file name') #ファイル名を入力
        if directory or file_name == None:
            break
        else:
            file_path = directory + '/' + file_name + '.txt' #ディレクトリとファイル名を結合
            with open(file_path, 'w') as f:
                f.write(values['notepad']) #メモ帳のデータをtxtファイルに出力

    if event == 'Load':
        load_file = sg.popup_get_file('Select file', file_types=(('Text Files', '.txt'),)) #ファイルを選択
        if load_file == None:
            break
        else:
            with open(load_file, 'r') as f:
                load_data = f.read()
                window['notepad'].update('') #メモ帳のデータをリセット
                window['notepad'].print(load_data) #txtファイルのデータをメモ帳に出力

    if event == 'notepad':
        window['count'].update(f'Characters: {len(values['notepad'])}') #入力の度に文字数を更新する

window.close()