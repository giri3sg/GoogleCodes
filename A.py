_T = int(raw_input())
for _t in range(_T):
  done=0
  N = int(raw_input())
  result=0
  List = [0,0,0,0,0,0,0,0,0,0]
  if N is not 0:
    i=1
    while(sum(List) != 10):
      n=i*N
      result=n
      while(n!=0):
        x=n%10
        n=n/10
        List[x]=1 
      i+=1
  if result  is 0:
    result = "INSOMNIA"
  print 'Case #%i:'%(_t+1),result
