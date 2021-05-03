# Visualizing Biomolecular Interactions with Chimera

In this session we will make use of some tools in Chimera that can be useful to visualize biomolecular interactions.
We will have a look at the crystal structure of a tethered dimer of hiv-1 protease complexed with the inhibitor A79 (a short name for the beatiful N-{1-benzyl-(2s,3s)-2,3-dihydroxy-4-[3-methyl-2-(3-methyl-3-pyridin-2-ylmethyl-ureido)-butyrylamino]-5-phenyl-pentyl}-3-methyl-2-(3-methyl-3-pyridin-2-ylmethyl-ureido)-butyramide). The PDB code for this system is `1HVC`.

## Importing the PDB structure

Open Chimera. Get the PDB file by directly fetching it from the Protein Data Bank by selecting `File -> Fetch by ID`. Alternatively (recommended this time) go to the [PDB site](https://www.rcsb.org/structure/1HVC) and download the PDB file (click on `Download Files`, select the `PDB File (Text)` and download the file). After that, you can use your preferred text editor to explore the contents of the file. Check in particular the details of the different REMARK entries. You can check also the web page for the PDB entry to explore the detailes of the file (sequence, chains, methods used, etc...).

## Visualizing the system

If you already imported the PDB file directly from Chimera using the `Fetch by ID`tool you are already set. If you downloaded the file, go to `File -> Open... -> select your file -> Open`. Some basic actions that can be of general use are:

* `Select`menu: allows to select for different parts of the structure:
  * `Chain` to select protein chains
  * `Residue` to select specific residue types (all `ASP`, for example)
  * `Structure` interesting to select all the chains in a particular structure (important when you have several structures opened in Chimera)
* `Actions` menu: you can choose here what to render (the complete structure if nothing was selected in the `Select` menu)
  * `Atoms/Bonds` to show/hide atoms and bonds and to choose the way they are rendered
  * `Ribbon` to show/hide ribbons and to choose the way they are rendered
  * `Surface` to show/hide surface and to choose the way it is rendered
  * `Color` to select the color of the rendering

## Analyzing the molecular Interactions

## Sequence analysis

Firs we will check the sequence of our structure and compare it to the sequence of the corresponding Uniprot entry.

* Open the amino acid sequence of the protein by clicking on `Tools -> Sequence -> Sequence`. In the `Show Model Sequence` window select the chains of interest and click on `Show`. You can see the name and number of a particular residue by placing the cursor on top of it. Portions of the sequence highlighted in yellow correspond to alpha helices and green to beta strand. Amino acids in a red rectangle are not solved in the PDB deposited structure.

* Open the amino acid sequence in Uniprot by clicking on `Tools -> Sequence -> PDB/UniProt Info`. In the “PDB/UniProt Info” window select with a double click one of the chains: in this way two windows will appear.
The first window shows the sequence corresponding to the protein codified by the gene (UniProt sequence). Portions of sequence absent from the structure are surrounded by a pink box.
The second window shows some interesting and useful information, such as missing residues on the structures and sequence mismatching (PDB vs UNIPROTKB).
NB: 3D-Structural and Sequence windows are synchronized, so you can select amino acids from the sequence window by left button clicking+dragging over the amino acids and localized them on the 3D-structural window.

## Protein preparation

First of all it's necessary to prepare the protein structure in terms of reconstruction of missing residues, protonation and calculation of partial charges, which are essential for the following calculation of electrostatic potential.

* Click on `Tools → Structure Editing → Dock Prep`. In the window that will appear flag:
  * `Delete solvent`: this will remove the molecules of water
  * `Delete non-complexed ions`: this will remove ions not in complex with the protein !If alternate locations, keep only highest occupancy : in this way multiple conformations for the same atoms will be removed
  * `Incomplete side chains and leave the default option`: this will generate complete side chains for incomplete residues
  * `Add hydrogens`: this tool aims to generate protonation states reasonable at physiological pH
  * `Add charges`: this tool will assign partial charges to atoms
Click `OK`, leave the default options in the following two windows and click `OK` in both of them, while skip the eventual third window clicking on `Cancel`.

## Protein Interactions

We will have a look at H-Bonds, contacts and clashes:

* **H-BONDS**: we will detect hydrogen bonds at the interface between the two molecules of the complex. Click on `Tools → Surface/Binding Analysis → FindHBond`. In the “H-Bond Parameters” window that will appear flag:
  * `both` in the `Find these bonds` box
  * `Relax H-bond constraints` and set the values `0.5 angstroms` and `30.0 degree`, this way also non-ideal H-bonds, falling in this range of deviation from ideality, will be computed
  * `Color H-bonds not meeting precise criteria differently`: non-ideal H-bonds of the selected color will be drawn in the structure
  * `If endpoint atom hidden, show endpoint residue`: residues involved in H-bonds will be drawn in the structure
  * `Write information to file`: a list of the interacting residue will be saved

  Click on `OK`, choose the directory and the name of the file to save and click on `Save`.
    These operations will show the amino acids involved in intermolecular hydrogen bonds and will write a file with a list of residues involved in these interactions. For each couple of residues H-bond donor, acceptor, hydrogen atom, donor - - acceptor distance and donor-H - - acceptor distance are reported in the file.
    
CONT ACTS:
In this section we will identify all kind of interactions (polar and non-polar, favorable and unfavorable (clashes)) between the two proteins.
• Select both protein chains clicking on: Select → Structure → protein
• Click on:
Tools → Surface/Binding Analysis → Find Clashes/Contacts
• In the “Find Clashes/Contacts”:
! click on Designate and flag themselves : in this way only contacts between the
two proteins will be checked
! click on contact in Default clash/contact criteria , in order to choose the contact
instead of clash option
! flag the Color option
! flag the Draw pseudobonds of color option
! flag If endpoint atom hidden, show endpoint residue , to draw residues involved
in contacts
! Write information to file: a list of the interacting residue will be saved

At the end amino acids involved in intermolecular interactions of every kind (for example ionic locks have a key role in protein-protein interactions) will appear on the structure.
     CLASHES:
In this section we will identify unfavorable intermolecular interactions where atoms are too close together, that is clashes.
• If they are not already selected, select both protein chains clicking on: Select → Structure → protein
• Click on:
Tools → Surface/Binding Analysis → Find Clashes/Contacts
• In the “Find Clashes/Contacts”:
! click on Designate and flag themselves : in this way only contacts between the
two proteins will be checked
! click on clashes in Default clash/contact criteria , in order to choose the contact
instead of clash option
! flag the Color option, and use a different color from the one used for atoms
involved in contacts
! flag the Draw pseudobonds of color option, and use a different color from the
one used for contacts
! flag If endpoint atom hidden, show endpoint residue , to draw residues involved
in clashes
• De-select the proteins clicking on
Select → Clear Selection
At the end amino acids involved in clashes will appear on the structure.
o 4.4 Surface Analysis

Protein-protein recognition depends on the complementarity between the surface of the two proteins, that is a complementarity in shape and in electrostatic and hydrophobic interactions.
Therefore it's necessary to calculate the surface of proteins in the complex.
SURFACE REPRESENTATION:
It's necessary to save two separate PDB for the two proteins before generating the molecular surface.
• Select chain A clicking on: Select → Chain → A
• Delete Chain A clicking on: Actions → Atoms/Bonds → delete
• Save the Chain B clicking on:
File → Save PDB → choose the directory and the name of the file to save → Save
• Close the session clicking on: File → Close Session
• Open your original PDB and repeat the previous points deleting chain B and saving chain A
• Open the PDB of the chain B. Now you have loaded the structure of both chain A and chain B.
• Generate the molecular surface clicking on: Actions → Surface → show
ELECTROSTATIC POTENTIAL
In this section we will color the surface according to the Coulombic potential.
• Click on:
Tools → Surface/Binding Analysis → Coulombic Surface Coloring
• Select both the surfaces in the “Coulombic Surface Coloring” window (left
button+Ctrl)
• Use the default options and click on OK
As a result the surfaces will be colored according to the Coulombic potential, going from red (negative potential) to blue (positive potential).
HYDROPHOBIC POTENTIAL
In this section we will generate a hydrophobicity surface coloring the molecular surface by amino acid hydrophobicity.
• Click on:
Tools → Depiction → Render by attribute
• In the window “Render/Select by attribute”:
! Select both chains (left button + Ctrl) and choose residues in the Attributes of
section
! Choose kdHydrophobicity in the Attribute: section
! Choose Cyan-Maroon in the Palette: section
! Use the remaining default options and click on OK
As a result the surfaces will be colored according to amino acid hydrophobicity: more hydrophobic residues (larger positive values of hydrophobicity) are colored in maroon, while the hydrophilic residues (negative values of hydrophobicity) are colored in cyan.

STERIC COMPLEMETARITY
To observe shape complementarity, it's useful to move only one protein leaving the other fixed, in this way it will be possible to check if a pocket in one structure fits with a protrusion in the partner.
In the same way we can check if positive portions match negative ones, if hydrophobic portions match hydrophobic ones and if hydrophilic portions match hydrophilic ones.
• Click on:
! Favorites → Model Panel
! Make one structure inactive by de-flagging the column A box in the line
corresponding to that structure
! move the structure using the central mouse button (avoid to rotate the structure,
so don't use the left mouse button)
5. Conclusions
Thanks to the molecular surface and interaction analysis it's possible to understand some of the key features for protein-protein recognition, giving interesting hints about what happens in response to single point mutations.
