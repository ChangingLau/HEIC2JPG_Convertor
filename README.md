# **HEIC to JPG Convertor**
## **1. Prerequisite Environment**
1. **ImageMagick**. ImageMagick can be downloaded from [ImageMagick official website](https://imagemagick.org/index.php). Verify the installation by following script in **cmd**;  
   >  magick --version
2. **Python** and **Python Libraries**. Python 3 can be downloaded from [Python official website](https://www.python.org/). Libraries, including **tk** and **datetime**, could be installed by following two commands in **cmd**.
    >`pip install tk -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --user`  
 
    >`pip install datetime -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --user`  
## **2. Program Instruction**
**Note:** This is a GUI program built for selecting files' directory and starting heic file to jpg file convertion, which is built on [Python 3](https://www.python.org/) and [ImageMagick](https://imagemagick.org/index.php). Importantly, the entire convertion work is done totally by ImageMagick instead of Python.  
### Procedure
1. Enter target directory into HEIC Directory by typing in the path box or clicking on the Select Directory button. Upon completion of entering the directory, the log widget will print hint about whether directory is valid or not;
2. By clicking on the Start Processing button, ImageMagick will start processing heic files in the target directory;
3. Users should make advantage of log widget, which is an important interaction method between the program and users.  
