#!/usr/bin/python3

from PyAppDevKit.pyappdevkit import error_msg

lang = str(input('Which language (English or Turkish)?: '))

if lang == "English" or lang == "EN" or lang == "en":
    music_file_txt = "Music"
    video_file_txt = "Video"
    playlist_file_txt = "Playlist"
    videodownload_link_input_txt = "Please Paste the Video Link you want to download: "
    process_started_txt = "Download Process Started..."
    process_completed_txt = "Download Completed."
    video_file_named_downloaded_msg = "Video File Named Downloaded"
    playlistdownload_link_input_txt = "Enter Playlist Link: "
    playlist_downloading_msg = "Downloading Playlist Named..."
    pl_downloading_video_msg = "Downloading Video File Named..."
    downloaded_video_file_named_txt = "Downloaded Video File Named."
    audiodownload_link_input_txt = "Please Paste the Audio Link you want to download: "
    audio_downloaded_msg = "Audio File Named Downloaded."
    video_search_input_txt = "Type the name of the Video you want to search: "
    option_one = "1- Download Video"
    option_two = "2- Download Music"
    option_three = "3- Download Playlist"
    option_four = "4- Video Search"
    option_five = "5- Exit"
    choose_txt = "Please Make Your Choice: "
    exit_lang = "EN"
elif lang == "Türkçe" or lang == "TR" or lang == "tr":
    music_file_txt = "Müzik"
    video_file_txt = "Video"
    playlist_file_txt = "Çalma listesi"
    videodownload_link_input_txt = "Lütfen indirmek istediğiniz Video Bağlantısını Yapıştırın: "
    process_started_txt = "İndirme İşlemi Başladı..."
    process_completed_txt = "İndirme Tamamlandı."
    video_file_named_downloaded_msg = "Adlı video indirilmiştir."
    playlistdownload_link_input_txt = "Oynatma Listesi Bağlantısını giriniz: "
    playlist_downloading_msg = "Adlı Oynatma Listesi indiriliyor..."
    pl_downloading_video_msg = "Adlı video indirilmiştir..."
    download_video_file_named_txt = "İndirilen Video Dosyasının Adlandırıldı."
    audiodownload_link_input_txt = "Lütfen indirmek istediğiniz Ses Bağlantısını Yapıştırın: "
    audio_downloaded_msg = "Adlı ses dosyası indirilmiştir."
    video_search_input_txt = "Aramak istediğiniz Videonun adını yazın: "
    option_one = "1- Video indir"
    option_two = "2- Müzik indir"
    option_three = "3- Oynatma listesi indir"
    option_four = "4- Video Arama"
    option_five = "5- Çıkış"
    choose_txt = "Lütfen Seçiminizi Yapın: "
    exit_lang = "TR"
else:
     error_msg("Invalid language selection!","","")