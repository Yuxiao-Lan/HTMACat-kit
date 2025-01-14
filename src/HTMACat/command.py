import os
from HTMACat.model.Construct_adsorption import *
from HTMACat.model.Construct_Coadsorption import *
from pathlib import *
import argparse

def ads():
    parser = argparse.ArgumentParser(description='High-throughput single adsorption modeling')
    parser.add_argument('-i', '--inputdir', type=str, default="./", help="The folder path of input files")
    args = parser.parse_args()
    wordir = Path(args.inputdir).resolve()
    Path_Info = str(wordir / 'StrucInfo')
    Model =  str(wordir / 'Model')
    with open(Path_Info,'r+') as f:
        for i,item in enumerate(f):
            Construct_adsorption(item,Model)


def coads():
    parser = argparse.ArgumentParser(description='High-throughput co-adsorption modeling')
    parser.add_argument('-i', '--inputdir', type=str, default="./", help="The folder path of input files")
    args = parser.parse_args()
    wordir = Path(args.inputdir).resolve()
    Path_Info = str(wordir / 'StrucInfo')
    Model =  str(wordir / 'Model')
    #spec_ads,spec_ads_stable=get_site_stable(Efile,Ecut=-0.1)
    #spec_ads_stable={'NH3':[1,2],'NH2':[2],'NH':[2,4],'N':[2,4],'O':[2,4],'OH':[2,4],'NO':[2,4],'H2O':[1],'H':[2,4]}
    spec_ads_stable={'NH3':[1],'NH2':[2],'NH':[2,4],'N':[2,4],'O':[2,4],'OH':[2,4],'NO':[2,4],'H2O':[1],'H':[2,4]}
    #spec_ads_stable={'NH2':[2],'NH':[3],'NO':[3],'NH3':[1],'N':[3],'O':[3],'OH':[3]} 
    Construct_coadsorption(Path_Info,Model,spec_ads_stable)
