# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:46:29 2021

@author: Esther_Su
"""
import pandas as pd
import argparse

def read_notes():
    """
    Read the highlight notes in kindle Clippings.txt 
    Returns list of notes
    -------
    contents : TYPE
        DESCRIPTION.

    """
    df = pd.read_csv('My Clippings.txt', delimiter = "\t", header=None)
    contents = df[0]
    return contents

def crack_notes(contents, book_name_substr='all'):
    """
    crack notes without citiations

    Parameters
    ----------
    contents : TYPE
        DESCRIPTION.
    book_name_substr : TYPE, optional
        DESCRIPTION. The default is 'all'.

    Returns
    -------
    notes : TYPE
        DESCRIPTION.

    """
    notes = []
    if book_name_substr=='all':
        keyword = '========'
        diff = -1
    else:
        keyword = book_name_substr
        diff = 2
    idxs = contents[contents.str.contains(keyword)].index
    for i in idxs:
        notes.append(contents[i+diff])
    return notes

def write_to_file(notes, book_name_substr):
    """
    Write notes in a file

    Parameters
    ----------
    notes : TYPE
        DESCRIPTION.
    book_name_substr : TYPE
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.

    """
    with open(book_name_substr + '_notes.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n\n'.join(notes))
    return 'Done!'
    
def main(bookname):
    contents = read_notes()
    notes = crack_notes(contents, bookname)
    write_to_file(notes, bookname)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Crack notes from kindle clips')
    parser.add_argument('bookname', help='the book name to crack notes, enter it', default='all')
    args = parser.parse_args()
    main(args.bookname)