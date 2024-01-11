# Keto Strip Analyzer
This keto strip analyzer is a tool for analyzing images of ketostrip tips to estimate ketone levels. It identifies the color present, and maps it to specific ketone concentration levels based on predefined color standards. 

* Limitation
  * Images need to be manually cropped to include only the tip.

This project includes a dataset of ketostrip images along with XML annotations in PASCAL VOC format, intended for training custom models for ketostrip analysis.

**The included Keto Strip Analyzer script does not utilize the training data, but it is available for independent use or development.**

![](https://github.com/FightingFalcon/KetoStripAnalyzer/blob/main/keto_gif.gif)

### Installation
Make sure Python is installed on your system and install opencv
```
pip install opencv-python
```
Set the image_path variable to the path of your ketostrip image.
```
image_path = 'path/to/your/image.png'
```
Run the script
```
python keto_strip_analyzer.py
```
Example
```
# In the script
image_path = 'images/ketostrip_example.png'

# Output
Estimation: 4.0 mmol/L - Moderate amounts
```
