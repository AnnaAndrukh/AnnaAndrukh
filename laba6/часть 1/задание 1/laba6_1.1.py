
import pandas as pd

class Library:
    data=pd.DataFrame()
    
    def add_book(self, name:str, author: str, year: int, genre: str):
        data_dictionary={"Назва":name, "Автор": author, "Рік": year, "Жанр": genre}
        self.data=self.data.append(data_dictionary, ignore_index=True)
        print(self.data)
    def delete_book(self, book_id: int):
        if len(self.data) == 0:
            print("Нет книг в библиотеке")
        else:
            self.data=self.data.drop(book_id)
            print(self.data)

    def find_book(self, book_id: int):
        all_indexes = self.data.head()
        for i in all_indexes.index:
            if all_indexes.index[i] == book_id:
                print(pd.DataFrame(self.data.iloc[book_id]))
l=Library()
print("Добавим первую книгу:")
l.add_book("Незнакомка","Александр Блок", 1906,"Худ.вымысел")

print("Добавим вторую книгу:")
l.add_book("Я вас любил","Александр Пушкин",1829 ,"Стихотворение") 

print("Удалим книгу с номером 0:")
l.delete_book(0)

print("Найдём книгу под номером 1:")
l.find_book(1)

