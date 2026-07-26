from dataclasses import dataclass


@dataclass
class Config:
    tjptuf: int = 851
    eclnfeb: int = 268

    def total(self):
        return self.tjptuf + self.eclnfeb


if __name__ == "__main__":
    x = Config()
    print(x.total())
