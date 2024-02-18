import subprocess
import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
#    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    command = sys.argv[3]
    args = sys.argv[4:]
    
    completed_process = subprocess.Popen(
        [command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = completed_process.communicate()
    if stdout:
        print(stdout.decode("utf-8"), end="")
    if stderr:
        print(stderr.decode("utf-8"), file=sys.stderr, end="")

if __name__ == "__main__":
    main()
