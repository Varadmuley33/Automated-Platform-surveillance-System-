##############################################################
# Project Name  : Automated Platform Surveillance System
# Author        : Varad Muley
# Description   : This script monitors system resources like
#                 CPU, RAM, Disk and running processes.
#                 It creates log files periodically.
##############################################################

import schedule      # Used to schedule tasks at regular intervals
import psutil        # Used to fetch system information
import time          # Used for time-related functions
import sys           # Used to handle command line arguments
import os            # Used for file and directory operations

# Global constant for formatting output
Border = "-" * 75


##############################################################
# Function Name : CreateLog
# Description   : Creates a log file and stores system info
# Input         : FolderName (Directory where logs will be saved)
# Output        : None
##############################################################
def CreateLog(FolderName):

    # Step 1: Check whether directory exists or not
    if os.path.exists(FolderName):

        # If exists but not a directory → error
        if not os.path.isdir(FolderName):
            print("Unable to create folder")
            return

    else:
        # If directory does not exist → create it
        os.mkdir(FolderName)
        print("Directory created successfully")

    # Step 2: Generate timestamp for unique log file
    # Format: Year_Month_Day_Hour_Min_Second
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")

    # Step 3: Create full file path
    FileName = os.path.join(FolderName, f"Marvellous_{timestamp}.log")
    print("Log file created:", FileName)

    # Step 4: Open file using 'with' (auto closes file)
    with open(FileName, "w") as fobj:

        # Write header in log file
        fobj.write(Border + "\n")
        fobj.write("----- Marvellous Platform Surveillance System -----\n")
        fobj.write("Log Created at : " + time.ctime() + "\n")
        fobj.write(Border + "\n")

        ##################################################
        # CPU INFORMATION
        ##################################################
        fobj.write("\n---------------- CPU Information ----------------\n")

        # Get CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        fobj.write(f"CPU Usage (%) : {cpu_usage}\n")

        ##################################################
        # RAM (MEMORY) INFORMATION
        ##################################################
        fobj.write("\n---------------- RAM Information ----------------\n")

        # Fetch virtual memory details
        mem = psutil.virtual_memory()

        # Convert bytes into GB for readability
        fobj.write(f"Total Memory     : {mem.total / (1024**3):.2f} GB\n")
        fobj.write(f"Available Memory : {mem.available / (1024**3):.2f} GB\n")
        fobj.write(f"Used Memory      : {mem.used / (1024**3):.2f} GB\n")
        fobj.write(f"Memory Usage (%) : {mem.percent}%\n")

        ##################################################
        # DISK INFORMATION
        ##################################################
        fobj.write("\n---------------- Disk Information ----------------\n")

        # Get disk usage of root directory
        disk = psutil.disk_usage('/')

        fobj.write(f"Total Disk Space : {disk.total / (1024**3):.2f} GB\n")
        fobj.write(f"Used Disk Space  : {disk.used / (1024**3):.2f} GB\n")
        fobj.write(f"Free Disk Space  : {disk.free / (1024**3):.2f} GB\n")
        fobj.write(f"Disk Usage (%)   : {disk.percent}%\n")

        ##################################################
        # PROCESS INFORMATION
        ##################################################
        fobj.write("\n---------------- Running Processes ----------------\n")
        fobj.write("PID\tProcess Name\tMemory Usage (MB)\n")

        # Iterate through all running processes
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                pid = proc.info['pid']                     # Process ID
                name = proc.info['name']                   # Process Name
                mem_usage = proc.info['memory_info'].rss   # Memory usage in bytes

                # Convert bytes to MB
                mem_usage = mem_usage / (1024 * 1024)

                # Write process info into file
                fobj.write(f"{pid}\t{name[:15]}\t{mem_usage:.2f} MB\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Skip processes that cannot be accessed
                continue

        ##################################################
        # FOOTER
        ##################################################
        fobj.write("\n" + Border + "\n")
        fobj.write("------------- End of Log File -------------\n")
        fobj.write(Border + "\n")


##############################################################
# Function Name : main
# Description   : Entry point of program
#                 Handles user input and scheduling
##############################################################
def main():

    # Display header
    print(Border)
    print("----- Marvellous Platform Surveillance System -----")
    print(Border)

    ##################################################
    # CASE 1 : Help / Usage
    ##################################################
    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("This script performs:")
            print("1. System monitoring (CPU, RAM, Disk)")
            print("2. Process tracking")
            print("3. Automatic log generation")

        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage:")
            print("python surveillance.py <TimeInterval> <DirectoryName>")
            print("TimeInterval : Time in minutes")
            print("Directory    : Folder to store logs")

        else:
            print("Invalid option. Use --h or --u")

    ##################################################
    # CASE 2 : Actual Execution
    ##################################################
    elif len(sys.argv) == 3:

        try:
            # Convert interval into integer
            interval = int(sys.argv[1])
            folder = sys.argv[2]

            print("Time Interval :", interval)
            print("Directory     :", folder)

            # Schedule CreateLog function periodically
            schedule.every(interval).minutes.do(CreateLog, folder)

            print("System started successfully...")
            print("Press Ctrl + C to stop")

            # Infinite loop to keep scheduler running
            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("Invalid time interval. Please enter integer value")

    ##################################################
    # INVALID INPUT
    ##################################################
    else:
        print("Invalid arguments. Use --h or --u")

    # Display footer
    print(Border)
    print("Thank you for using the script")
    print(Border)


# Entry point of program
if __name__ == "__main__":
    main()