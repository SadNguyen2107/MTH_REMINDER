from datetime import datetime
import json
import os


def trial_generator():
    trial = 0
    while True:
        yield trial
        trial += 1


def retrieveData(data):
    trial_obj = trial_generator()
    while index := next(trial_obj):
        message_data = data[index].get("message", "Wait A Minute !!!")
        print(f"Trial {index}: {message_data}")
        if message_data is not None:
            return message_data

        elif index > 100:
            break


def getLastData(path_to_html):
    
    with open(path_to_html, "r") as old_output_file:
        return old_output_file.read()


# Write data into HTML file
def write_announcement_data_html(data_response: json):
    message_data = retrieveData(data_response)
   

    current_time = datetime.now()
    date_string = datetime.strftime(current_time, "%B %d, %Y: %H:%M:%S")

    path_to_html_file = "OutputData/announcementInfo.html"
    # If message_data then get the last data
    if message_data == None:
        message_data = getLastData(path_to_html_file)
    
    with open(path_to_html_file, "w") as announcement_file:
        announcement_file.write(f"Last Update: {date_string}\n")
        announcement_file.write(message_data)
        print(f"Successfully dump data in the file {path_to_html_file}")


def createDirectoryHTMLfile(data_response: json):
    # Make a directory named OutputData with all the file in there
    try:
        # Directory to put all the file in there
        directory = "OutputData"

        # Parent Directory path
        parent_dir = os.getcwd()

        # Path to the Folder
        path = os.path.join(parent_dir, directory)

        # Create a directory
        os.mkdir(path)
    except OSError:
        write_announcement_data_html(data_response)
    else:
        write_announcement_data_html(data_response)
