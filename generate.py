from textgenrnn import textgenrnn

saveFile = 'textgenrnn_weights_saved.hdf5'
textgen = textgenrnn(saveFile)
textgen.generate(temperature=0.75, max_gen_length=140, progress=False)