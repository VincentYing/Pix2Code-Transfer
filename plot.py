import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.interpolate import spline


def plot_charts(modelName):
  fileObj = open("./" + modelName, 'r')

  epoch = []
  trainLoss = []
  trainScore = []
  valLoss = []
  valScore = []

  # Read in File
  for line in fileObj:
    words = line.split("-")
    for i in range(len(words)):
      if words[i] == 'epoch':
        print(int(words[i+1]))
        epoch.append(int(words[i+1]))
      elif words[i] == 'val_loss':
        print(float(words[i+1]))
        valLoss.append(float(words[i+1]))
      elif words[i] == 'loss':
        print(float(words[i+1][:-6]))
        trainLoss.append(float(words[i+1][:-6]))

  fileObj.close()

  print epoch
  print valLoss
  print trainLoss

  minValLoss = min(valLoss)
  epochValLoss = np.argmin(valLoss)

  # Curvefit
  x_new = np.linspace(epoch[0], epoch[-1], 50)
  y_new = spline(epoch, trainLoss, x_new)
  y_new2 = spline(epoch, valLoss, x_new)

  # Plot Loss and Score
  plt.figure()

  # train/val loss
  plt.xlim([epoch[0]-1, epoch[-1] + 1 ])
  plt.plot(x_new, y_new, label='Training')
  plt.plot(x_new, y_new2, label='Validation')
  #plt.plot(epochValLoss, minValLoss, marker='x', markersize=3, color="black")
  plt.xlabel('Epochs')
  plt.ylabel('Loss')
  plt.title('Training and Validation Loss')
  plt.legend()
  plt.minorticks_on()

  plt.show()
  plt.savefig("./" + modelName + ".png")


if __name__ == '__main__':
  modelName = sys.argv[1]
  plot_charts(modelName)
