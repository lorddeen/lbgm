import os
import shutil
import subprocess
import argparse

#basic structure of folders in project
directories = ["hardware", "software", "firmware", "docs", "valids", "common"]

# parser for CLI
def parse_arguments():
    parser = argparse.ArgumentParser(description="Utility to  manage monorepo hardware projects.")
    parser.add_argument("--mp", type=str, help="Name of the project directory to create.")
    parser.add_argument("--dp", type=str, help="Name of the project directory to delete.")
    parser.add_argument("--ne", type=str, help="Name of the new entity to create.")
    args = parser.parse_args()
    return args

def make_project_dir(project_name):
    
    try:
        if os.path.isdir(project_name):
            print("Directory"+{project_name}+"already exists")
        os.makedirs(project_name, exist_ok=True)
        print(f"Project directory '{project_name}' created successfully.")

    except Exception as e:
        print(f"Error 1 occurred while creating project directory: {e}")

    try:
        for directory in directories:
            if os.path.isdir(f"{project_name}/{directory}"):
                print(f"Directory {directory} already exists.")
            else:
                os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    except Exception as e:
        print(f"Error 2 occurred while creating project directory: {e}")
        pass

def delete_project_dir(project_name):
    try:
        if os.path.isdir(project_name):
            response = input(f"Are you sure you want to delete the project directory '{project_name}'? This action cannot be undone. (y/n): ")
            if response.lower() == 'y':
                shutil.rmtree(project_name, ignore_errors=True)
                print(f"Project directory '{project_name}' deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Project directory '{project_name}' does not exist.")
    except Exception as e:
        print(f"Error occurred while deleting project directory: {e}")


class Entity():
    def __init__(self, entity_name, entity_type):
        self.name = entity_name
        self.type = entity_type

    def make_pcb():
        pass

    def make_cable():
        pass

    def make_mech():
        pass

    def make_sw():
        pass




if __name__ == "__main__":
    # change working directory to the parent directory and then to the test directory
    os.chdir("..")
    os.chdir("test")
    print("Current working directory:", os.getcwd())

    # parse command-line arguments
    args = parse_arguments()

    # create or delete project directory based on the provided arguments
    if args.mp:
        make_project_dir(args.mp)
    if args.dp:
        delete_project_dir(args.dp)
    if args.ne:
        entity_name = args.ne
        entity_type = input("Enter the type of entity (pcb, cable, mech, sw): ")
        entity = Entity(entity_name, entity_type)
        print(f"Entity '{entity.name}' of type '{entity.type}' created.")




 