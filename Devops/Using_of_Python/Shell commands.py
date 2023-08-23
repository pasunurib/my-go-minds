# Import the subprocess module
import subprocess

# Define a function to run shell commands
def run_command(command):
    # Run the command and capture the output
    output = subprocess.run(command, shell=True, capture_output=True)
    # Check if the command was successful
    if output.returncode == 0:
        # Print the standard output
        print(output.stdout.decode())
    else:
        # Print the standard error
        print(output.stderr.decode())

# Install Docker using apt-get
run_command("sudo apt-get update")
run_command("sudo apt-get install docker.io")

# Pull the hello-world image from Docker Hub
run_command("sudo docker pull hello-world")

# Run the hello-world container
run_command("sudo docker run hello-world")
