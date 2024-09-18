from __future__ import annotations
from typing import List

class Product:
    __lastSale: Sale = None
    __inventory: int = 0  # New inventory attribute

    def __init__(self, sale: Sale = None, inventory: int = 0):
        self.__lastSale = sale
        self.__inventory = inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    def reduceInventory(self, amount: int):
        if amount <= self.__inventory:
            self.__inventory -= amount
        else:
            raise ValueError("Not enough inventory")

    def addInventory(self, amount: int):
        self.__inventory += amount

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    @property
    def getInventory(self) -> int:
        return self.__inventory

class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, products: List[Product], quantities: List[int]):
        Sale.__saleTimes += 1
        self.__productSold = products
        self.__saleNumber = Sale.__saleTimes

        for index, product in enumerate(products):
            product.setLastSale(self)
            product.reduceInventory(quantities[index])

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber

# Create Products with initial inventory
productOne = Product(inventory=10)
productTwo = Product(inventory=20)

# Create Sales
saleOne = Sale([productOne, productTwo], [2, 3])  # Sale of 2 from productOne, 3 from productTwo
saleTwo = Sale([productOne], [1])  # Sale of 1 from productOne

print(f"ProductOne Last Sale: {productOne.getLastSale.getSaleNumber}, Remaining Inventory: {productOne.getInventory}")
print(f"ProductTwo Last Sale: {productTwo.getLastSale.getSaleNumber}, Remaining Inventory: {productTwo.getInventory}")
