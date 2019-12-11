# building-meme-generation

## Markov Model
###### Markov code modified from https://github.com/pub12/MarkovText 

The ```markov``` folder contains the python files and dictionary for generating captions using an order 2 markov chain. To generate captions, use the command
```
python3 genCaption.py -n 5
```
The n parameter can be changed to change the number of captions generated at once. Note that the program checks if the caption it generated exists in the original dataset, and will try up to 10 times to generate an original caption before moving on. 


## Neural Net
###### uses textgenrnn from https://github.com/minimaxir/textgenrnn

The ```neuralNet``` folder contains an IPython notebook demonstrating using textgenrnn to train and generate a model. The ```models``` folder also contains the final trained model, which can be loaded and used by textgenrnn. 
