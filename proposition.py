p = True
q = False

logical_expr = "(p and (p or q)) or (q and p) or ((not p) or q)"

logical_expr = logical_expr.replace('p', str(p))
logical_expr = logical_expr.replace('q', str(q))

result = eval(logical_expr)

print(result)  

for p in [True,False]:
    for q in [True,False]:
        print(f"{p} {q} ", eval(f"{p} == {q}"))
