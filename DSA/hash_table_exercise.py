mydict={
  "Jan 1":27,
  "Jan 2":31,
  "Jan 3":23,
  "Jan 4":34,
  "Jan 5":37,
  "Jan 6":38,
  "Jan 7":29,
  "Jan 8":30,
  "Jan 9":35,
  "Jan 10":30

 }
maximum=max(mydict.values())
avg=mydict["Jan 1"]+mydict["Jan 2"]+mydict["Jan 3"]+mydict["Jan 4"]+mydict["Jan 5"]+mydict["Jan 6"]+mydict["Jan 7"]
print("Average Temperature of the week= ",end="")
print("%.2f"%(avg/7))
print("Maximum Temperature was: ",maximum)
