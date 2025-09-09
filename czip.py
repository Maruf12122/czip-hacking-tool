#!/usr/bin/env python

import pyzipper
import argparse
import os
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("czip", font="slant")
    print(banner)
    print("🔓 ZIP Password Cracker | By Minera\n")

def crack_zip(zip_path, wordlist_path):
    if not os.path.exists(zip_path):
        print("❌ ZIP ফাইল পাওয়া যায়নি:", zip_path)
        return
    if not os.path.exists(wordlist_path):
        print("❌ ওয়ার্ডলিস্ট পাওয়া যায়নি:", wordlist_path)
        return

    print("🔍 ক্র্যাকিং শুরু হয়েছে...\n")

    try:
        with pyzipper.AESZipFile(zip_path) as zf:
            with open(wordlist_path, 'r', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    try:
                        zf.pwd = password.encode('utf-8')
                        zf.extractall()
                        print(f"\n✅ পাসওয়ার্ড পাওয়া গেছে: {password}")
                        print("📁 ফাইল আনজিপ করা হয়েছে সফলভাবে!")
                        return
                    except RuntimeError:
                        print(f"❌ চেষ্টা করা হলো: {password}")
                    except Exception as e:
                        print(f"⚠️ সমস্যা: {e}")
        print("\n😔 দুঃখিত, ওয়ার্ডলিস্টে সঠিক পাসওয়ার্ড পাওয়া যায়নি।")
    except Exception as e:
        print(f"🚫 ZIP ফাইল ওপেন করতে সমস্যা হয়েছে: {e}")

def main():
    show_banner()

    parser = argparse.ArgumentParser(
        prog="czip",
        description="🔐 czip - ZIP ফাইলের পাসওয়ার্ড ক্র্যাক করার CLI টুল (শিক্ষামূলক উদ্দেশ্যে)",
        epilog="📌 উদাহরণ: czip -a -f test.zip -p wordlist.txt"
    )
    parser.add_argument("-a", action="store_true", help="ক্র্যাকিং শুরু করো")
    parser.add_argument("-f", type=str, help="ZIP ফাইলের ঠিকানা")
    parser.add_argument("-p", type=str, help="ওয়ার্ডলিস্ট ফাইল")

    args = parser.parse_args()

    if args.a and args.f and args.p:
        crack_zip(args.f, args.p)
    else:
        print("\n❗ ভুল ব্যবহার। সাহায্য দেখতে টাইপ করুন: czip -h")

if __name__ == "__main__":
    main()