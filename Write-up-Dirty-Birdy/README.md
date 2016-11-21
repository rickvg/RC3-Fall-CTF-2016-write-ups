#Write-up Dirty Birdy - RC3 Fall CTF 2016

Challenge text:
We had an employee that was up to no good. Our SIEM caught him uploading files to a website from our file server but we canceled the transmission. We currently have an image of home directory that we store on our server. Take a look for yourself on what he stole.
Download Link: https://drive.google.com/file/d/0Bw7N3lAmY5PCUWExQUJVZGVySXc/view?usp=sharing

This challenge provides the file dtrump.img. This is probably a filesystem as the challenge text mentions "image of home directory".
The command to check what filetype this file is:

> file dtrump.img

Execution of the command results in the output:
> dtrump.img: ISO 9660 CD-ROM filesystem data 'CDROM'

The file is a CD-ROM. To read the structure and files on the CD-ROM, the filesystem can be mounted. Mounting the file can be achieved by using the following command:

> mount dtrump.img /mnt/media

To browse to the files run command:
> cd /mnt/media

The folder structure of the CD-ROM:
```
root@knokknokwhoisdere:/mnt/media# ls
Desktop    Downloads         Music     Public    secretfiles  Videos
Documents  examples.desktop  Pictures  rr_moved  Templates
```

All folders appear to be empty, except for the folder "secretfiles", which contains the visible files:
* document.txt;
* README.md;
* Workbook1.xlsx.gpg.

#Analyzing the file contents
There are three visible files in folder "secretfiles". Command 'cat' is used to preview the contents of the files.

> document.txt: passowrd123

This file appears to be a nonsense TXT, but is definitely a file that might be needed later.

> README.md: # supersecret

This file appears to be a github README.md file as the content contains github syntaxis for header text (\#).

> Workbook1.xlsx.gpg: Contents are too long to paste here, but it appears to be a GPG-encrypted Excel-file

Command to decrypt this file:
```
root@knokknokwhoisdere:/mnt/media/secretfiles# gpg --decrypt Workbook1.xlsx.gpg gpg: encrypted with 1024-bit RSA key, ID 51B94612E22CB12D, created 2016-11-18
      "ThugG (lolz) <nope@gmail.com>"
gpg: decryption failed: No secret key
```
The secret key is still missing, which is required to decrypt Workbook1.xlsx.gpg. As all other folders seem to be empty, it is time to check the folders for hidden files with command:
> ls -al

The result is that folder secretfiles contains a hidden folder, named .git. This might contain a reference to a github repository containing the private key.

#Analyzing .git
The github page corresponding to the .git directory can be found in "config".

```
root@knokknokwhoisdere:/mnt/media/secretfiles/.git# cat config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://github.com/rc3club/supersecret.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

Let's clone this repository into a local folder:

```
root@knokknokwhoisdere:~/Desktop# git clone https://github.com/rc3club/supersecret.git
Cloning into 'supersecret'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
```

The folder indeed contains a file named private.key. This might be the key we are looking for, so import the file into the gpg secret keys list:
```
root@knokknokwhoisdere:~/Desktop/supersecret# gpg --import private.key
gpg: key BD8B144E8FFDF6D6: "ThugG (lolz) <nope@gmail.com>" not changed
gpg: key BD8B144E8FFDF6D6: secret key imported
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
```

The name of the secret key appears to be similar to the requested key, so let's try to decrypt the workbook again.

```
root@knokknokwhoisdere:~/Desktop# gpg --decrypt Workbook1.xlsx.gpg > Workbook.xlsx
gpg: encrypted with 1024-bit RSA key, ID 51B94612E22CB12D, created 2016-11-18
      "ThugG (lolz) <nope@gmail.com>"
```

The output is "Workbook.xlsx" which can be opened (if it is an Excel file) with software like Microsoft Office Excel/LibreOffice/OpenOffice.
The workbook, however, requests a password to open the Excel file.

#Opening the Excel file
We have two files remaining:
* README.md;
* document.txt

First try the text in document.txt: passowrd123. This didn't work. Second try the password in README.md: supersecret. This didn't work either. There could be a typo in the file document.txt.
At last try the text in document.txt (corrected): password123. This worked.

An Excel sheet opens containing the text: Equity Analysis of a Project, with numbers. In the lower left corner we can see there are two sheets.
After clicking on Sheet2, the formula input line contains the flag:
> RC3-2016-SNEAKY21
