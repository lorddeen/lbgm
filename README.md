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

```
python lbgm.py -np project_name
```

gives you folder tree

project_name
* hardware #kicad and stuff
* firmware #firmware sourcecode for mcus
* software #software for mpus and desktop apps. 
* valids #automated test results
* docs #documentation. schemes in pdf, markdown reports, manufacture notes
* common #central hub for logs, project data etc. 

```
python lbgm.py -dp project_name
```

deletes the folder tree.

```
python lbgm.py -me entity_type 
```

makes folders of specific name for every entity.

## Entities
Entity is a part of project specified with its physical or nonphysical parameters. 
* pcb_analog - pcb without any form of coding needed.
* pcb_mcu - pcb with microcontroler (avr or stm32 for example)
* pcb_mpu - with microprocessor or SoC (Raspberry Pi for example). May include microrontrolers as well.
* cable - specification of cables connecting diferrent systems.
* software - mobile or desktop app for control of device
* mech - mechanical part like enclosure