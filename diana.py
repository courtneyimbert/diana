#!/usr/bin/python
#
# Diana Cryptosystem Encoder / Decoder
# Courtney Imbert, courtneyimbert@gmail.com
#
# This short program is a python implementation of the polyalphabetic, symmetric Diana Cryptosystem, in use by U.S. Special Forces during the Vietnam War. It encrypts/decrypts strings using a One Time Pad (OTP) or key. The algorithm is similar to a Vernam or Vigenere cipher.
# For more information on the Diana Cryptosystem, read http://www.blogbyben.com/2014/12/trigraphs-diana-pads-and-zombies.html
# 
# This program is for personal hobbyist and puzzle use. It is NOT a secure method for encrypting data. I wrote it for fun.

import sys,string, argparse

def diana(key,plaintext):
    reverseA = string.ascii_lowercase[::-1]
    count=0
    lookup=''
    for p in plaintext:
        if (p in string.ascii_lowercase) or (p in string.ascii_uppercase):
            kdeep = ord(key[count]) - 97
            shiftA=reverseA[kdeep:] + reverseA[:kdeep]
            pdeep=ord(p.lower()) - 97
            result=shiftA[pdeep]
            if count==len(key)-1: 
                count=0
            else:
                count +=1
        else:
            result=p
        lookup=lookup+result
    return lookup

def sanitizeKey(k):
    cleanKey=""
    for i in k:
        if (i == " "):
            pass
        elif (i not in string.ascii_lowercase) and (i not in string.ascii_uppercase):
            print "Key must contain only ASCII letters."
            exit()
        else:
            cleanKey=cleanKey+i.lower()
    return cleanKey

def main(argv):
    otp = ''
    encoded = ''
    parser=argparse.ArgumentParser(description="Diana Cryptosystem Program by Courtney Imbert, courtneyimbert@gmail.com")
    parser.add_argument('-k',action="store",dest="key", help="key or One Time Pad (OTP)",default="",required=True)
    parser.add_argument('-i',action="store",dest="plaintext", required=True,help="plaintext. Use quotes around a string, or specify a file path.",default="")
    parser.add_argument('--nospaces',action='store_true',dest='nospaces',default=False,help='Remove spaces from the output text to thwart freq analysis')
    parser.add_argument('--upper',action='store_true',dest='upper',default=False,help='Make the output upper case')
    input=parser.parse_args()
    if input.key=="" or input.plaintext=="":
        print "Usage: diana.py -k <key> -i <plaintext or encrypted text>"
        print "Example: diana.py -k ABCDE -i hello"
        exit()
    sanitizedKey = sanitizeKey(input.key)
    try:
        with open(input.plaintext) as f:
            lines = f.read()
            output=diana(sanitizedKey,lines)
    except:
            output=diana(sanitizedKey,input.plaintext)
    if input.nospaces:
        output=output.replace(" ","")
    if input.upper:
        output=output.upper()
    print output

if __name__ == "__main__":
    main(sys.argv[1:])
