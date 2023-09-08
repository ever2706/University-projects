function [mEuler] = Euler (f,a,b,w0,n)
  syms t y
  
  h=(b-a)/n ;
  ti=a:h:b;
  wi(1)=w0;
  for i=1:n
    f1=double(h*subs(f,[t y], [ti(i) wi(i)]));
    
    wi(i+1) = wi(i)+f1;
  endfor
  mEuler=[ti' wi'];
endfunction
