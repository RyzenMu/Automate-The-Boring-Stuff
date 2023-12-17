import traceback
try:
    raise Exception ("An Exception is raised")
except:
    error_file = open("error_log", "a")
    error_file.write(traceback.format_exc())
    error_file.close()
    print("The trace back was written to error log file")