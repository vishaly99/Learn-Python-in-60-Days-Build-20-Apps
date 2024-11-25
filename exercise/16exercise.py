import FreeSimpleGUI as sg

label1=sg.Text("Enter feet:=")
label2=sg.Text("Enter inches:=")

inputbox1=sg.Input()
inputbox2=sg.Input()

submitbutton=sg.Button("Convert")

window=sg.Window("Conertor",
                 layout=[[label1,inputbox1],
                        [label2,inputbox2],
                         [submitbutton]])
window.read()
window.close()