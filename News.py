import subprocess

with open("daily_prompt.txt", "r") as file:  # "r" mode opens the file for reading
    prompt = file.read()  # Reads the entire file

process = subprocess.Popen(["zsh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Send multiple commands
commands = "ollama run deepseek-r1:7b\n && " + prompt + "\n"
stdout, stderr = process.communicate(commands)

print("Output:\n", stdout)
print("Error:\n", stderr)

# Opening the console and prompt Deepseek
# process = subprocess.Popen(["ollama run deepseek-r1:7b\n", prompt + "\n"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Getting the output and error (if any)
#. stdout, stderr = process.communicate()

print(stdout)
print("Done!")