# Write-up SALAD - RC3 Fall CTF 2016

Challenge text: <br/>
“The fault, dear Brutus, is not in our stars, but in ourselves.” (I.ii.141) Julius Caesar in William Shakespeare’s Julius Caesar
Cipher Text: 7sj-ighm-742q3w4t

This challenge provides a Cipher Text, where every character was rotated by 20 positions using a custom alphabet. The custom alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.
The challenge was solved using caesar.py, created by rickvg, which can be found in this repository.

Usage:
> python caesar.py [integer|all] [input file]

In this case, I removed the dashes (-) from the cipher text as they were not part of the alphabet and used the command:
> python caesar.py all cipher

Output of the script: <br/>
>ROT 1: 8TKJHIN853R4X5U <br/>
>ROT 2: 9ULKIJO964S5Y6V <br/>
>ROT 3: AVMLJKPA75T6Z7W <br/>
>ROT 4: BWNMKLQB86U708X <br/>
>ROT 5: CXONLMRC97V819Y <br/>
>ROT 6: DYPOMNSDA8W92AZ <br/>
>ROT 7: EZQPNOTEB9XA3B0 <br/>
>ROT 8: F0RQOPUFCAYB4C1 <br/>
>ROT 9: G1SRPQVGDBZC5D2 <br/>
>ROT 10: H2TSQRWHEC0D6E3 <br/>
>ROT 11: I3UTRSXIFD1E7F4 <br/>
>ROT 12: J4VUSTYJGE2F8G5 <br/>
>ROT 13: K5WVTUZKHF3G9H6 <br/>
>ROT 14: L6XWUV0LIG4HAI7 <br/>
>ROT 15: M7YXVW1MJH5IBJ8 <br/>
>ROT 16: N8ZYWX2NKI6JCK9 <br/>
>ROT 17: O90ZXY3OLJ7KDLA <br/>
>ROT 18: PA10YZ4PMK8LEMB <br/>
>ROT 19: QB21Z05QNL9MFNC <br/>
>ROT 20: RC32016ROMANGOD <br/>
>ROT 21: SD43127SPNBOHPE <br/>
>ROT 22: TE54238TQOCPIQF <br/>
>ROT 23: UF65349URPDQJRG <br/>
>ROT 24: VG7645AVSQERKSH <br/>
>ROT 25: WH8756BWTRFSLTI <br/>
>ROT 26: XI9867CXUSGTMUJ <br/>
>ROT 27: YJA978DYVTHUNVK <br/>
>ROT 28: ZKBA89EZWUIVOWL <br/>
>ROT 29: 0LCB9AF0XVJWPXM <br/>
>ROT 30: 1MDCABG1YWKXQYN <br/>
>ROT 31: 2NEDBCH2ZXLYRZO <br/>
>ROT 32: 3OFECDI30YMZS0P <br/>
>ROT 33: 4PGFDEJ41ZN0T1Q <br/>
>ROT 34: 5QHGEFK520O1U2R <br/>
>ROT 35: 6RIHFGL631P2V3S <br/>


Flag:
> RC3-2016-ROMANGOD
