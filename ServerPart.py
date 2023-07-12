import json, requests, sqlite3, logging, os.path, xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from datetime import *
import time as t
import feedparser 
#LinkZone
CBRLink = "https://www.cbr-xml-daily.ru/daily_json.js"
ECBLink = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml" 
NBGLink = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date="  + str(date.today()) # Дата должна быть в формате 2022-09-16
BOCLink = "https://www.bankofcanada.ca/valet/observations/FXAUDCAD,FXBRLCAD,FXCNYCAD,FXEURCAD,FXHKDCAD,FXINRCAD,FXIDRCAD,FXJPYCAD,FXMYRCAD,FXMXNCAD,FXNZDCAD,FXNOKCAD,FXPENCAD,FXRUBCAD,FXSARCAD,FXSGDCAD,FXZARCAD,FXKRWCAD,FXSEKCAD,FXCHFCAD,FXTWDCAD,FXTHBCAD,FXTRYCAD,FXGBPCAD,FXUSDCAD,FXVNDCAD/json?start_date=%s&end_date=%s"%(date.today()-timedelta(days=5),date.today())
HNBLink = "https://api.hnb.hr/tecajn/v2"
NBRBLink= "https://www.nbrb.by/api/exrates/rates?periodicity=0" 
SNBLink = "https://www.snb.ch/selector/en/mmr/exfeed/rss"

# Настройка Логгера
logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

def SQLExecute(Command):
    db = sqlite3.connect('currencies.db')
    Cursor = db.cursor()
    Cursor.execute(Command)
    db.commit()
    db.close()



def CreateTable(TableName):
    if TableName == "CBRData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            ID text,
            NumCode integer,
            CharCode text,
            Name text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)
        
    elif TableName == "ECBData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            CharCode text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)

    elif TableName == "NBGData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            CharCode text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)
        
    elif TableName == "BOCData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            CharCode text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)

    elif TableName == "HNBData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            CharCode text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)

    elif TableName == "NBRBData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            CharCode text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)
        
    elif TableName == "SNBData":
        Command = ("""
            CREATE TABLE IF NOT EXISTS %s(
            CharCode text,
            Value float,
            UpdateDate datetime
            )""")%TableName
        SQLExecute(Command)
        
    else: print("Данной таблицы не найдено")
    logging.debug(TableName + " создана.")   



def UpdateTable(TableName):
    
    if TableName == "CBRData":
        Response = requests.get(CBRLink)
        JsonData = json.loads(Response.text)
        CurList = JsonData['Valute']
        SQLExecute("DELETE FROM %s"%TableName)
        for i in CurList:
            Command = "INSERT INTO %s  VALUES('%s',%d,'%s','%s',%f,'%s')"%(TableName,str(JsonData['Valute'][i]['ID']),int((JsonData['Valute'][i]['NumCode'])),i, JsonData['Valute'][i]['Name'] ,(JsonData['Valute'][i]['Value']/JsonData['Valute'][i]['Nominal']),datetime.now())
            SQLExecute(Command)
            
    elif TableName == "ECBData":
        Response = requests.get(ECBLink)
        soup = BeautifulSoup(Response.text, 'xml')
        SQLExecute("DELETE FROM %s"%TableName)        
        for i in soup.find_all(currency=True):
            Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,i.attrs['currency'],float(i.attrs['rate']),datetime.now())
            SQLExecute(Command)
            
    elif TableName == "NBGData":
        Response = requests.get(NBGLink)
        JsonData = json.loads(Response.text)
        CurList = JsonData[0]["currencies"]
        SQLExecute("DELETE FROM %s"%TableName)        
        for i in CurList:
            Value = i['rate']/i['quantity']
            Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,i['code'],float(Value),datetime.now())
            SQLExecute(Command)
            
    elif TableName == "BOCData":
        Response = requests.get(BOCLink)
        JsonData = json.loads(Response.text)    
        CurList = JsonData['observations'][len(JsonData['observations'])-1]
        CurList.pop("d") #Починить этот костыль
        SQLExecute("DELETE FROM %s"%TableName)         
        for i in CurList:
            CharCode = i[2:5]
            Value = str(CurList[i])[7:-2]
            Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,CharCode,float(Value),datetime.now())
            SQLExecute(Command)
            
    elif TableName == "HNBData":
        Response = requests.get(HNBLink)
        JsonData = json.loads(Response.text)
        SQLExecute("DELETE FROM %s"%TableName) 
        for i in JsonData:
            Value = float(i["srednji_tecaj"].replace(',', '.'))/i["jedinica"]
            Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,i["valuta"],Value,datetime.now())
            SQLExecute(Command)
            
    elif TableName == "NBRBData":
        Response = requests.get(NBRBLink)
        JsonData = json.loads(Response.text)
        SQLExecute("DELETE FROM %s"%TableName)
        for i in JsonData:
            Value = float(i["Cur_OfficialRate"])/i["Cur_Scale"]
            Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,i["Cur_Abbreviation"],Value,datetime.now())
            SQLExecute(Command)
            
    elif TableName == "SNBData":
        JsonData = feedparser.parse(SNBLink)
        SQLExecute("DELETE FROM %s"%TableName)
        for i in range(3):
            Value = JsonData['entries'][len(JsonData['entries'])-4+i]['title_detail']['value'][4:10]
            CharCode = JsonData['entries'][len(JsonData['entries'])-4+i]['title_detail']['value'][19:22]
            Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,CharCode,float(Value),datetime.now())
            SQLExecute(Command)
        Value = float(JsonData['entries'][len(JsonData['entries'])-1]['title_detail']['value'][4:10])/100
        CharCode = JsonData['entries'][len(JsonData['entries'])-1]['title_detail']['value'][21:24]
        Command = "INSERT INTO %s  VALUES('%s',%f,'%s')"%(TableName,CharCode,float(Value),datetime.now())
        SQLExecute(Command)

    
    else: print("Данной таблицы не найдено")
    logging.debug(TableName + " обновлена.")   

def CreateTables():
    CreateTable("ECBData")
    CreateTable("CBRData")
    CreateTable("NBGData")
    CreateTable("BOCData")
    CreateTable("HNBData")
    CreateTable("NBRBData")
    CreateTable("SNBData")
    logging.debug("Все таблицы существуют.")


def StartUpdate():
    while(True):
        UpdateTable("CBRData")
        UpdateTable("ECBData")
        UpdateTable("NBGData")
        UpdateTable("BOCData")
        #UpdateTable("HNBData")
        UpdateTable("NBRBData")
        UpdateTable("SNBData")
        logging.debug("Все таблицы обновлены.")
        t.sleep(180)


print("Запуск успешен")
CreateTables()
StartUpdate()







