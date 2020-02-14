#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    while ht.capacity < length:
        hash_table_resize(ht)
    
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
        first_index = i
        difference  = limit - weights[i]

        other_index = hash_table_retrieve(ht, difference)

        if other_index:
            if other_index == first_index:
                hash_table_remove(ht, difference)
                other_index = hash_table_retrieve(ht, difference)

            return (first_index, other_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

w = [4,4]
print(get_indices_of_item_weights(w,2,8))