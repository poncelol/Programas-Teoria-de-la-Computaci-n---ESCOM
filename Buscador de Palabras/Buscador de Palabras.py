from graphviz import Digraph
import pandas as pd
import matplotlib.pyplot as plt

estados_DFA = {
    'q0':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q1':{'a':'q1','b':'q0','c':'q4','d':'q0','e':'q0','f':'q0','g':'q5','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q2':{'a':'q6','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q3':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q7','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q8','ó':'q0','ú':'q0'},
    'q4':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q9','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q10','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q5':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q11','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q6':{'a':'q1','b':'q0','c':'q12','d':'q0','e':'q0','f':'q0','g':'q5','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q7':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q13','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q8':{'a':'q1','b':'q0','c':'q14','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q9':{'a':'q1','b':'q0','c':'q15','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q10':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q16','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q11':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q17','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q12':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q9','f':'q0','g':'q0','h':'q18','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q10','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q13':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q19','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q14':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q20','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q15':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q21','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q16':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q22','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q17':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q23','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q18':{'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q24','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q19': {'a':'q25','b':'q0','c':'q0','d':'q0','e':'q26','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q20': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q27','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q21': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q28','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q22': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q23': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q29','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q24': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q30','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q25': {'a':'q1','b':'q0','c':'q31','d':'q0','e':'q0','f':'q0','g':'q5','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q26': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q32','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q27': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q33','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q28': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q29': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q34','ú':'q0'},
    'q30': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q35','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q31': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q9','f':'q0','g':'q0','h':'q0','i':'q36','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q10','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q32': {'a':'q1','b':'q0','c':'q37','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q33': {'a':'q38','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q34': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q39','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q35': {'a':'q40','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q36': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q41','ú':'q0'},
    'q37': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q42','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q38': {'a':'q1','b':'q0','c':'q43','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q39': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q40': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q41': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q44','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q42': {'a':'q45','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q43': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q18','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q44': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'},
    'q45': {'a':'q1','b':'q0','c':'q0','d':'q0','e':'q0','f':'q0','g':'q0','h':'q0','i':'q0','j':'q0','k':'q0','l':'q0','m':'q2','n':'q0','ñ':'q0','o':'q0','p':'q0','q':'q0','r':'q0','s':'q0','t':'q0','u':'q0','v':'q3','w':'q0','x':'q0','y':'q0','z':'q0','á':'q0','é':'q0','í':'q0','ó':'q0','ú':'q0'}
}

def analizar_archivo(archivo_texto):
    estados_finales = {
        'q22': {
            'palabra': 'acoso',
            'longitud': 5,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        },
        'q28': {
            'palabra': 'acecho',
            'longitud': 6,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        },
        'q38': {
            'palabra': 'víctima',
            'longitud': 7,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        },
        'q39': {
            'palabra': 'agresión',
            'longitud': 8,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        },
        'q40': {
            'palabra': 'machista',
            'longitud': 8,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        },
        'q44': {
            'palabra': 'violación',
            'longitud': 9,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        },
        'q45': {
            'palabra': 'violencia',
            'longitud': 9,  # Longitud predefinida de la palabra
            'ocurrencias': 0,
            'ubicaciones': []
        }
    }

    estado_actual = 'q0'
    registro_estados_DFA = []
    with open(archivo_texto, "r", encoding="utf-8") as archivo:
        linea_actual = 0
        for linea in archivo:
            columna_actual = 1
            linea_actual += 1
            for caracter in linea:
                columna_actual += 1
                estado_anterior = estado_actual
                estado_actual = estados_DFA.get(estado_actual, {}).get(caracter, 'q0')
                if estado_actual in estados_finales:
                    estados_finales[estado_actual]['ocurrencias'] += 1
                    longitud_palabra = estados_finales[estado_actual]['longitud']
                    estados_finales[estado_actual]['ubicaciones'].append((columna_actual - longitud_palabra, linea_actual))
                registro_estados_DFA.append((estado_anterior, caracter, estado_actual))

    return estados_finales, registro_estados_DFA


def exportar_resultados(archivo_salida, estados_finales):
    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write("Resultados del análisis:\n")
        for estado, detalles in estados_finales.items():
            archivo.write(f"Palabra: {detalles['palabra']}\n")
            archivo.write(f"  Ocurrencias: {detalles['ocurrencias']}\n")
            archivo.write(f"  Ubicaciones: {detalles['ubicaciones']}\n\n")

def exportar_estados_DFA(archivo_estados_DFA, registro):
    with open(archivo_estados_DFA, 'w', encoding='utf-8') as archivo:
        archivo.write("Historial de estados_DFA:\n")
        for transicion in registro:
            estado_inicial, simbolo, estado_final = transicion
            archivo.write(f"δ({estado_inicial}, '{simbolo}') -> {estado_final}\n")



# Definir los estados y transiciones
nfa = {
    1: {'a': [2, 7, 13], 'v': [21, 28, 37], 'm': [46], 'Σ': [1]},
    2: {'c': [3]},
    3: {'o': [4]},
    4: {'s': [5]},
    5: {'o': [6]},
    7: {'c': [8]},
    8: {'e': [9]},
    9: {'c': [10]},
    10: {'h': [11]},
    11: {'o': [12]},
    13: {'g': [14]},
    14: {'r': [15]},
    15: {'e': [16]},
    16: {'s': [17]},
    17: {'i': [18]},
    18: {'o': [19]},
    19: {'n': [20]},
    21: {'i': [22]},
    22: {'c': [23]},
    23: {'t': [24]},
    24: {'i': [25]},
    25: {'m': [26]},
    26: {'a': [27]},
    28: {'i': [29]},
    29: {'o': [30]},
    30: {'l': [31]},
    31: {'a': [32]},
    32: {'c': [33]},
    33: {'i': [34]},
    34: {'o': [35]},
    35: {'n': [36]},
    37: {'i': [38]},
    38: {'o': [39]},
    39: {'l': [40]},
    40: {'e': [41]},
    41: {'n': [42]},
    42: {'c': [43]},
    43: {'i': [44]},
    44: {'a': [45]}, 
    46: {'a': [47]},
    47: {'c': [48]},
    48: {'h': [49]},
    49: {'i': [50]},
    50: {'s': [51]},
    51: {'t': [52]},
    52: {'a': [53]},
}
def create_nfa_graph(nfa, initial_state, accepting_states, output_file='nfa_graph'):
    # Crear el gráfico
    nfa_graph = Digraph(format='png', engine='dot')

    # Configuración de dirección izquierda a derecha
    nfa_graph.attr(rankdir='LR')
    nfa_graph.attr('node', shape='circle')

    # Agregar el estado inicial
    nfa_graph.node("", shape="none")
    nfa_graph.edge("", str(initial_state))

    # Agregar nodos y transiciones
    for state, transitions in nfa.items():
        for symbol, next_states in transitions.items():
            for next_state in next_states:
                nfa_graph.edge(str(state), str(next_state), label=symbol)

    # Agregar estados finales
    for accepting_state in accepting_states:
        nfa_graph.node(str(accepting_state), shape='doublecircle')

    # Guardar y renderizar el gráfico
    nfa_graph.render(output_file)
initial_state = 1
accepting_states = {6, 12, 20, 27, 36, 45, 53}

def generar_grafo():
    estados_finales = {'q22', 'q28', 'q38', 'q39', 'q40', 'q44', 'q45'}
    grafo_DFA = Digraph(format='png')
    for estado, trans in estados_DFA.items():
        if estado in estados_finales:
            grafo_DFA.node(estado, estado, shape='doublecircle')
        else:
            grafo_DFA.node(estado, estado, shape='circle')
        for simbolo, estado_destino in trans.items():
            grafo_DFA.edge(estado, estado_destino, label=simbolo)
    grafo_DFA.render('grafo_DFA')
    
def guardar_tabla_estados_DFA(estados_DFA, nombre_archivo='tabla_estados_DFA.png'):
    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(estados_DFA).T

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(15, 8))  # Ajusta el tamaño de la figura

    # Dibujar la tabla
    ax.axis('off')  # Eliminar los ejes
    tabla = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        rowLabels=df.index,
        cellLoc='center',
        loc='center',
    )

    # Ajustar el tamaño de la fuente
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)
    tabla.auto_set_column_width(col=list(range(len(df.columns))))

    # Guardar la tabla como PNG
    plt.savefig(nombre_archivo, bbox_inches='tight', dpi=300)
    print(f"Tabla guardada como '{nombre_archivo}'.")

def procesar_datos():
    archivo_entrada = 'TextoPrueba.txt'
    archivo_salida_resultados = 'resultados.txt'
    archivo_salida_estados_DFA = 'estados_DFA.txt'

    print("Analizando archivo de texto usando el DFA...")
    estados_finales, registro_estados_DFA = analizar_archivo(archivo_entrada)

    exportar_resultados(archivo_salida_resultados, estados_finales)
    print(f"Resultados exportados a {archivo_salida_resultados}")
    
    guardar_tabla_estados_DFA(estados_DFA)
    print("Tabla de Estados de DFA generado y guardado.")
    
    create_nfa_graph(nfa, initial_state, accepting_states)
    print("Grafo del NFA generado y guardado.")

    exportar_estados_DFA(archivo_salida_estados_DFA, registro_estados_DFA)
    print(f"Historial de estados_DFA exportado a {archivo_salida_estados_DFA}")
    
    generar_grafo()
    print("Grafo del DFA generado y guardado.")

if __name__ == "__main__":
    procesar_datos()
    