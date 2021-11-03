<<<<<<< HEAD

This tutorial is for creating default settings and alias commands for Pymol. 
Custom default settings and alias are stored in a pymol configuration file titled pymolc.pml. 

To make changes to this file:

Windows Users:
	1) Open command prompt window and type:
		notepad "%HOMEDRIVE%%HOMEPATH%\pymolrc.pml"
		
Unix/Linux Users:
	1) Open your terminal and type:
		nano ~/.pymolrc
	
2) This should open your pymol.pml file using notepad (Winodows) or Nano (Unix/Linux) and allow you to make edits.
3) Add desired comands and aliases to file and save. 

https://pymolwiki.org/index.php/Pymolrc
	
NOTE: You do NOT need to use the PYMOL API format in this file. 

###################################################################################


Aliases allow you to name your known custom commands in pymol.
Template for making an alias:
	alias name, command-sequence
	
	https://pymolwiki.org/index.php/Alias


Example pymolrc.pml files:

	From https://betainverse.wordpress.com/2017/04/14/pymol-default-settings-pymolrc/ :

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
		
	
	From http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/ : 

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

=======

This tutorial is for creating default settings and alias commands for Pymol. 
Custom default settings and alias are stored in a pymol configuration file titled pymolc.pml. 

To make changes to this file:

Windows Users:
	1) Open command prompt window and type:
		notepad "%HOMEDRIVE%%HOMEPATH%\pymolrc.pml"
		
Unix/Linux Users:
	1) Open your terminal and type:
		nano ~/.pymolrc
	
2) This should open your pymol.pml file using notepad (Winodows) or Nano (Unix/Linux) and allow you to make edits.
3) Add desired comands and aliases to file and save. 

https://pymolwiki.org/index.php/Pymolrc
	
NOTE: You do NOT need to use the PYMOL API format in this file. 

###################################################################################


Aliases allow you to name your known custom commands in pymol.
Template for making an alias:
	alias name, command-sequence
	
	https://pymolwiki.org/index.php/Alias


Example pymolrc.pml files:

	From https://betainverse.wordpress.com/2017/04/14/pymol-default-settings-pymolrc/ :

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
		
	
	From http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/ : 

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

>>>>>>> 025d130801db3f2de1199f50b8c6bafe1b900462
