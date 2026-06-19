try :
  num1=int(input())
  num=input()
  num2=int(input())
  if num=="+":
    ans=num1+num2
    print(ans)
  elif num=="-":
    ans=num1-num2
    print(ans)
  elif num=="*":
    ans=num1*num2
    print(ans)
  elif num=="/":
    ans=num1/num2
    print(f"{ans:.2f}")
except Exception as e :
   print(e)


