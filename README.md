# **HEIC to JPG Convertor**
## **1. Prerequisite Environment**
1. **ImageMagick**, it can be downloaded from [ImageMagick official website](https://imagemagick.org/index.php), after installation it can be verified by following script in **cmd**;  
   >  magick --version
2. **Python** and **Python Libraries**, python can be downloaded from [Python official website](https://www.python.org/); and libraries includes **tk** and **datetime**, which could be installed by following two scripts in **cmd**.
    >`pip install tk -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --user`  
 
    >`pip install datetime -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --user`  
## **2. Program Instruction**
**Note:** This is a GUI program built for selecting files' directory and starting heic file to jpg file convertion, which is built on [Python 3](https://www.python.org/) and [ImageMagick](https://imagemagick.org/index.php), importantly, the entire convertion work is done totally by ImageMagick instead of Python.  
### Procedure
1. Enter target directory into HEIC Directory by typing or clicking on the Select Directory button, the log widget will print hint whether directory is valid or not;
2. By clicking on the Start Processing button ImageMagick will start processing heic files in the target directory;
3. Users should make good use of log widget, which is an important interaction method between the program and users.  