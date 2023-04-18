import webbrowser
import os

def write_one_line(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    
    with open(file_path, 'w') as f:
        f.write('Hello Sad\n')
        f.write(data)

def deleteFirstLine(file_path):
    with open(file_path, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(file_path, 'w') as fout:
        fout.writelines(data[1:])

def openWebBrowser():
    path_to_html_file = os.path.abspath('OutputData copy/announcementInfo_copy.html')  # Get the path of that html file

    write_one_line(path_to_html_file)
    
    announcementInfo_file = f'file://{path_to_html_file}'
    webbrowser.open(announcementInfo_file)
    
    deleteFirstLine(path_to_html_file)
    
if __name__ =='__main__':
    openWebBrowser()
    