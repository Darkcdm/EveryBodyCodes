findWords = "TSWYSEWETR,DS,YZJGEFDZSS,LXHOMVKVYJ,CILS,HHXMOZWKPY,UW,OC,G,MR,YIYWHHQKGC,VJII,IZ,GTBK,M,ERHWVTBTNZ,GCS,VDVC,ZIH,RX,VIZ,PVYX,KFSU,GN,VVG,QD,VWRM,JMXPEIYXWB,BBI,ZZFG,XB,E,MXU,JOAUILKSGG,YNC,MIXR,XY,OO,UAQAROQMRV,OW,CNC,L,XGQ,RPHW,WOW,U,AZPLAZMHUN,IPM"
#findWords = "THE,OWE,MES,ROD,HER"
invertedWords = findWords[::-1]


with open('input', 'r') as file:
    input = file.read()

findWords = findWords.split(",")
invertedWords = invertedWords.split(",")
count = 0

for line in input.split("\n"):
    findline = line
    for word in findWords:
        index = 0
        while index != -1:
            index = findline.find(word, index)
            if index >= 0:
                line = line[:index] + line[index:index+len(word)].lower() + line[index+len(word):]
                index += 1

    for word in invertedWords:
        index = 0
        while index != -1:
            index = findline.find(word, index)
            if index >= 0:
                line = line[:index] + line[index:index+len(word)].lower() + line[index+len(word):]
                index += 1


    print(line)
    count += sum(1 for c in line if c.islower())

print(count)