from typing import Dict
def flattenDictionary(dic):
    result = {}
    initial_key = ""
    flattenDictionaryHelper(initial_key, dic, result)
    return result
def flattenDictionaryHelper(parent,dic, result):
    for k in dic.keys():
        if k !="":
            val = dic[k]
            if not isinstance(val,Dict):
                #this is a primitive type
                if not parent:
                    result[k]=val
                else:
                    result[parent+"."+k] = val
            else:
                #this is another dictionary object now we will recurse
                if not parent:
                    flattenDictionaryHelper(k,val, result)
                else:
                    flattenDictionaryHelper(parent+"."+k,val,result)
           
def testMethod():
    dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
    output = flattenDictionary(dict)
    print(output)

testMethod()
