from win32_setctime import setctime
# importing datetime module
import datetime
import time
import PySimpleGUI as sg

layout = [
    [sg.Image('linux.png', size=(300,300))],
    [sg.Button("OK")]
]
window = sg.Window("Demo",layout)
while True:
    event, values = window.read()
# file_list_column = [
#     [
#         sg.Text("Image Folder"),
#         sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
#         sg.FolderBrowse(),
#     ],
#     [
#         sg.Listbox(
#             values=[], enable_events=True, size=(40,20),
#             key="-FILE LIST-"
#         )
#     ],
# ]
# window = sg.Window("Image Viewer")
# event, values = sg.Window('Choose an option', [[sg.Text('Select one->'), sg.Listbox(['Option a', 'Option b', 'Option c'], size=(20, 3), key='LB')],
#     [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

# if event == 'Ok':
#     sg.popup(f'You chose {values["LB"][0]}')
# else:
#     sg.popup_cancel('User aborted')
# assigned regular string date
date_time = datetime.datetime(2021, 7, 26, 21, 20, 40)
 
# print regular python date&time
print("date_time =>",date_time)

unix_time = time.mktime(date_time.timetuple())
setctime("test.ahk", unix_time)