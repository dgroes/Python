""" 
const production1 = [
  { toy: 'car', quantity: 3 },
  { toy: 'doll', quantity: 1 },
  { toy: 'ball', quantity: 2 }
]

const result1 = manufactureGifts(production1)
console.log(result1)
// ['car', 'car', 'car', 'doll', 'ball', 'ball']
"""

gifts = [
    { "toy": 'car', "quantity": 3 },
    { "toy": 'doll', "quantity": 1 },
    { "toy": 'ball', "quantity": 2 }
]
## print(gifts)

def manufacture_gifts(gifts_to_produce):
    # lista en la que estarán los regalos a facturar
    produce = []
    regalo = []

    gifts = []

    #recorrer la lista de diccionarios
    for groups in gifts_to_produce:

        toys = list(groups.values())[0]
        quantity = list(groups.values())[1]
        
        gifts.extend([toys] * quantity)


    return gifts

print(manufacture_gifts(gifts))