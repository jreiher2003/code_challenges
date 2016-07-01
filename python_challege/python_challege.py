#2
import string
print string.lowercase

def convert(shift):
    statement = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    return ''.join(chr((ord(char) + shift) % 26) for char in statement)



strs='abcdefghijklmnopqrstuvwxyz'      #use a string like this, instead of ord() 
def shifttext(shift):
    # inp = statement = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    inp = "http://www.pythonchallenge.com/pc/def/map.html"
    data=[]
    for i in inp:                     #iterate over the text not some list
        if i.strip() and i in strs:                 # if the char is not a space ""  
            data.append(strs[(strs.index(i) + shift) % 26])    
        else:
            data.append(i)           #if space the simply append it to data
    output = ''.join(data)
    return output
        
print shifttext(2)
   
