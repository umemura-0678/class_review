class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def age(self):
        return self.age

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age > 3 and self.age < 20:
            return 1000
        elif self.age >= 20 and self.age < 65:
            return 1500
        elif self.age >= 65 and self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# 省略
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 500 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())


print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print(michelle.info_tab())
