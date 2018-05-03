1. Module list: 
	There’re quite a few modules used in this project, including math, os, string, random, csv, re, struct, shutil, random, string, tkinter, bumpy, matplotlib, pandas, seaborn, sklearn, pickle, cv2, pillow, and pyscreenshot. Some of them are python built in modules, therefore no need to download and install. As for others, there is a python file named ‘module_manager.py’, make sure it’s in the same directory as other python files, and include:

		import module_manager
		module_manager.review()

on the top of the files that need to use the modules. If the module_manager doesn’t work (that may happen when install pyscreenshot), open terminal and type in:

		pip install moduleName

	Make sure your python version is up to date and you are using Python3.

2. Run the program:
	All required data and trained models are included. To run the final ‘Beauty Detector’, just open the file ‘face detection animation.py’ and run it in a ‘600x600’ window. 

3. Other files explanations:
	face detection animation.py: as mentioned above, the main animation file;
	minorMode.py: include the simple modes of the animation (start and end screen);
	shootMode.py: include openCV function that can capture pictures;
	analyzeMode.py: include openCV function that detect facial key points;
	editMode.py: edit screen;
	featureEditMode.py: key points edit screen;
	chooseMode.py: choose scorer screen;
	scoreMode.py: load machine learning model and get score, also include screenshot;
	haarcascadetection.py: raw openCV functions, but modified in shoot and analyze mode;
	ptsLoader.py: change the original pts file in raw dataset to txt files;
	generateFeature.py: manipulate the raw data and generate feature matrix and label column;
	train***Mode.py: use the data to train models.
