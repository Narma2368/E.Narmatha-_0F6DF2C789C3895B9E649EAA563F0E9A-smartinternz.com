

def linear_search_product(productlist,targetproduct):
  indices=[]
  for i,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(i)

  return indices


products=["pen","pencil","eraser","pen","pencil","pen"]
target=input("enter the target : ")
result=linear_search_product(products,target)
print(result)