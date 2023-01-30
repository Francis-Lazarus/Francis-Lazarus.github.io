from pylab import *

def distCourreur(v,tArray):
   '''
      d(vt,0) dans R/Z
   '''
   return [min((v*t)%1, (-v*t)%1) for t in tArray]

def plotv(v,tArray):
   plot(tArray, distCourreur(v,tArray), label=str(v))

def minDist(vArray,t):
   return min([min((v*t)%1, (-v*t)%1) for v in vArray])

def integrate(x,y):
   '''
      integre y(x)
   '''
   a=0
   for i in range(size(x)-1):
      a += (x[i+1] - x[i])*(y[i+1] + y[i])
   return a/2.

def minDistPlot(vArray,tArray):
   y=[minDist(vArray,t) for t in tArray]
   aire = integrate(tArray,y)
   plot(tArray, y, "k", linewidth=3,label='aire = ' + str(aire))

def plotAll(vArray, n):
   x=linspace(0,1,n+1)
   for v in vArray:
      plotv(v,x)
   minDistPlot(vArray,x)
   y=1./(size(vArray)+1)
   plot([0,1],[y,y],"r--")
   legend()
   show()

