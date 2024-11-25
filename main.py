import time
import sys
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_command(command, typing_speed=0.1):
    """Simulate typing each character with a delay."""
    for char in command:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()  # New line after command is typed

def fake_terminal(commands, typing_speed=0.1, output_speed=0.5):
    for command in commands:
        if len(command) > 0:
            # Simulate typing the command
            print("$ ", end="")
            type_command(command[0], typing_speed)
            
            # Simulate the output
            for output in command[1:]:
                time.sleep(output_speed)  # Delay between each output
                print(output)

            print()  # Blank line to separate commands for clarity

# Example input
commands = [
    ['ls', 'processing', 'done'],
    ['here', '1 minute remaining', 'success']
]

clear_screen()
time.sleep(3)
fake_terminal(commands)
