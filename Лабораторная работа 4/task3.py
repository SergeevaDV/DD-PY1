def delete(list_, index=None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    #list_ = list_.split()
    #a = list_[len(list_) // 2]
    #left_list = list_[:a]
    #right_list = list_[a:]
    #for i in range(len(list_)):
        #list_index = list_[index]
        #current_list = list_[i]
        #if current_list == list_index :
           # del list_[index]
    #return delete(list_)
    if index is None:
        print("Этого индекса нет")
    else:
        return list_[:index] + list_[index+1:]
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4], index=4))  # [0, 1, 2, 3]
