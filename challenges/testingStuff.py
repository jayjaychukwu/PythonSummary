"""
Input: [ {“Dg set”: “Diesel generator”}, {“Organization”: “Organisation”}, {“Group”: “Organization”}, {“Orange”: “Kinnu”}, {“Orange”: “narangi”} ]
Output: [[“Organization”, “Organisation”, “Group”], [“Dg set”, “Diesel generator”], [“Orange”, “Kinnu”, “narangi”]]
"""


def synonyms(dict_list):
    syms = []
    keys = []
    values = []
    for dict_item in dict_list:
        for a in dict_item.keys():
            keys.append(a)
        for b in dict_item.values():
            values.append(b)
    new_dict = {k: v for dict in dict_list for (k, v) in dict.items()}
    print(new_dict)
    for dict in new_dict:
        temp = []
        for key in keys:
            if dict.values() in key:
                temp.append(key, dict[key], dict.values())
        syms.append(temp)
    print(syms)
    # dict_keys = []
    # dict_values = []
    # synonymous = []
    # for dict_item in dict_list:
    #     for a in dict_item.keys():
    #         dict_keys.append(a)
    #     for b in dict_item.values():
    #         dict_values.append(b)
    # for dict in dict_list:
    #     print(dict.keys(), dict.values())
    #     for i in dict_keys:
    #         if i == dict.values():
    #             synonymous.append([dict.keys(), dict.values(), i, dict_list[i]])
    # print(synonymous)
    # for dict_item in dict_list:
    #     for a in dict_item.keys():
    #         dict_keys.append(a)
    #     for b in dict_item.values():
    #         dict_values.append(b)
    # print(dict_keys, dict_values)


if __name__ == "__main__":
    print(
        synonyms(
            [
                {"Dg set": "Diesel generator"},
                {"Organization": "Organisation"},
                {"Group": "Organization"},
                {"Orange": "Kinnu"},
                {"Orange": "narangi"},
            ]
        )
    )
