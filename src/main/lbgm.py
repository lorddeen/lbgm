import os # for file and directory management
from pathlib import Path
import shutil # for file and directory management
import subprocess # for git management
import argparse # for command-line argument parsing
import json # for config file handling

#basic structure of folders in project
directories = ["hardware", "software", "firmware", "docs", "valids", "common"]

# parser for CLI
def parse_arguments():
    parser = argparse.ArgumentParser(description="Utility to  manage monorepo hardware projects.")
    parser.add_argument("--mp", type=str, help="Name of the project directory to create.")
    parser.add_argument("--dp", type=str, help="Name of the project directory to delete.")
    parser.add_argument("--me", type=str, help="Name of the new entity to create.")
    parser.add_argument("--git", type=str, help="Command for git")
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
                if directory == "common":
                    with open(os.path.join(project_name, directory, "project_definitions.json"), "w") as file:
                        json.dump({" project_name": project_name}, file)

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
    def __init__(self):
        try:
            config_path = Path(__file__).resolve().parent.parent / "configs" / "entities.json"
            with open(config_path, "r") as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError as e:
            print(e)

    def make_entity(self, project_name, entity_name, entity_type):
        try:
            for directory in self.config[entity_type]:
                if directory:
                    if os.path.isdir(f"{project_name}/{directory}/{entity_name}"):
                        print(f"Entity {entity_name} in directory {directory} of project {project_name} already established.")
                    else:
                        os.makedirs(os.path.join(project_name, directory, entity_name))
                        print(f"Established entity {entity_name} in directory {directory} of project {project_name}")
        except Exception as e:
            print(f"Error ocured while creating entity {entity_name} in directory {directory}: {e}")

    def add_to_project_list(self, project_name, entity_name, entity_type):
        print(os.getcwd())
        with open("/common/project_definitions.json", "r") as file:
            project_definitions = json.load(file)
        if project_name not in project_definitions:
            project_definitions[project_name] = []
        project_definitions[project_name].append({entity_name: {"type": entity_type}})
        with open("common/project_definitions.json", "w") as file:
            file.write(json.dumps(project_definitions))


class Git_manager():

    def __init__(self):
        self.command = None


    def status(self):
        state=subprocess.run(["git","status"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return state

    def commit(self):
        try:
            message = input("Enter commit message: ")
            subprocess.run(["git", "add", "."], check=True)
            state = subprocess.run(["git", "commit", "-m", message], check=True)
            print("Changes committed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while committing changes: {e}")
            return e
        return state

    def push(self):
        try:
            state = subprocess.run(["git", "push"], check=True)
            print("Changes pushed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while pushing changes: {e}")
            return e
        return state

    def pull(self):
        try:
            state = subprocess.run(["git", "pull"], check=True)
            print("Changes pulled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while pulling changes: {e}")
            return e
        return state

    
    def command (command):
        match command:
            case "status":
                return self.status()
            case "commit":
                return self.commit()
            case "push":
                return self.push()
            case "pull":
                return self.pull()


        
        
if __name__ == "__main__":
    # change working directory to the parent directory and then to the test directory
  

    os.chdir("../../test")

    print("Current working directory:", os.getcwd())

    # parse command-line arguments
    args = parse_arguments()

    # create or delete project directory based on the provided arguments
    if args.mp:
        project_name = args.mp
        make_project_dir(project_name)
    if args.dp:
        project_name = args.dp
        delete_project_dir(project_name)

# creating entity based on the provided arguments
    if args.me:
        entity = Entity()

        if not args.mp:
            project_name = input("Enter the name of existing project")

        entity_type = args.me
        entity_name = input("Enter the name of the new entity: ")

        entity.make_entity(project_name, entity_name, entity_type)  # Replace with actual entity type if needed
        entity.add_to_project_list(project_name, entity_name, entity_type)

    if args.git:
        git=Git_manager()
        git.command = args.git
        if git.command == "status":
            state = git.status()
            print(state)





 