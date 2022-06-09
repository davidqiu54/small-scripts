# PYMOL DEFAULT SETTINGS AND ALIASES GUIDE

### Custom default settings and aliases (custom functions) for PyMOL are stored in a configuration file titled pymolrc. The pymolrc file will initalize everytime you start PyMOL to incorrporate your custom setting automatically.  

### This tutorial will cover:

1. How to customize your PyMOL pymolrc file with default settings and/or aliases.
2. What to include in your PyMOL pymolrc file
3. How to write an basic PyMOL alias (custom function).
4. Example pymolrc files

# 1. Edit your pymolrc file

## QUICK SET-UP: Edit your pymolrc file in PyMOL

1. Open a window of PyMOL and choose, **File > Edit pymolrc**
2. Add your desired commands and aliases and save.  

    **If you plan to use the Weeks lab's default pymolrc.pml file:**
    - Copy the contents of the pymolrc.pml file from the Weeks-UNC/small-scripts/Pymol github directory.
    - Paste the contents of the pymolrc.pml file into your open notepad file and save.

## ADVANCED SET-UP: Edit your pymolrc file within the command line

### WINDOWS USERS:
1. Open command prompt window and paste
    > notepad "%HOMEDRIVE%%HOMEPATH%\pymolrc.pml"
2. This will open your pymolrc.pml file using notepad allowing you to make edits.
3. Add your desired commands and aliases and save.  

    **If you plan to use the Weeks lab's default pymolrc.pml file:**
    - Copy the contents of the pymolrc.pml file from the Weeks-UNC/small-scripts/Pymol github directory.  
    - Paste the contents of the pymolrc.pml file into your open notepad file and save.

### MAC/LINUX USERS:
1. Open your terminal and type  
    > nano ~/.pymolrc

    or (depending on your preference)

    > vim ~/.pymolrc
2. This will open your pymolrc.pml file in your perfered text editor allowing you to make edits.
3. Add your desired commands and aliases and save. 

    **If you plan to use the Weeks lab's default pymolrc.pml file:**  
    - Copy the contents of the pymolrc.pml file from the Weeks-UNC/small-scripts/Pymol github directory.  
    - Paste the contents of the pymolrc.pml file into your open nano session and save.

### MULTIPLE PYMOLRC FILES:

PyMOL will even load multiple pymolrc files, however only from the same directory.  
You can have multiple scripts: e.g. pymolrc-settings.pml and pymolrc-misc.pml in your home directory.

- pymolrc-settings.pml can e.g. be used to define 'permanent' custom Settings that you rarely change
- pymolrc-misc.pml can e.g. be used to define more transient custom Settings, such as Working Directory or Fetch Path

You can query which pymolrc files have been loaded:

> PyMOL> print invocation.options.deferred

**NOTE:** You do NOT need to use the PYMOL API format in pymolrc.pml files.

# 2. What to include in your pymolrc file

### Your pymolrc file should contain settings that you always apply to your PyMOL sessions. 
### Examples:

- ### Apply basic settings to PyMOL 

      # Change backround color to white for easier viewing.
      bg_color white

      # Display sequence viewer.
      set seq_view, 1

      # Toggles whether PyMOL loops movies.
      set movie_loop, 1

      # Save fetched PDB files here.
      set fetch_path, /your/fetch/path

- ### Apply consistent styles
        
      # Adjust the thickness of atomic bonds viewed as sticks.
      set stick_radius, 0.3

      # Adjust the radius of spheres.
      set sphere_scale, 1

      # Settings related to surface features.
      set surface_quality, 1
      set solvent_radius, 1.6
      set transparency, 0.5
      set surface_color, grey80

      # Settings related to labels.
      set label_size, 60
      set label_outline_color, 1
      set label_color, 0
      set label_position, [0, 0, 10]
        
- ### Apply raytrace settings

      # Enable multi-thread processing for faster ray trace processing.
      set max_threads, 4

      # Sets specular reflection intensity to lowwer value for aesthetics. 
      set specular, 0.1

      # Removes distracing shadows from ray-traced images.
      set ray_shadows, off

      # Improves antiliasing/edge smoothing for ray-traced images.
      set antialias, 2

- ### Apply aliases (custom function)

    Adding an alias (custom function) to your pymolrc file will ensure that it can be used by default anytime you use PyMOL.  
    Creating an alias is covered below in section 3.


Read more at: https://pymolwiki.org/index.php/Pymolrc

