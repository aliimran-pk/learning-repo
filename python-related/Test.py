
try:
    a = 0
    print (1/0)
except Exception as e:
    print("In Exception " + e.message)
else:
    print("No Exception")
finally:
    print("In Finally")