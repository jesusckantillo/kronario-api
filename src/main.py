from scrapping import webScrapper, URL_COURSEINFO
from managejson import create_classcodejson


def main():
 print(type(webScrapper.get_allnrcbycode("IBA4032", URL_COURSEINFO)))
 

if __name__ == '__main__':
 main()