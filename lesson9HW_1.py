di={'A001':'小熊軟糖 20元','A002':'冰棒 25元','A004':'王子麵 10元','A006':'汽水 30元'}

k=str(input('請輸入貨號:'))
if k in di:
    print(di[k])
else:
    print('無此項目,請新增貨號')
    add=str(input('新增貨號:'))
    a=str(input('新增商品,價錢:'))
    di[add]=a
    print(di)