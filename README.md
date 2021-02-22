# DSP_Collect
Using [TheHologram's](https://github.com/TheHologram/unity-console) python console for Unity games, these scripts collect the attributes of objects of the game Dyson Sphere Program.

# Why?
I want to build some tools to make some stuff easier in DSP, but first I wanted some sort of reference to the members of the game's objects.
I also did not want to do anything in C#, so TheHologram's tool is very useful for executing Python scripts.

# How?
You need to install TheHologram's program, and add this directory to /Console/Mods
Then, when loaded into the game, load a save and enter the following:

`import dsp_doc_collect`

`dsp_doc_collect.main()`

This will write several JSON files to the DSP main directory in /Steam/steamapps/common/. These will need to be moved to /Mods/DSP_Collect, where you can run `parser.py` and `to_latex.py`.
