# Running on Google Colab (tested for all weeks)
Google has released its own flavour of Jupyter called Colab, which has free GPUs!

Here's how you can use it:
1. Open https://colab.research.google.com, click **Sign in** in the upper right corner, use your Google credentials to sign in.
2. Click **GITHUB** tab, paste https://github.com/hse-aml/intro-to-dl-pytorch and press Enter
3. Choose the notebook you want to open, e.g. week01/week01_linear_models.ipynb
4. Click **File -> Save a copy in Drive...** to save your progress in Google Drive
5. Click **Runtime -> Change runtime type** and select **GPU** in Hardware accelerator box
6. Start with **executing** some of the first cells that download dependencies and import packages
7. Enjoy the assignment!
8. If you run many notebooks on Colab, they can continue to eat up memory,
you can kill them with `! pkill -9 python3` and check with `! nvidia-smi` that GPU memory is freed.
