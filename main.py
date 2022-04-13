from collections import defaultdict
import json
import time
import tqdm
from matplotlib.pyplot import table
from utils import *
from config import get_config
from multiprocessing import Process, Manager

Config=get_config()

def generate(index,all_table):
    table={}
    if index==0:
        for _ in tqdm(range(Config.ROWS)):
            password=generate_password()
            start=password
            for i in range(Config.COLS):
                hash=H(password)
                password=R(hash,i)
            table[password].add(start)
    else:
        for _ in range(Config.ROWS):
            password=generate_password()
            start=password
            for i in range(Config.COLS):
                hash=H(password)
                password=R(hash,i)            
            table[password].add(start)

    all_table[index]=table

def generate_table():
    rainbow_table=defaultdict(set)
    startTime = time.time()
    with Manager() as m:
        threads = []
        all_table = m.dict()
        for i in range(Config.CORES):
            p = Process(target=generate,args=(i, all_table))
            threads.append(p)
        for p in threads:
            p.start()
        for p in threads:
            p.join()
        for i in range(Config.CORES):
            t=all_table[i]
            init_rows=len(rainbow_table)
            for j in t.keys():
                rainbow_table[j]=rainbow_table[j] | t[j]
            ##测试
            if i == len(all_table) - 1:
                print('repetition rate\t:\t%.2f' % (100 - 100 * ((len(rainbow_table) - init_rows) / Config.ROWS)))
                print('total rows\t:\t', len(rainbow_table))
    cost_time=(time.time()-startTime)
    print("Done in {} mins".format(int(cost_time)/60))
    temp=json.dumps(rainbow_table)
    f=open("rainbow_table.json","w")
    f.write(temp)
    f.close()

def crack(password):
    return ""

if __name__ =="__main__":
    generate_table()
    crack()