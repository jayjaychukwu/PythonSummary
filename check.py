class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year

    def __str__(self) -> str:
        return f"tags={self.tags}, year = {self.year}"


tags = ["g", "m"]
year = 2022
bc = FunEvent(tags, year)
tags.append("h")
year = 21
print(bc)
