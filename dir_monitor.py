import os
import time
import mp3_conv


class DirMonitor:
    def __init__(self, dir_path, ext=".mp4"):
        self.dir_path = dir_path
        self.ext = ext


    def list_files(self) -> list:
        files = []
        for file in os.listdir(self.dir_path):
            full_file_path = os.path.join(self.dir_path, file)
            file, extension = os.path.splitext(full_file_path)
            if extension == self.ext:
                files.append(full_file_path)

        return files

    def watch(self):
        files_status = self.list_files()
        while True:
            time.sleep(5)
            current_files_status = self.list_files()
            new_files = list(set(current_files_status) - set(files_status))

            # Will be the logic to convert the new files:
            for new_file in new_files:
                mp3_conv.convert(new_file)

            files_status = current_files_status