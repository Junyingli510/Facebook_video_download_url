#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import requests as r
import wget

filedir = os.path.join('./download')
ERASE_LINE = '\x1b[2K'

def menu():
    print("-------------------Facebook Video Downloader-------------------")
    print("1. Download Low Resolution Video")
    print("2. Download High Resolution Video")
    print("3. Exit")
    print("-------------------*******-------------------------------------")

menu()
CHOICE = input("ENTER YOUR CHOICE: ")

if CHOICE == "1":
    try:
        LINK = input("Enter a Facebook Video Post URL: ")
        html = r.get(LINK)
        sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
    except r.ConnectionError as e:
        print("OOPS!! Connection Error.")
    except r.Timeout as e:
        print("OOPS!! Timeout Error")
    except r.RequestException as e:
        print("OOPS!! General Error or Invalid URL")
    except (KeyboardInterrupt, SystemExit):
        print("Ok ok, quitting")
        sys.exit(1)
    except TypeError:
        print("Video May Private or Invalid URL")
    else:
        sd_url = sdvideo_url.replace('sd_src:"', '')
        print("\n")
        print("Normal Quality: " + sd_url)
        print("[+] Video Started Downloading")
        wget.download(sd_url, filedir)
        sys.stdout.write(ERASE_LINE)
        print("\n")
        print("Video downloaded")

elif CHOICE == "2":
    try:
        LINK = input("Enter a Facebook Video Post URL: ")
        html = r.get(LINK)
        hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
    except r.ConnectionError as e:
        print("OOPS!! Connection Error.")
    except r.Timeout as e:
        print("OOPS!! Timeout Error")
    except r.RequestException as e:
        print("OOPS!! General Error or Invalid URL")
    except (KeyboardInterrupt, SystemExit):
        print("Ok ok, quitting")
        sys.exit(1)
    except TypeError:
        print("Video May Private or Hd version not avilable")
    else:
        hd_url = hdvideo_url.replace('hd_src:"', '')
        print("\n")
        print("High Quality: " + hd_url)
        print("[+] Video Started Downloading")
        wget.download(hd_url, filedir)
        sys.stdout.write(ERASE_LINE)
        print("\n")
        print("Video downloaded")

elif CHOICE == "3":
    print("Exiting")

else:
    print("[-] Invalid option!")