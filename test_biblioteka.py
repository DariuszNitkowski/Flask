import biblioteka
from biblioteka import app
import pytest
import json
from flask import Flask





@pytest.fixture
def dane():
    with open("baza.txt") as json_file:
        dane=json.load(json_file)
        dane=dane["items"]
        return dane


  
def test_formatowanie(dane):
    lista_bib=[]
    assert biblioteka.formatowanie(lista_bib,[{"":""}])==[]
    assert biblioteka.formatowanie(lista_bib,[{"Aa":10}])==[]
    assert len(biblioteka.formatowanie(lista_bib,[{"volumeInfo":{"title":""}},{"volumeInfo":{"":""}}]))==1
    
    
    
    

def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200

    #(autor, jezyk, isbn, dataod, datado,stron, okladka)

def test_walidator():
    result=biblioteka.walidator("!Darek", "ES", "123", "2010-10-10", "200-10-10", "200", "")
    assert len(result)==3
    result=biblioteka.walidator("Darek", "en", "1234567890", "1990-10-10", "2015-10-10", "215","")
    assert len(result)==0
    result=biblioteka.walidator("1D!arek", "P1", "12s34567890", "2990-10-10", "2015-10-10", "215,1","")
    assert len(result)==5


