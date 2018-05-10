# Pix2Code with Capsule Network

The field took off last year when Tony Beltramelli introduced the [pix2code paper](https://arxiv.org/abs/1705.07962) and Airbnb launched [sketching interfaces](https://airbnb.design/sketching-interfaces/). 

In this project, we’ll teach a neural network how to code a basic HTML and CSS website based on a picture of a design mockup. Instead of the standard CNN encoder, we will substitute in a Capsule Network a network architecture created by a team under Geoffrey Hinton. [Paper](https://arxiv.org/abs/1710.09829).


#### A quick overview of the process: 

1) Give a design image to the trained neural network

2) The neural network converts the image into HTML markup 

3) Rendered output

## Installation

### Local
``` bash
pip install keras
pip install tensorflow
pip install pillow
pip install h5py
pip install jupyter

cd Pix2Code-CapsNet/local
jupyter notebook
```
Go do the desired notebook, files that end with '.ipynb'. To run the model, go to the menu then click on Cell > Run all

The model is prepared with a small set to test run. If you want to try it with all the data, you need to download the data here: https://www.floydhub.com/emilwallner/datasets/imagetocode, and specify the correct ```dir_name```.

## Model Architecture
<p align="center"><img src="/README_images/Bootstrap_model.png?raw=true" width="400px"></p>


### Acknowledgments
- This project is influenced by Tony Beltramelli's pix2code paper. [Code](https://github.com/tonybeltramelli/pix2code) [Paper](https://arxiv.org/abs/1705.07962)
- The code is based on Emil Wallner's blog post. [Blog](https://blog.floydhub.com/Turning-design-mockups-into-code-with-deep-learning/)  [Code](https://github.com/emilwallner/Screenshot-to-code-in-Keras)
