#!/usr/bin/python3
import json

f = open("/home/liam/sail-riscv/json.out")
g = json.load(f)


for i in g["instructions"]:
        mnemonic = i["mnemonic"].upper().replace('.' , '_')
        c = ""
        for k in i["fields"]:
            if k["field"].startswith("0b"):
                c = c + ('1' * k["size"])
                
            else:
                c = c + ('0' * k["size"])
                
        print("#define MASK_" + mnemonic + " 0x" + hex(int(c, 2)).removeprefix('0x').zfill(8))
        
        c = ""
        for k in i["fields"]:
            if k["field"].startswith("0b"):
                d = k["field"]
                d = d.removeprefix('0b')
                c = c + d
                
            else:
                c = c + ('0' * k["size"])
                
        print("#define MATCH_" + mnemonic + " 0x" + hex(int(c, 2)).removeprefix('0x').zfill(8))
    
# if len(i["operands"]) == 0:
# print(i["mnemonic"])
# print(len(g["instructions"]))
# print(json.dumps(g, sort_keys=True,indent=4))
