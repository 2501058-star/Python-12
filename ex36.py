a = {100, 200, 300, 400, 500}

is_super = a.issuperset({100, 200, 300, 400, 500})
is_sub = a.issubset({100, 200, 300, 400, 500})

if is_super and is_sub:
    print("동시")
elif is_super:
    print("상위")
elif is_sub:
    print("부분")