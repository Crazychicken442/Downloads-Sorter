import os
import shutil

userName = str(input("Please insert your Account User Name: "))
drive = str(input("What drive is your Downloads folder on? "))
directory = drive+":\\Users\\"+userName+"\\Downloads"
Audio = drive+":\\Users\\"+userName+"\\Downloads\\Audio"
Zipped = drive+":\\Users\\"+userName+"\\Downloads\\Zipped"
Disc = drive+":\\Users\\"+userName+"\\Downloads\\Disc"
Data = drive+":\\Users\\"+userName+"\\Downloads\\Data"
Email = drive+":\\Users\\"+userName+"\\Downloads\\Email"
Exe = drive+":\\Users\\"+userName+"\\Downloads\\Exe"
Font = drive+":\\Users\\"+userName+"\\Downloads\\Font"
Image = drive+":\\Users\\"+userName+"\\Downloads\\Image"
Internet = drive+":\\Users\\"+userName+"\\Downloads\\Internet"
Presentation = drive+":\\Users\\"+userName+"\\Downloads\\Presentation"
Programming = drive+":\\Users\\"+userName+"\\Downloads\\Programming"
Spreadsheet = drive+":\\Users\\"+userName+"\\Downloads\\Spreadsheet"
System = drive+":\\Users\\"+userName+"\\Downloads\\System"
Video = drive+":\\Users\\"+userName+"\\Downloads\\Video"
Text = drive+":\\Users\\"+userName+"\\Downloads\\Text"
Other = drive+":\\Users\\"+userName+"\\Downloads\\Other"


