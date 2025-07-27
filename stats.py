def word_count(text):
    text_array = text.split()
    return len(text_array)

def char_count(text):
    dict = {}
    lower_text = text.lower()
    for c in lower_text:
        if c not in dict:
            dict[c]=1
        else:
            dict[c]+=1
    return dict

def sort_on(items):
    return items["num"]

def sort_dict(char_dic):
    diclist = []
    for item in char_dic:
        new_dic = {"char": item, "num": char_dic[item]}
        diclist.append(new_dic)
    diclist.sort(reverse=True, key=sort_on)
    return diclist
