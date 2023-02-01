class Cdna:

    def __init__(self, cds=""):
        self.cds = cds

    def parse_to_cdna(self) -> str:
        cdna_list = list(self.cds.replace(" ", ""))
        result = [i for i in cdna_list if not i.isdigit()]

        return ''.join(result)
