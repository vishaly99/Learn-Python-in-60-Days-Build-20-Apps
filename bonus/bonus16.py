
import FreeSimpleGUI as sg


label1=sg.Text("Select the compression:=")
label2=sg.Text("Select the destination location:=")

selected_compression = sg.Input()
selected_destination = sg.Input()


add_button1=sg.FileBrowse("Select Location")
add_button2=sg.FolderBrowse("Select Destination")
compress=sg.Button("Compress")


window=sg.Window("File compressor",
                 layout=[[label1,selected_compression,add_button1],
                        [label2,selected_destination,add_button2],
                         [compress]])
window.read()
window.close()