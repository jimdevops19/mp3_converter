from dir_monitor import DirMonitor
import constants

if __name__ == "__main__":
    d1 = DirMonitor(constants.CONTAINER_DIRECTORY)
    print("The MP3 converter starts...")
    d1.watch()