if os.path.isdir(directory) is True:
    for filename in os.listdir(directory):
        if filename.endswith(".aif") or filename.endswith(".cda") or filename.endswith(".mid") or filename.endswith(".midi") or filename.endswith(".mp3") or filename.endswith(".mpa") or filename.endswith(".ogg") or filename.endswith(".wav") or filename.endswith(".wma") or filename.endswith(".wpl"):
            if os.path.isdir(Audio) is False:
                os.mkdir(Audio)
            shutil.move(filename, Audio)
            
        elif filename.endswith(".7z") or filename.endswith(".arj") or filename.endswith(".deb") or filename.endswith(".pkg") or filename.endswith(".rar") or filename.endswith(".tar.gz") or filename.endswith(".z") or filename.endswith(".zip"):
            if os.path.isdir(Zipped) is False:
                os.mkdir(Zipped)
            shutil.move(filename, Zipped)
            
        elif filename.endswith(".bin") or filename.endswith(".dmg") or filename.endswith(".iso") or filename.endswith(".toast") or filename.endswith(".vcd"):
            if os.path.isdir(Disc) is False:
                os.mkdir(Disc)
            shutil.move(filename, Disc)
            
        elif filename.endswith(".email") or filename.endswith(".eml") or filename.endswith(".emlx") or filename.endswith(".msg") or filename.endswith(".oft") or filename.endswith(".ost") or filename.endswith(".pst") or filename.endswith(".vcf"):
            if os.path.isdir(Email) is False:
                os.mkdir(Email)
            shutil.move(filename, Email)
            
        elif filename.endswith(".apk") or filename.endswith(".bat") or filename.endswith(".bin") or filename.endswith(".cgi") or filename.endswith(".pl") or filename.endswith(".com") or filename.endswith(".exe") or filename.endswith(".gadget") or filename.endswith(".jar")  or filename.endswith(".msi")  or filename.endswith(".py")  or filename.endswith(".wsf") or filename.endswith(".err"):
            if os.path.isdir(Exe) is False:
                os.mkdir(Exe)
            shutil.move(filename, Exe)
            
        elif filename.endswith(".fnt") or filename.endswith(".fon") or filename.endswith(".otf") or filename.endswith(".ttf"):
            if os.path.isdir(Font) is False:
                os.mkdir(Font)
            shutil.move(filename, Font)
            
        elif filename.endswith(".ai") or filename.endswith(".bmp") or filename.endswith(".gif") or filename.endswith(".ico") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".ps") or filename.endswith(".psd") or filename.endswith(".svg") or filename.endswith(".tif") or filename.endswith(".tiff") or filename.endswith(".jfif") or filename.endswith(".webp") or filename.endswith(".PNG") or filename.endswith(".HEIC"):
            if os.path.isdir(Image) is False:
                os.mkdir(Image)
            shutil.move(filename,Image)
            
        elif filename.endswith(".asp") or filename.endswith(".aspx") or filename.endswith(".cer") or filename.endswith(".cfm") or filename.endswith(".cgi") or filename.endswith(".pl") or filename.endswith(".css") or filename.endswith(".htm") or filename.endswith(".html") or filename.endswith(".js") or filename.endswith(".jsp") or filename.endswith(".part") or filename.endswith(".php") or filename.endswith(".py") or filename.endswith(".rss") or filename.endswith(".xhtml"):
            if os.path.isdir(Internet) is False:
                os.mkdir(Internet)
            shutil.move(filename,Internet)
        
        elif filename.endswith(".key") or filename.endswith(".odp") or filename.endswith(".pps") or filename.endswith(".ppt") or filename.endswith(".ppx"):
            if os.path.isdir(Presentation) is False:
                os.mkdir(Presentation)
            shutil.move(filename,Presentation)
            
        elif filename.endswith(".c") or filename.endswith(".c") or filename.endswith(".class") or filename.endswith(".cpp") or filename.endswith(".cs") or filename.endswith(".h") or filename.endswith(".java") or filename.endswith(".php") or filename.endswith(".py") or filename.endswith(".sh") or filename.endswith(".swift") or filename.endswith(".vb") or filename.endswith(".ipynb"):
            if os.path.isdir(Programming) is False:
                os.mkdir(Programming)
            shutil.move(filename,Programming)
            
        elif filename.endswith(".ods") or filename.endswith(".xls") or filename.endswith(".xlsm") or filename.endswith(".xlsx") or filename.endswith(".csv"):
            if os.path.isdir(Spreadsheet) is False:
                os.mkdir(Spreadsheet)
            shutil.move(filename,Spreadsheet)
            
        elif filename.endswith(".bak") or filename.endswith(".cab") or filename.endswith(".cfg") or filename.endswith(".cpl") or filename.endswith(".cur") or filename.endswith(".dll") or filename.endswith(".dmp") or filename.endswith(".drv") or filename.endswith(".icms") or filename.endswith(".ico") or filename.endswith(".ini") or filename.endswith(".lnk") or filename.endswith(".msi") or filename.endswith(".sys") or filename.endswith(".tmp"):
            if os.path.isdir(System) is False:
                os.mkdir(System)
            shutil.move(filename,System)
       
        elif filename.endswith(".3g2") or filename.endswith(".3gp") or filename.endswith(".avi") or filename.endswith(".flv") or filename.endswith(".h264") or filename.endswith(".m4v") or filename.endswith(".mkv") or filename.endswith(".mov") or filename.endswith(".mp4") or filename.endswith(".mpg") or filename.endswith(".mpeg") or filename.endswith(".rm") or filename.endswith(".swf") or filename.endswith(".vob")  or filename.endswith(".wmv"):
            if os.path.isdir(Video) is False:
                os.mkdir(Video)
            shutil.move(filename,Video)
            
        elif filename.endswith(".txt") or filename.endswith(".doc") or filename.endswith(".docx") or filename.endswith(".odt") or filename.endswith(".pdf") or filename.endswith(".rtf") or filename.endswith(".tex") or filename.endswith(".wpd") or filename.endswith(".log"):
            if os.path.isdir(Text) is False:
                os.mkdir(Text)
            shutil.move(filename, Text)
            
        else:
            if os.path.isdir(Other) is False:
                os.mkdir(Other)
            shutil.move(filename,Other)
            
            
else:
    print("Your directory cannot be found. Please try again")