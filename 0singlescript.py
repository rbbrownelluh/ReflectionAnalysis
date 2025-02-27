import subprocess
import os

def run_script(script_name):
    """Helper function to execute a Python script."""
    try:
        subprocess.run(["python3", script_name], check=True)  # Use 'python3' explicitly
        print(f"Successfully executed {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")
    except FileNotFoundError as e:
        print(f"Command not found: {e}")

def main():
    # List of scripts to run in order
    scripts = [
        "1anonymize.py",
        "2combinehtml.py",
        "3htmlheadings.py",
        "4singlefile.py"
    ]

    # Get the current working directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Execute each script in sequence
    for script in scripts:
        script_path = os.path.join(current_directory, script)
        if os.path.exists(script_path):
            print(f"Running {script}...")
            run_script(script_path)
        else:
            print(f"Script not found: {script}")

    print("All scripts executed successfully.")

if __name__ == "__main__":
    main()