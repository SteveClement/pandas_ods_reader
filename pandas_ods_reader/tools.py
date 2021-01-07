"""Provides utility functions for the parser"""

import ezodf
import json

def ods_info(doc, json=False, nameOnly=False):
    """Prints the number of sheets, their names, and number of rows and columns
    """
    doc = check_ezodf_obj(doc)

    print("Spreadsheet contains %d sheet(s)." % len(doc.sheets))
    for sheet in doc.sheets:
        print("-"*40)
        print("   Sheet name : '%s'" % sheet.name)
        print("Size of Sheet : (rows=%d, cols=%d)" % (
            sheet.nrows(), sheet.ncols()))


def ods_sheet_names(doc, json=False):
    """Prints the name of sheets
    """
    doc = check_ezodf_obj(doc)

    if not json:
        print("Spreadsheet contains %d sheet(s)." % len(doc.sheets))
        for sheet in doc.sheets:
            print("-"*40)
            print("   Sheet name : '%s'" % sheet.name)

    if json:
        sheets = []
        for sheet in doc.sheet:
            sheets.append(doc.name)
        return json.dumps(json)


def check_ezodf_obj(doc):
    try:
        type(doc) is ezodf.document.PackageDocument
    except AttributeError:
        doc = ezodf.opendoc(doc)
    return doc

def sanitize_df(df):
    """Drops empty rows and columns from the DataFrame and returns it"""
    # Delete empty rows
    for i in df.index.tolist()[-1::-1]:
        if df.iloc[i].isna().all():
            df.drop(i, inplace=True)
        else:
            break
    # Delete empty columns
    cols = []
    for column in df:
        if not df[column].isnull().all():
            cols.append(column)
    df = df[cols]
    return df
