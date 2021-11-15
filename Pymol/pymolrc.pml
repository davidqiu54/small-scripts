# Created by: Seth Veenbaas
# Last date modified: 11/15/21


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
set surface_quality, 1
set solvent_radius, 1.6
set transparency, 0.5
set surface_color, grey80

# orthoscopic turns on and off the perspective handling
set orthoscopic, off


#### Custom Aliases #####

# RNA cartoon command
# Sets RNA cartoon style, removes ions and water, colors RNA lightteal and ligand brightorange.
alias rna, set cartoon_ring_mode, 3; set cartoon_ring_finder, 1; remove resn hoh; remove inorganic and not resn STP; cartoon oval; set cartoon_oval_length, 0.75; set cartoon_oval_width, 0.25; color lightteal, (polymer); color brightorange, organic; remove (byres polymer & name CA)

# RNA cartoon command + center
alias rna_c, rna; center

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
alias fpocket, stored.list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","1.0","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.0","pocket"+str(my_index))

# a-sphere appearence command with transparent a-spheres 
# NOTE: Ray tracing will not be able to render transparent surfaces if they are located behind a surface.
alias fpocket_t, stored.list=[]; cmd.iterate("(resn STP)","stored.list.append(resi)"); lastSTP=stored.list[-1]; hide lines, resn STP; for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index)); for my_index in range(2,int(lastSTP)+1): cmd.color(my_index,"pocket"+str(my_index));cmd.color(13,"pocket1"); for my_index in range(2,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","1.0","pocket"+str(my_index)); for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.4","pocket"+str(my_index))






