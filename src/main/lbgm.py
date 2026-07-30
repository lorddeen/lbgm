import os
import subprocess
from project_manager import ProjectManager, Git_manager, Entity
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Utility to  manage monorepo hardware projects.")
    parser.add_argument("--mp", type=str, help="Name of the project directory to create.")
    parser.add_argument("--dp", type=str, help="Name of the project directory to delete.")
    parser.add_argument("--me", type=str, help="Name of the new entity to create.")
    parser.add_argument("--git", type=str, help="Command for git")
    args = parser.parse_args()
    return args
        
if __name__ == "__main__":
    # change working directory to the parent directory and then to the test directory
  

    os.chdir("../../test")

    print("Current working directory:", os.getcwd())

    # parse command-line arguments
    args = parse_arguments()

    # create or delete project directory based on the provided arguments
    if args.mp:
        project_name = args.mp
        ProjectManager.make_project_dir(project_name)
    if args.dp:
        project_name = args.dp
        ProjectManager.delete_project_dir(project_name)

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
        if git.command == args.git:
            state = git.commander("status")
            print(state)





 