# 3. Create your own PyMOL alias

**alias** allows you to bind a commonly used command (or series of commands) to a single PyMOL keyword of your choice.  
In essence, aliases allow you to add customized functions to PyMOL.

## USAGE
 
> PyMOL> alias *name*, *command-sequence*

alias: name of the PyMOL command for creating a new alias.  
*name*: name of your new custom function.  
*command-sequence*: list of your desired PyMOL> command line commands. 

## EXAMPLES

### Aliases can be used to simplify a commonly used command or series of commands into a single function name.
    
- remove_protein: alias which removes all amino acid residues.
    > PyMOL> alias remove_protein, remove (byres polymer & name CA)

- ligand: alias which shows organic ligands as wires and colors them by element (orange).

    > PyMOL> alias ligand, show wire, organic; util.cbao (organic)

### Aliases are speficically useful for consistantly applying style settings for publication.

- rna: alias which implements a cartoon style for RNAs.
    > PyMOL> alias rna, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; remove (byres polymer & name CA)

<p float="left">
  <img src="https://github.com/Weeks-UNC/small-scripts/blob/master/Pymol/Images/3E5C_RNA_Default_Style.png?raw=true" width="200" />
  <img src="https://github.com/Weeks-UNC/small-scripts/blob/master/Pymol/Images/3E5C_RNA_rna_Style.png?raw=true" width="200" /> 
  <img src="https://github.com/Weeks-UNC/small-scripts/blob/master/Pymol/Images/3E5C_RNA_rna_s_ligand_Style.png?raw=true" width="200" />
</p>


## NOTES

Multiple commands should be seperated by a semi-colon.

After defining an alias, you can implement your alias simply by entering the alias name into the PyMOL> command line.
	
Read more at: https://pymolwiki.org/index.php/Alias

# 4. Example pymolrc files

### From https://pymolwiki.org/index.php/Pymolrc

    # simple test: change background color of PyMOL window
    bg blue

    # this will run the script in the specified location
    run /path/to/home/pymol/load_sep.py

    # your favorite settings
    set movie_loop, 0
    set two_sided_lighting, 1

    set label_size, 60
    set label_outline_color, 1
    set label_color, 0
    set label_position, [0, 0, 10]

    # for images:
    #   antialias =1 smooths jagged edges, 0 turns it off
    set antialias, 1

    #   stick_radius -adjust thickness of atomic bonds
    set stick_radius, 0.3

    # save fetched PDB files here
    set fetch_path, /your/fetch/path

    # Personal short-cut to color_obj function
    import color_obj
    cmd.extend("co",color_obj.color_obj)

### From https://betainverse.wordpress.com/2017/04/14/pymol-default-settings-pymolrc/

    # default path that PyMOL uses to load files from before it tries to download them from the PDB.
    set fetch_path, /home/edmonds/PDBs/
    
    # use white background
    bg_color white
    
    # set ray tracing settings
    set ray_opaque_background, off
    set ray_shadows,off
    
    # run custom pymol scripts
    run /home/edmonds/scripts/pymolscripts/data2bfactor.py
    run /home/edmonds/scripts/pymolscripts/spectrumany.py
    
### From http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/

    # use white background
    set bg_rgb, 1 1 1

    # set orthoscopic, rather than perspective as the default
    set orthoscopic, 1

    # set size of graphics window
    #viewport 800, 600
    viewport 1100, 900

    set hash_max, 170

    # turn off auto zoom
    set auto_zoom, 0

    set cgo_line_radius, 0.05
    set line_width, 2
    set cgo_line_width, 2
    set ribbon_radius, .2
    set ribbon_width, 2
    set ribbon_sampling, 1
    set cartoon_smooth_loop, 0

    set stick_radius, .2
    set fog, 1.

    # set spec_refl to 2. for bright reflections, .5 for dimmer
    set spec_refl, 1.5
    # set spec_power to 200 for tight reflections, 40 for broader
    set spec_power, 100

    # default to antialiased rendering (on or 1)
    set antialias, on
    # to set background to transparent for ray tracing, set the following off, or 0
    set ray_opaque_background, on

    # The following may not be necessary now as one can set the preferred
    # color space see the "Display -> Color Space" menu item in the main GUI
    #optimized rgb values for cmyk output:
    set_color _dblue= [0.05 , 0.19 , 0.57]
    set_color _blue=  [0.02 , 0.50 , 0.72]
    set_color gold, [1.0, 0.8, 0.0]
    set_color gold2, [0.90, 0.6, 0.0]
    set_color lightblue, [0.6, 0.8, 1.0]
    set_color lightgreen, [0.,1.0, 0.3]
    set_color darkgreen, [0.,0.7,0.0]


    # run some of my scripts (see http://adelie.biochem.queensu.ca/~rlc/work/pymol/ for these)
    run c:\Program Files\DeLano Scientific\PyMOL\load_best.py
    run c:\Program Files\DeLano Scientific\PyMOL\load_models.py
    run c:\Program Files\DeLano Scientific\PyMOL\load_sep.py
    run c:\Program Files\DeLano Scientific\PyMOL\load_list.py

