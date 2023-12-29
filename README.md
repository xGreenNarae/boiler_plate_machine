
## Boiler Plate Machine

a cli tool to generate boiler plate code files with directories by using templates

Note: if you need a single file generation, use IDE's file template feature instead. it is more convenient.

### Usage

there are two types of configuration files.  
1. structure config file  
define directories and files structure with yaml.  

2. template files  
define content of file with jinja2 template syntax.( just enclose variable with {{ }} )  

structure config file path is `~/.config/bpm/structures/<structure_config_filename>.yaml`   
template files path is `~/.config/bpm/templates/<template_filename>`  


1. make templates  

1-1. make directory structure file with yaml
```yaml
# ~/.config/bpm/structures/3layer.yaml
- 3layer/:
    - "{{name}}Controller.java": "Controller.tpl" # extension should not necessarily be .tpl
    - "{{name}}Service.java": "Service.tpl"
    - "{{name}}Repository.java": "Repository.tpl"
```
Note1: all items should be list( '-' at the beginning of line )  
Note2: directory should ends with '/' and filename should not.   
Note3: filename field means `<filename>: <template filename>`.  


1-2. make template files for each files
```
# ~/.config/bpm/templates/Controller.tpl  
import {{ package_name }}

@RestController
@RequiredArgsConstructor
@RequestMapping("/{{ name }}")
public class {{ name }}Controller {
    private final {{ name }}Service {{ name|lower }}Service;


}
```
...



2. generate boiler plate  

use `dist/bpm` binary file for now.

`bpm <structure_config_filename> <target_directory>`

---


### TODO
- show list of config files
- add, remove config files easily
