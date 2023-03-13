
from pickle import LIST

import random

def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[] 
    file=open(f,"r",encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        riik_pealinn[k]=v 
        pealinn_riik[v]=k 
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid 

def Lisa_failisse(fail:str,riik:str, pealinn:str):
    f=open(fail,"a",encoding="utf-8-sig")
    f.write(riik+"-"+pealinn+"\n")
    f.close()
def muuda_riik(fail:str, riikpealinn:dict,pealinnriik:dict):
        x=input("vana riik: ")
        if x in riikpealinn:
            y=input("uus riik: ")
            k=input(f"uus pealinn: ")

            vana_pealinn = riikpealinn[x]

            riikpealinn.pop(x)
            riikpealinn[y]=k

            pealinnriik.pop(vana_pealinn)
            pealinnriik[k]=y

            f=open(fail,"w",encoding="utf-8-sig")
            for riik in riikpealinn:
                f.write(riik+"-"+riikpealinn[riik]+"\n")

def game(riik_pealinn:dict):

    while True:
        riik = random.choice(list(riik_pealinn.keys()))
        kasutaja_pealinn=input(f"sisestage riigi {riik} pealinn : ")

        if riik_pealinn[riik] == kasutaja_pealinn:
            print("oige")
        else:
            print(f"vale. oige pealinn on {riik_pealinn[riik]}")
            break


riik_pealinn, pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")

while True:
    v=int(input(f"1-otsi riik/pealinn\n2-lisa\n3-muuda\n4-mang"))
    if v==1:

        suund = int(input("1-riik_pealinn\n2-pealinn_riik"))
        if suund == 1:
            riik=input("sissesta riik: ")
            if riik in riik_pealinn:
                print(f"pealinn on {riik_pealinn[riik]}")
            else:
                print("riik ei ole leitud")
        else:
            pealinn=input("sissesta pealinn: ")
            if pealinn in pealinn_riik:
                print(f"riik on {pealinn_riik[pealinn]}")
            else:
                print("pealinn ei ole leitud")

    elif v==2:

        uusriik=input("lisa riik: ")
        uuspealinn=input("lisa pealinn: ")

        riik_pealinn[uusriik] = uuspealinn
        pealinn_riik[uuspealinn] = uusriik
        riigid.append(uusriik) 

        Lisa_failisse("riigid_pealinnad.txt",uusriik,uuspealinn)
    elif v==3:
        muuda_riik("riigid_pealinnad.txt",riik_pealinn, pealinn_riik)
    elif v==4:
        game(riik_pealinn)
