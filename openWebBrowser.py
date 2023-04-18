import webbrowser
import os

def deleteFirstLine(file_path):
    with open(file_path, 'r') as fin:
        data = fin.read().splitlines(True)
        print(data)
        print(len(data))
        
    with open(file_path, 'w') as fout:
        fout.writelines(data[1:])

def openWebBrowser(blank: bool):
    path_to_html_file = os.path.abspath('OutputData/announcementInfo.html')  # Get the path of that html file

    announcementInfo_file = f'file://{path_to_html_file}'
    webbrowser.open(announcementInfo_file)
    
    if not blank:
        deleteFirstLine(path_to_html_file)
    
