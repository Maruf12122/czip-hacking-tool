# 🔓 czip

**czip** হলো একটি কমান্ড-লাইন টুল, যা ZIP ফাইলের পাসওয়ার্ড ক্র্যাক করতে ব্যবহার করা হয়।  
এটি শুধুমাত্র **শিক্ষামূলক উদ্দেশ্যে** তৈরি করা হয়েছে। 🚫

---

## ✨ ফিচার
- 🔑 AES এনক্রিপ্টেড ZIP ফাইল সাপোর্ট  
- 📖 ওয়ার্ডলিস্ট দিয়ে ব্রুটফোর্স চেষ্টা  
- 👀 প্রতিটি চেষ্টা করা পাসওয়ার্ড দেখা যাবে  
- ✅ পাসওয়ার্ড পেলে ফাইল আনজিপ হবে  

---

## 📦 ইনস্টলেশন
Python 3 ইন্সটল করা থাকতে হবে। এরপর নিচের কমান্ড রান করো:  

```bash
pip install pyzipper pyfiglet
```

---

## ⬇️ Kali Linux-এ ডাউনলোড (GitHub থেকে)

1. প্রথমে git ইন্সটল আছে কিনা চেক করো:
   ```bash
   git --version
   ```
   না থাকলে ইন্সটল করো:
   ```bash
   sudo apt update && sudo apt install git -y
   ```

2. এখন GitHub থেকে প্রোজেক্ট ক্লোন করো:
   ```bash
   git clone https://github.com/username/czip.git
   ```

3. ডিরেক্টরিতে প্রবেশ করো:
   ```bash
   cd czip
   ```

4. এখন রান করতে পারো:
   ```bash
   python czip.py -a -f test.zip -p wordlist.txt
   ```

---

## 🌍 গ্লোবাল সেটআপ

যদি `czip` কে সরাসরি টার্মিনালে কমান্ড হিসেবে চালাতে চাও:

```bash
chmod +x czip.py
sudo mv czip.py /usr/local/bin/czip
```

তারপর ব্যবহার করতে পারো:
```bash
czip -a -f test.zip -p wordlist.txt
```

---

## 🚀 ব্যবহার
```bash
czip -a -f <zip_file> -p <wordlist>
```

### উদাহরণ
```bash
czip -a -f test.zip -p wordlist.txt
```

---

## ⚠️ সতর্কবার্তা
এই টুল শুধুমাত্র **শিক্ষামূলক এবং ব্যক্তিগত পরীক্ষার জন্য**।  
অন্যের অনুমতি ছাড়া ZIP ফাইল ক্র্যাক করা আইনত দণ্ডনীয় অপরাধ।  

---
