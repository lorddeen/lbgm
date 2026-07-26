# LBGM - Lindys Board Git Manager
## About
Management toolkit to manage your smallscale electronics project.

## Functionality
At this moment it manages folder structure.


## Dependencies
You need Python 3
At this moment you only need standard Python 3 packages. 

## Scripts

### lbgm
Simple script for CLI which generates folder structure

~~~python lbgm.py -np project_name~~~

gives you folder tree

project_name
    - hardware #kicad and stuff
    - firmware #firmware sourcecode for mcus
    - software #software for mpus and desktop apps. 
    - valids #automated test results
    - docs #documentation. schemes in pdf, markdown reports, manufacture notes
    - common #central hub for logs, project data etc. 
