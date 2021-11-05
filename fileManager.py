##########################################
# Code by R Rajesh                       #
##########################################
import os, shutil, re, time


def menu():
    print("================================ File Manager ======================================")
    print("Choose 1 : To Filter the file as per extension \nChoose 2 : Rename File \n\
Choose 3 : Remove numbers from the file name \nChoose 4 : Custom Extension \n\
Choice 5 : Custom name with Number \nChoose 0 : Exit")


def fbe():
    print("================================ Filter By extension ======================================")
    print("Choose 1 : For Imager Filer \nChoose 2 : For Video Filter \n\
Choose 3 : Ending With Customised Extension \nChoose 0 : Exit")


def imgf():
    print("=================== Image Filter ===================")
    src = input("Enter the source Path : ")
    dst = input("Enter the destination path : ")
    # To check all the files and sub files
    for root, dirs, files in os.walk(src):
        for file in files:
            # To check the particular file extensions
            extn = ['jpg', 'jpeg', 'bmp', 'png', 'gif', 'JPG']
            if any(file.endswith(ext) for ext in extn):
                # To check the errors and skip if any
                try:
                    shutil.move(os.path.join(root, file), os.path.join(dst, file))
                except Exception as e:
                    print(e)
                finally:
                    pass
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


def vf():
    print("=================== Video Filter ===================")
    src = input("Enter the source Path : ")
    dst = input("Enter the destination path : ")
    # To check all the files and sub files
    for root, dirs, files in os.walk(src):
        for file in files:
            # To check the particular file extensions
            extn = ['mp4', 'MP4', 'MOV']
            if any(file.endswith(ext) for ext in extn):
                # To check the errors and skip if any
                try:
                    shutil.move(os.path.join(root, file), os.path.join(dst, file))
                except Exception as e:
                    print(e)
                finally:
                    pass
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


def cf():
    print("=================== Custom Filter ===================")
    src = input("Enter the source Path : ")
    dst = input("Enter the destination path : ")
    ex = input("Enter The extension of your Choice without [DOT] : ")
    # To check all the files and sub files
    for root, dirs, files in os.walk(src):
        for file in files:
            # To check the particular file extensions
            extn = []
            # ['xlsx','xlsm','xlsb','xltx','xltm','xls','xlt','xls']
            extn.append(ex)
            if any(file.endswith(ext) for ext in extn):
                # To check the errors and skip if any
                try:
                    shutil.move(os.path.join(root, file), os.path.join(dst, file))
                except Exception as e:
                    print(e)
                finally:
                    pass
    extn.remove(ex)
    # print(extn)
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


def fr():
    print("================================ File Re_Name ======================================")
    src = input("Enter the file source path : ")
    # name = input("Enter the file name : ")
    i = 1
    for file in os.listdir(src):
        try:
            old_name = os.path.splitext(file)[0]
            # print(oldName)
            old_ext = os.path.splitext(file)[1]
            # # print(oldName)
            new_file_name = ("{}_" + old_name + old_ext).format(i)
            # # print(newFileName)
            os.rename(file, new_file_name)
            i += 1
        except Exception as e:
            print(e)
        finally:
            pass
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


def folr():
    print("================================ Folder Re-Name ======================================")
    print('WARNING : USE THIS OPTION ONLY FOR RENAMING FOLDER ELSE AT YOUR OWN RISK')
    src = input("Enter the file source path : ")
    for file in os.listdir(src):
        try:
            old_name = os.path.splitext(file)[0]
            new_name = re.sub("[0-9_-]", '', old_name)
            os.rename(file, new_name)
            # print(new_name)
        except Exception as e:
            print(e)
        finally:
            pass
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


def ce():
    print("================================ Customer Extension ======================================")
    src = input("Enter the file source path : ")
    extn = input("Enter your Extension including [DOT] : ")
    for file in os.listdir(src):
        try:
            old_name = os.path.splitext(file)[0]
            # print(oldName)
            old_ext = extn
            # # print(oldName)
            new_file_name = (old_name + old_ext)
            # # print(newFileName)
            os.rename(file, new_file_name)
        except Exception as e:
            print(e)
        finally:
            pass
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


def cnn():
    print("================================ Custom Name with Number ======================================")
    src = input("Enter the file source path : ")
    name = input("Enter the file name : ")
    i = 1
    for file in os.listdir(src):
        try:
            old_name = name
            # print(oldName)
            old_ext = os.path.splitext(file)[1]
            # # print(oldName)
            new_file_name = ("{}_" + old_name + old_ext).format(i)
            # # print(newFileName)
            os.rename(file, new_file_name)
            i += 1
        except Exception as e:
            print(e)
        finally:
            pass
    print("Done !")
    print("Time Taken %s seconds " % round((time.time() - start_time), 2))


try:
    start_time = time.time()
    while True:
        menu()
        opt = int(input("Enter Your Choice : "))
        if opt == 0:
            break
        if opt == 1:
            while True:
                fbe()
                Option = int(input("Enter your Choice : "))
                if Option == 0:
                    break
                if Option == 1:
                    imgf()
                if Option == 2:
                    vf()
                if Option == 3:
                    cf()
        if opt == 2:
            fr()
        if opt == 3:
            folr()
        if opt == 4:
            ce()
        if opt == 5:
            cnn()
except Exception as e:
    print(e)
finally:
    pass
