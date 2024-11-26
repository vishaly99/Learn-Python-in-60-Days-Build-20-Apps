from distutils.command.install import value

import FreeSimpleGUI as sg
from openpyxl.styles.builtins import output

#from gui import event, values

from zip_creator import make_archive

label1=sg.Text("Select the compression:=")
label2=sg.Text("Select the dest location:=")

selected_compression = sg.Input()
selected_destination = sg.Input()


add_button1=sg.FileBrowse("Select Location",key="files")
add_button2=sg.FolderBrowse("Select Destination",key="folder")
compress=sg.Button("Compress")

output_label=sg.Text(Key="output",text_color="green")

window=sg.Window("File compressor",
                 layout=[[label1,selected_compression,add_button1],
                        [label2,selected_destination,add_button2],
                         [compress,output_label]])
while True:
    event, values=window.read()
    print(event,values)
    filepaths=values["files"].split(";")
    folder=values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="Compression completed!")

window.close()