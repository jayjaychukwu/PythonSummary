"""
Input: [ {“Dg set”: “Diesel generator”}, {“Organization”: “Organisation”}, {“Group”: “Organization”}, {“Orange”: “Kinnu”}, {“Orange”: “narangi”} ]
Output: [[“Organization”, “Organisation”, “Group”], [“Dg set”, “Diesel generator”], [“Orange”, “Kinnu”, “narangi”]]
"""


def synonyms(dict_list):
    syms = []


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