### From Seth Veenbaas.
### Settings designed for RNA and fpocket.

    # Created by: Seth Veenbaas
    # Last date modified: 05/03/22
    ----------------------------------------

    #### Startup settings ####
    # set size of PYMOL window on boot
    viewport 1500, 1000

    # enable multi-thread processing
    set max_threads, 4

    # change backround color
    bg_color white

    # display sequence viewer
    set seq_view, 1

    # sets specular reflection intensity
    set specular, 0.1

    # controls appearence of shadows for ray-traced images
    set ray_shadows, off

    # controls antiliasing/edge smoothing for ray-traced images
    set antialias, 2

    # settings related to surface features
    set surface_quality, 1
    set solvent_radius, 1.6
    set transparency, 0.5
    set surface_color, grey80

    # settings related to rendering meshes
    set mesh_quality, 2
    set mesh_type, 0
    set mesh_width, 0.5
    set mesh_radius, 0.015

    # orthoscopic turns on and off the perspective handling
    set orthoscopic, off


    #### Custom Aliases #####

    # RNA cartoon command
    # Sets RNA cartoon style, removes ions and water, colors RNA lightteal and ligand brightorange.
    alias rna, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; remove (byres polymer & name CA)

    # RNA cartoon command + extract ligand as an object
    alias rna_o, rna; extract Ligand, organic; util.cbao (organic)

    # RNA cartoon command + colors proeteins lightpink instead of removing.
    alias rna_protein, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; color lightpink, (byres polymer & name CA)

    # RNA & Protein command + extracts objects for proteins and ligands
    alias rna_protein_o, rna_protein; extract Protein, (byres polymer & name CA); extract Ligand, organic; orient

    # Ribosome
    alias ribosome, set surface_quality, 0; rna_protein_o

    # RNA ribbon command
    alias rna_ribbon, set cartoon_ring_finder, 0

    # Show surface of RNA only
    alias rna_s, show surface, resn A+U+C+G

    # Show surface of RNA and Protein
    alias rna_protein_s, show surface, resn A+U+C+G; show surface, Protein; set surface_color, lightpink, Protein

    # RNA ribbon command + show surface
    alias rna_ribbon_s, rna_ribbon; show surface

    # ligand colored by element
    alias ligand, util.cbao (organic)

    # shows details of ligand binding site.
    alias binding_site, ligand; select Binding_Site, byresidue polymer within 4.5 of organic; set cartoon_ring_finder, 0; show sticks, Binding_Site; util.cnc Binding_Site; contacts Ligand, Binding_Site; disable contacts_all & contacts_aa & contacts_dd; hide labels, contacts; color purple, contacts_polar; color purple, contacts_polar_ok; color tv_yellow, contacts_all; zoom (Ligand)

    # Remove everything expect organic ligands + adds hydrogens
    alias remove_not_organic, remove not organic; h_add all

    # Remove all amino acids
    alias remove_protein, remove (byres polymer & name CA)

    # Selects all amino acids
    alias select_protein, select proteins, (byres polymer & name CA)

    # removes predicted fpockets that interact with proteins
    alias sort_pockets, extract Protein_Pockets, byresidue resn STP within 4 of (byres polymer & name CA); extract RNA_Pockets, byresidue resn STP and not Protein_Pockets; color purple, Protein_Pockets; color tv_orange, RNA_Pockets

    # a-sphere appearence command
    # Creates selections to group a-spheres by pockets and colors them.
    alias fpocket, stored.list=[]; stored.b_list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); cmd.iterate("(resn STP)","stored.b_list.append(b -2)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale", stored.b_list[my_index], "resn STP and resi "+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.0","pocket"+str(my_index))


        
