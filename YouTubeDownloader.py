from AppFunction.appfunction import *

while True:
    tprint("Lxlm-YTdownloader")
    print("""
-----------------------------------------------------------------------
{0}
{1}
{2}
{3}
{4}""". format(option_one,option_two,option_three,option_four,option_five))
    choose = input("\n{0}". format(choose_txt)) 

    if choose == "1":
        video_download()
    elif choose == "2":
        audio_download()
    elif choose == "3":
        playlist_download()
    elif choose == "4":
        video_search()
    elif choose == "5":
        all_exit(OFF,exit_lang,exitselectdialog_txt,usertimedialog_txt,exitdialog_txt,errormsgdialog_txt,SECOND)