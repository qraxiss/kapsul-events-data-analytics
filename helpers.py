from charset_normalizer import detect
import pandas as pd


def column_formatter(col: pd.Series):
    # replace turkish characters
    col = col.str.lower()
    ascii = dict(
        ğ='g',
        ü='u',
        ş='s',
        ç='c',
        ö='o',
        ı='i',
        **{" ": "", "\n": ""})
    for k, v in ascii.items():
        col = col.str.replace(k, v)

    for i, item in enumerate(col):
        col[i] = utf8_convert(item)

    return col


def utf8_convert(name: str):
    #  and detect(name.encode())['encoding'] == 'utf-8'
    if type(name) == str:
        return str(name.encode("ascii", 'replace'), "windows-1252").replace("?", "").strip()
    else:
        return name


def first_letter_id_generator(name:str, hash_table:dict):
    try:
        print(name)
        letter = name[0]
    except IndexError:
        letter = name
    finally:
        id = ['22']
        try:
            id.extend(hash_table[letter])
        except KeyError:
            letter = letter.lower() # for "NaN"
            id.extend(hash_table[letter])
        finally:
            hash_table[letter][1] += 1

    print(letter)

    id[1:]=(list(map(lambda x: str(x)[1:], id[1:])))

    return "".join(id), hash_table