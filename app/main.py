import subprocess
import sys
import tempfile
import shutil
import os

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
#    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    command = sys.argv[3]
    args = sys.argv[4:]
    
    directory_path = tempfile.mkdtemp()
    shutil.copy2(command, directory_path)
    os.chroot(directory_path)
    command = os.path.join("/", os.path.basename(command))

    
    completed_process = subprocess.Popen(
        [command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = completed_process.communicate()
    if stdout:
        sys.stdout.buffer.write(stdout)
        sys.stdout.buffer.flush()
    if stderr:
        sys.stderr.buffer.write(stderr)
        sys.stderr.buffer.flush()        

    sys.exit(completed_process.returncode)

if __name__ == "__main__":
    main()
