from functools import reduce
names=["Amit","Sham","John","Alice"]
marks=[85,90,73,92]

combine=list(zip(names,marks))

total_marks=reduce(lambda x,y:x+y,marks)
average=total_marks / len(marks)

topper=max(combine,key=lambda x: x[1])

pass_list=list(filter(lambda x: x[1] >= 80,combine))

print(f"\nAverage marks: {average}\n")

print(f"Topper: {topper[0]} ({topper[1]})\n")

print(f"Passed Students:")
for name,mark in pass_list:
    print(f"\t{name} ({mark})")

print("\nAll Students:")
for n,m in combine:
    print(f"{n:<8}: {m}")


