from textgenrnn import textgenrnn

saveFile = 'textgenrnn_weights_saved.hdf5'
textgen = textgenrnn(saveFile)
textgen.train_from_file('titles.txt', num_epochs=1)
textgen.save(saveFile)