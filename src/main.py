from scrapping import webScrapper, URL_COURSEINFO_BYIST
from managejson import create_classcodejson


def main():
 webScrapper.get_allnrc_dpt("IST4330",URL_COURSEINFO_BYIST)

if __name__ == '__main__':
 main()