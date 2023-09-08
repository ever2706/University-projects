function [mRK2] = RK2 (f,a,b,w0,n)
  syms t y;
  w=w0;
  h=(b-a)/n;
  ti=a:h:b;
  wi(1)=w0;
  for i=1:n
    k1=double(h*subs(f, [t y], [ti(i) wi(i)]));
    k2=double(h*subs(f, [t y], [ti(i)+h wi(i)+k1]));
    wi(i+1)=wi(i)+(k1+k2)/2;
    
  endfor
  
  mRK2=[ti' wi'];
  

endfunction