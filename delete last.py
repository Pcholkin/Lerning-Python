ss = input("Enter:")
l = len(ss)
rem_lst = ss[:l-1]   #удаляем последний символ
print(rem_lst)
show_last = ss[-1]  #показываем последний символ
print(show_last)

#еще так можно

mm = input('Enter:')
Rem_lst2 = mm[:-1]  #тоже удаляем последний символ
print(Rem_lst2)
