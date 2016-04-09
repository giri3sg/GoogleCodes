_T = int(raw_input()) #read number of test cases
for _t in range(_T):
  res = 0
  stack = raw_input()
  while(len(stack)!=0):
    stacklist = list(stack)
    findex = stack.find('-')
    lindex = stack.rfind('-')
    if lindex == -1: #if no - is found already sorted
      break
      
    stacklist = stacklist[0:lindex+1] #remove ending '+' coz we don't care 
    if len(stacklist)==0:
      break

    if findex >0:    # swap starting '+' packs
      res+=1
      for i in xrange(0,findex):
        stacklist[i]='-'
    
    if lindex > -1:    
      res+=1
      stacklist.reverse()
      for x in xrange(0,len(stacklist)):
        stacklist[x] = 'x' if stacklist[x] is '-' else '-'
    stack=''.join(stacklist)
  print 'Case #%i:'%(_t+1),res
