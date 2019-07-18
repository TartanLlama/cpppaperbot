from textgenrnn import textgenrnn

def generateTitle():
    saveFile = 'textgenrnn_weights_saved.hdf5'
    textgen = textgenrnn(saveFile)
    return textgen.generate(return_as_list=True, temperature=0.75, max_gen_length=140, progress=False)[0]

if __name__ == "main":
    print(generateTitle())