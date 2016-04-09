def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()
for _t in range(_T):

  N, S = raw_input().split()
  N = int(N)

  print _T
  print N
  print S
  
  res = N+N


  print 'Case #%i:'%(_t+1), res
