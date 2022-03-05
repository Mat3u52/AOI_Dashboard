import tkinter as tk
from tkinter import ttk
import math
from tkinter import *
import os
import time
import xml.dom as minidom
import xml.dom.minidom
import subprocess
import matplotlib.pyplot as plt

lines = os.listdir('XML')
#10.231.161.222
#subprocess.call(r'net use m: \\10.231.161.222\XML /user:AOI_VITOX_INSTALL 123456789*a', shell=True)
#lines = os.listdir('\\\\10.231.161.222\XML')
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('AOI Dashboard')
        self.root.resizable(0, 0)
        #self.root.geometry('1100x80')
        self.root.iconbitmap('dashboard.ico')

        self.label = tk.Label(text="")
        self.label.grid(row=3, column=0)

        self.chartFlag = False

        self.L1 = Label(self.root, text="Line", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        #self.L2 = Label(self.root, text=f"{lines[2]}", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L2 = Label(self.root, text=f"{lines[0]}", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L1.grid(row=0, column=0)
        self.L2.grid(row=1, column=0)
        self.L3 = Label(self.root, text="Item", width=27, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L4 = tk.Label(self.root, text=f"", width=27, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L3.grid(row=0, column=1)
        self.L4.grid(row=1, column=1)
        self.L5 = Label(self.root, text="PCB Qty", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L6 = tk.Label(self.root, text=f"", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L5.grid(row=0, column=2)
        self.L6.grid(row=1, column=2)
        self.L7 = Label(self.root, text="Avg F/C", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L8 = tk.Label(self.root, text="", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L7.grid(row=0, column=3)
        self.L8.grid(row=1, column=3)
        self.L9 = Label(self.root, text="Max F/C", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L10 = tk.Label(self.root, text="", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L9.grid(row=0, column=4)
        self.L10.grid(row=1, column=4)
        self.L11 = Label(self.root, text="Ref. Des.", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L12 = tk.Label(self.root, text="", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L11.grid(row=0, column=5)
        self.L12.grid(row=1, column=5)

        self.L12.bind("<Button-1>", self.mouseClick)

        self.L13 = Label(self.root, text="Occurs", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L14 = tk.Label(self.root, text="", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L13.grid(row=0, column=6)
        self.L14.grid(row=1, column=6)
        self.L15 = Label(self.root, text="Percent", width=10, borderwidth=1, relief="solid", bg="#302928", font="Arial", fg="#FFFFFF", pady="2")
        self.L16 = tk.Label(self.root, text="", width=10, borderwidth=1, relief="solid", bg="#080808", font="Arial", fg="#FFFFFF", pady="2")
        self.L15.grid(row=0, column=7)
        self.L16.grid(row=1, column=7)

        self.updateClock()
        self.updateList()
        self.root.mainloop()

    def mouseClick(self, event):
        print("mouse clicked")
        self.chartFlag = True

    def updateClock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.updateClock)

    def updateList(self):
        xml0 = ""
        for date in os.listdir('XML/Gamma/Archive'):
            for xml0 in os.listdir('XML/Gamma/Archive/' + date):
                docs = xml.dom.minidom.parse('XML/Gamma/Archive/'+date+'/'+xml0)
        #for date in os.listdir('\\\\10.231.161.222\XML\GAMMA\Archive'):
        #    for xml0 in os.listdir('\\\\10.231.161.222\XML\GAMMA\Archive\\' + date):
        #        docs = xml.dom.minidom.parse('\\\\10.231.161.222\XML\GAMMA\Archive\\' + date + '\\' + xml0)
                progName = xml0.split('#')

                #print(progName[1])
            if (xml0 != ""):
                print("OK")

                filePathP = 'C:\_pythonProject\XML\gammaP.txt'
                filePathA = 'C:\_pythonProject\XML\gammaA.txt'
                filePathAvg = 'C:\_pythonProject\XML\gammaAvg.txt'
                filePathMax = 'C:\_pythonProject\XML\gammaMax.txt'
                filePathRD = 'C:\_pythonProject\XML\gammaRD.txt'
                #filePathP = '\\\\10.231.161.222\XML\gammaP.txt'
                #filePathA = '\\\\10.231.161.222\XML\gammaA.txt'
                #filePathAvg = '\\\\10.231.161.222\XML\gammaAvg.txt'
                #filePathMax = '\\\\10.231.161.222\XML\gammaMax.txt'
                #filePathRD = '\\\\10.231.161.222\XML\gammaRD.txt'
                f = open(filePathP, "r")
                self.prog = f.readlines()
                f.close()
                if self.prog[0] != progName[1]:
                    f = open(filePathP, "w")
                    f.write(f"{progName[1]}")
                    f.close()
                    f = open(filePathA, "w")
                    f.write(f"0")
                    f.close()
                    f = open(filePathAvg, "w")
                    f.write(f"0")
                    f.close()
                    f = open(filePathMax, "w")
                    f.write(f"0")
                    f.close()
                    f = open(filePathRD, "w")
                    f.write(f"")
                    f.close()

                self.L4.configure(text=f"{progName[1]}")

                f = open(filePathA, "r")
                self.fqty = f.readlines()
                f.close()
                self.qty = int(self.fqty[0])
                self.qty += 1

                f = open(filePathA, "w")
                f.write(f"{self.qty}")
                f.close()

                self.L6.configure(text=f"{self.qty}")

                #att = docs.getElementsByTagName("ns1:BoardTestXMLExport")
                att = docs.getElementsByTagName("ns1:RepairEventXML")
                #print("%d ns1:BoardTestXMLExport" % att.length)
                for i in att:
                    #print(i.getAttribute("numberOfDefects"))
                    #avg = i.getAttribute("numberOfDefects")
                    avg = i.getAttribute("numberOfFalseCalledComponents")

                f = open(filePathAvg, "r")
                self.avgF = f.readlines()
                f.close()
                self.avgToSave = int(self.avgF[0])
                self.avgToSave += int(avg)
                f = open(filePathAvg, "w")
                f.write(f"{self.avgToSave}")
                f.close()
                self.L8.configure(text=f"{round(self.avgToSave/self.qty)}")


                f = open(filePathMax, "r")
                self.maxF = f.readlines()
                f.close()
                self.max = int(self.maxF[0])
                if self.max < int(avg):
                    f = open(filePathMax, "w")
                    f.write(f"{avg}")
                    f.close()
                    self.L10.configure(text=f"{avg}")
                else:
                    self.L10.configure(text=f"{self.max}")

                if int(avg) > 0:
                    attRD = docs.getElementsByTagName("ns1:TestXML")
                    attRDFC = docs.getElementsByTagName("ns1:RepairActionXML")
                    # print("%d ns1:BoardTestXMLExport" % att.length)
                    f = open(filePathRD, "a")
                    iFC = 0
                    for iRD in attRD:
                        # print(i.getAttribute("numberOfDefects"))
                        #for iRDFC in attRDFC:
                        #print(attRDFC[iFC].getAttribute("repairStatus"))
                        if attRDFC[iFC].getAttribute("repairStatus") != "Repaired":
                            RDs = iRD.getAttribute("name")
                            #RDs = iRD.getAttribute("designator")
                            #print(RDs)
                            f.write(f"{RDs}\n")
                        iFC += 1
                    f.close()

                    f = open(filePathRD, "r")
                    self.readRD = f.readlines()
                    f.close()
                    tabRD = self.readRD
                    # print(tabRD)
                    # print(tabRD[0])
                    howMany = 0
                    for RD in tabRD:
                        # print(tabRD.count(RD))
                        # print(tabRD.count(RD))
                        if int(howMany) < int(tabRD.count(RD)):
                            howMany = int(tabRD.count(RD))
                            refDes = RD
                            # howMany = int(tabRD.count(RD))
                    # print(refDes)
                    self.L12.configure(text=f"{refDes.strip().upper()}")
                    self.L14.configure(text=f"{howMany}")
                    self.L16.configure(text=f"{round((howMany / self.qty) * 100)}%")
                else:
                    f = open(filePathRD, "r")
                    self.readRD = f.readlines()
                    f.close()
                    tabRD = self.readRD
                    #print(tabRD)
                    #print(tabRD[0])
                    if tabRD: # <----- sprawdzić czy plik z ref des nie jest pusty!!!
                        howMany = 0
                        for RD in tabRD:
                            #print(tabRD.count(RD))
                            #print(tabRD.count(RD))
                            if int(howMany) < int(tabRD.count(RD)):
                                howMany = int(tabRD.count(RD))
                                refDes = RD
                                #howMany = int(tabRD.count(RD))
                        #print(refDes)
                        self.L12.configure(text=f"{refDes.strip().upper()}")
                        self.L14.configure(text=f"{howMany}")
                        self.L16.configure(text=f"{round((howMany/self.qty)*100)}%")

                if self.chartFlag == True:
                    self.chartFlag = False
                    print(tabRD)
                    tabRDCount = []
                    for RDs in tabRD:
                        print(tabRD.count(RDs))
                        tabRDCount.append(tabRD.count(RDs))

                    x = ['one', 'two', 'tree']
                    y = [1, 2, 3]

                    plt.scatter(tabRD, tabRDCount, label='Number of false calls', color = 'g', marker= 'o')

                    plt.xlabel('Ref. Des.')
                    plt.ylabel('Occurs')
                    plt.title('Gamma')
                    plt.legend()
                    plt.show()

                os.remove('XML/Gamma/Archive/'+date+'/'+xml0)
                #os.remove('\\\\10.231.161.222\XML\GAMMA\Archive\\' + date + '\\' + xml0)
            else:
                print("NOK")
                filePathRD = 'C:\_pythonProject\XML\gammaRD.txt'
                f = open(filePathRD, "r")
                self.readRD = f.readlines()
                f.close()
                tabRD = self.readRD

                if tabRD:  # <----- sprawdzić czy plik z ref des nie jest pusty!!!
                    if self.chartFlag == True:
                        self.chartFlag = False
                        print(tabRD)
                        tabRDCount = []
                        for RDs in tabRD:
                            print(tabRD.count(RDs))
                            tabRDCount.append(tabRD.count(RDs))

                        x = ['one', 'two', 'tree']
                        y = [1, 2, 3]

                        plt.scatter(tabRD, tabRDCount, label='Number of false calls', color = 'g', marker= 'o')

                        plt.xlabel('Ref. Des.')
                        plt.ylabel('Occurs')
                        plt.title('Gamma')
                        plt.legend()
                        plt.show()
        self.root.after(1000, self.updateList)

app=App()