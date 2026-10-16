import json
import os
from datetime import date

FILE_NAME = 'exp.json'


class Expences:
    def __init__(self,id,amount,catogery,note,day):
        self.id=id
        self.amount=amount
        self.catogery=catogery
        self.note=note
        self.day=day


    def to_dict(self):
        return{
            "id":self.id,
            "amount":self.amount,
            "catogery":self.catogery,
            "note":self.note,
           "day" :self.day

        }

    def show(self):
        print(f" {self.id}. {self.day} | {self.catogery} | {self.note }")


class Expencetrack:
    def __init__(self):
        self.expences = []
        self.load()

    def load(self):
        if not os.path.exists(FILE_NAME):
            return
        try:
            with open(FILE_NAME,"r") as f:
                for i in json.load(f):
                    self.expences.append(
                        Expences(i["id"], i["amount"], i["category"], i["note"], i["day"])
                    )
        except(json.JSONDecodeError,KeyError):
            print("Data File is Broken,The list is empty ")
            self.expences=[]

    def save(self):
        data =[e.to_dict() for e in self.expences]
        with open(FILE_NAME,"w")as f:
            json.dump(data,f,indent=4)




    def add(self,amount,catogery,note):
            new_id=self.expences[-1] .id +1 if self.expences else 1
            self.expences.append(Expences(new_id,amount,catogery,note ,str(date.today())))
            self.save()
            print("Expence Added Succesfully")


    def view(self):
        if not self.expences:
            print("Not Expences yet")
            return
        for e in self.expences:
            e.show()

    def delete(self ,id):
        for e in self.expences:
            if e.id == id:
                self.expences.remove(e)
                self.save()
                print("Expence is removed")
                return
            
        print("ID IS Not found ")
                

    def total(self):
        return sum(e.amount for e in self.expences)



    def by_catogery(self):
        result = {}
        for e in self.expences:
            result[e.catogery] =result.get(e.catogery,0) + e.amount
        return result



def ask_number(text):
        while True:
            try:
               return float(input(text))
            except ValueError:
               print("Please type a number.")

def main():
    tracker = Expencetrack()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Total spending")
        print("5. Spending by category")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            amount = ask_number("Amount: ")
            category = input("Category: ").strip().title()
            note = input("Note: ").strip()

            if not category:
                print("Category cannot be empty.")
                continue

            tracker.add(amount, category, note)

        elif choice == "2":
            tracker.view()

        elif choice == "3":
            expense_id = ask_number("ID to delete: ")

            if expense_id.is_integer():
                tracker.delete(int(expense_id))
            else:
                print("Please enter a whole-number ID.")

        elif choice == "4":
            print("Total spending:", tracker.total())

        elif choice == "5":
            for category, amount in tracker.by_category().items():
                print(f"{category}: {amount}")

        elif choice == "6":
            print("Bye!")
            break

        else:
            print("Wrong choice, try again.")


if __name__ == "__main__":
    main()