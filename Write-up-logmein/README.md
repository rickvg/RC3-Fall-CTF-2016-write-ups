#Write-up Logmein - RC3 Fall CTF 2016

Challenge text:
This has to be one of the safest and most secure login forms out there. Can you break it o 1337 h4x0r?
Download Link: https://drive.google.com/file/d/0Bw7N3lAmY5PCUVR4WGloSGlkUG8/view?usp=sharing

This challenge provides a file named "Logmein". To check what filetype this file is:
> file logmein

This command results in the output:
> logmein: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=c8f7fb137d9be24a19eb4f10efc29f7a421578a7, stripped

logmein is an ELF 64-bit executable. In order to analyze it or decompile the executable to pseudocode, the executable has to be opened in a 64-bit decompiler.
Currently, only "main" is the section of interest as this shows the main code to be executed. The output of main:

```
void __fastcall __noreturn main(__int64 a1, char **a2, char **a3)
{ 
  size_t v3; // rsi@1
  int i; // [sp+3Ch] [bp-54h]@3 
  char s[36]; // [sp+40h] [bp-50h]@1
  int v6; // [sp+64h] [bp-2Ch]@1 
  __int64 v7; // [sp+68h] [bp-28h]@1 
  char v8[8]; // [sp+70h] [bp-20h]@1 
  int v9; // [sp+8Ch] [bp-4h]@1e 

  v9 = 0;
  strcpy(v8, ":\"AL_RT^L*.?+6/46");
  v7 = 28537194573619560LL;
  v6 = 7;
  printf("Welcome to the RC3 secure password guesser.\n", a2, a3);
  printf("To continue, you must enter the correct password.\n");
  printf("Enter your guess: "); 
  __isoc99_scanf("%32s", s);
  v3 = strlen(s);
  if ( v3 < strlen(v8) )
    sub_4007C0();
  for ( i = 0; i < strlen(s); ++i ) 
  { 
    if ( i >= strlen(v8) )
      sub_4007C0();
    if ( s[i] != (char)(*((_BYTE *)&v7 + i % v6) ^ v8[i]) )
      sub_4007C0();
  } 
  sub_4007F0();
} 

```

#Cleaning the code
First, let's clean this up and make the code better understandable for everyone:

```
void __fastcall __noreturn main(__int64 a1, char **a2, char **a3)
{ 
  int i; 
  char s[36];
  int v6; 
  __int64 v7; 
  char v8[18]; 

  strcpy(v8, ":\"AL_RT^L*.?+6/46");
  v7 = 28537194573619560LL;
  printf("Welcome to the RC3 secure password guesser.\n");
  printf("To continue, you must enter the correct password.\n");
  printf("Enter your guess: "); 
  __isoc99_scanf("%32s", s);
  if ( strlen(s) < strlen(v8) )
    sub_4007C0();
  for ( i = 0; i < strlen(s); ++i ) 
  { 
    if ( i >= strlen(v8) )
      sub_4007C0();
    if ( s[i] != (char)((v7 >> (8*(i % 7))) & 0xff) ^ v8[i])
      sub_4007C0();
  } 
  sub_4007F0();
} 
```

The following operations have occured:
* Removed size_t v3. It's purpose in this code is to carry the string length of "s" (strlen(s)). This is not necessarily needed;
* Changed char v8[8] to char v8[18] as the actual size of the string copied to v8 is 18 (see strcpy);
* Removed v9. It serves no purpose in this code;
* Removed a2 and a3 from printf statement. This serves no purpose either;
* Removed v6 as it only carried value 7. This is inserted directly into the if-statement;
* Changed (char)(*((_BYTE *)&v7 + i % v6) ^ v8[i]) ) to (char)((v7 >> (8*(i % 7))) & 0xff) ^ v8[i]).

The last operation is based on the typedef of *((_BYTE *)&x + y, which can be found in the files of Hex-Rays decompiler.
It basically states *((_BYTE*)&(x)+y means: yth byte of value x. So the statement was replaced to get the (i%7)th byte of v7.

#Functions
The code contains two different functions sub_4007C0 and sub_4007F0.

sub_4007C0:
```
void __noreturn sub_4007C0()
{
  printf("Incorrect password!\n");
  exit(0);
}
```

This function basically prints "Incorrect password!" and exits the code, meaning the if-statements must be not true (remember !=).

sub_4007F0:
```
void __noreturn sub_4007F0()
{
  printf("You entered the correct password!\nGreat job!\n");
  exit(0);
}
```

This function basically prints "You entered the correct password! (newline) Great job!" and then exits the code. As the flag is not printed when the password is guessed correctly, the password is probably the flag.

#If-statements not true
In order to get to function sub_4007F0 all if-statements passed in "main" should return false. The code runs three if-statements.

First if-statement
```
if ( strlen(s) < strlen(v8) )
    sub_4007C0();
```

This if-statement defines, the string length of s (input string) may not be lower than the string length of v8.
The length of string s should remain above or equal to 17. Why 17? One character, the double quote, was escaped using a backslash. So, the backslash does not count as a character.

Second if-statement
```
if ( i >= strlen(v8) )
      sub_4007C0();
```

This if-statement defines that if i is bigger than the string length of v8, the program should be exited. This is correct, as the for-loop only runs until i is equal to strlen(v8) and then stops.
This means, our input string has to equal the exact length of 17 characters.

Third if-statement
```
if ( s[i] != (char)((v7 >> (8*(i % 7))) & 0xff) ^ v8[i])
      sub_4007C0();
```

This if-statement defines that if a specific character in our input string is not equal to the XOR-ed value, the program should be exited.
From here we know, the XOR-value is equal to the password. In order to find the flag, we need to find the result of the XOR-statement.
In order to do this, I created a python script, which is described in the next section.

#Python
The python script is a rewritten piece of code based on the pseudocode generated from logmein. The python script can be found in this repository as xorops.py

Executing this python script results in the flag:
> RC3-2016-XORISGUD 
