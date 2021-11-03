<<<<<<< HEAD
# Created by: Seth Veenbaas
# Last date modified: 11/3/21


#### Startup settings ####
# set size of PYMOL window on boot
viewport 1500, 1000

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
set surface_quality, 0
set solvent_radius, 1.6
set transparency, 0.5
set surface_color, grey80

# orthoscopic turns on and off the perspective handling
set orthoscopic, off


#### Custom Aliases #####

# RNA cartoon command
alias rna, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; remove resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# RNA cartoon command + center
alias rna_c, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; center

# RNA+Protein cartoon command
alias rna_protein, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; color lightpink, resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# RNA ribbon command
alias rna_ribbon, set cartoon_ring_mode, 3; set cartoon_ring_finder, 0; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic

# RNA surface/ribbon command
alias rna_surface, set cartoon_ring_mode, 3; set cartoon_ring_finder, 0; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; show surface

# ligand colored by element
alias ligand, util.cbao (organic)

# Remove everything expect organic ligands
alias organic_only, remove not organic; h_add all

# Remove all amino acids
alias remove_protein, remove resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# Selects all amino acids
alias select_protein, select proteins, resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# a-sphere appearence command
# Creates selections to group a-spheres by pockets and colors them.
alias fpocket, stored.list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","1.0","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.0","pocket"+str(my_index))

# a-sphere appearence command with transparent a-spheres 
# NOTE: Ray tracing will not be able to render transparent surfaces if they are located behind a surface.
alias fpocket_t, stored.list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","1.0","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.4","pocket"+str(my_index))






=======
# Created by: Seth Veenbaas
# Last date modified: 11/3/21


#### Startup settings ####
# set size of PYMOL window on boot
viewport 1500, 1000

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
set surface_quality, 0
set solvent_radius, 1.6
set transparency, 0.5
set surface_color, grey80

# orthoscopic turns on and off the perspective handling
set orthoscopic, off


#### Custom Aliases #####

# RNA cartoon command
alias rna, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; remove resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# RNA cartoon command + center
alias rna_c, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; center

# RNA+Protein cartoon command
alias rna_protein, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; color lightpink, resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# RNA ribbon command
alias rna_ribbon, set cartoon_ring_mode, 3; set cartoon_ring_finder, 0; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic

# RNA surface/ribbon command
alias rna_surface, set cartoon_ring_mode, 3; set cartoon_ring_finder, 0; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; show surface

# ligand colored by element
alias ligand, util.cbao (organic)

# Remove everything expect organic ligands
alias organic_only, remove not organic; h_add all

# Remove all amino acids
alias remove_protein, remove resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# Selects all amino acids
alias select_protein, select proteins, resn Ala+Arg+Asn+Asp+Cys+Glu+Gln+Gly+His+Ile+Leu+Lys+Met+Phe+Pro+Ser+Thr+Trp+Tyr+Val

# a-sphere appearence command
# Creates selections to group a-spheres by pockets and colors them.
alias fpocket, stored.list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","1.0","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.0","pocket"+str(my_index))

# a-sphere appearence command with transparent a-spheres 
# NOTE: Ray tracing will not be able to render transparent surfaces if they are located behind a surface.
alias fpocket_t, stored.list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","1.0","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.4","pocket"+str(my_index))






>>>>>>> 025d130801db3f2de1199f50b8c6bafe1b900462
