import os # for file and directory management
from pathlib import Path
import shutil # for file and directory management
import subprocess # for git management
import argparse # for command-line argument parsing
import json
from unittest import case # for config file handling

#basic structure of folders in project
directories = ["hardware", "software", "firmware", "docs", "valids", "common"]



class ProjectManager:
    def __init__(self):
        pass

    def make_project_dir(self, project_name):
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
                print(self.config)
        except FileNotFoundError as e:
            print(e)

    def make_entity(self, project_name, entity_name, entity_type):
            for directory in self.config[entity_type]:
                try:
                    if directory:
                        if os.path.isdir(f"{project_name}/{directory}/{entity_name}"):
                            print(f"Entity {entity_name} in directory {directory} of project {project_name} already established.")
                        else:
                            os.makedirs(os.path.join(project_name, directory, entity_name))
                            print(f"Established entity {entity_name} in directory {directory} of project {project_name}")
                except Exception as e:
                    print(f"Error occurred while creating entity {entity_name} in directory {directory}: {e}")

    def add_to_project_list(self, project_name, entity_name, entity_type):
        try:
            print(Path.cwd())
            path = Path.cwd() / project_name / "common" / "project_definitions.json"
            print(path)
            with open(path, "r") as file:
                project_definitions = json.load(file)
            if entity_name not in project_definitions:
                project_definitions[entity_name] = []
            project_definitions[entity_name].append({"type": entity_type})
            with open(path, "w") as file:
                file.write(json.dumps(project_definitions))
        except Exception as e:
            print(f"Error occurred while adding entity {entity_name} to project definitions: {e}")

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

    def init(self):
        try:
            state = subprocess.run(["git", "init"], check=True)
            print("Git repository initialized successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while initializing git repository: {e}")
            return e
        return state

    
    def commander (command):
        match command:
            case "status":
                return self.status()
            case "commit":
                return self.commit()
            case "push":
                return self.push()
            case "pull":
                return self.pull()
            case "init":
                return self.init()
            case _:
                print("Invalid command. Please use 'status', 'commit', 'push', or 'pull'.")
