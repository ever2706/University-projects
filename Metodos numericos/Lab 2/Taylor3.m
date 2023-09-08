function [mTaylor3] = Taylor3 (f,a,b,w0,n)
  syms t y
  dt=diff(f,t);
  dw=diff(f,y);
  derf1=dt+dw*f;
  dt2=diff(derf1,t);
  dw2=diff(derf1,y);
  derf2=dt2+dw2*f;
  h=(b-a)/n ;
  ti=a:h:b;
  wi(1)=w0;
  for i=1:n
    f1=double(h*subs(f,[t y], [ti(i) wi(i)]));
    f2=double(h^2/2*subs(derf1,[t y],[ti(i) wi(i)]));
    f3=double(h^2/6*subs(derf2,[t y],[ti(i) wi(i)]));
    wi(i+1) = wi(i)+f1+f2+f3;
  endfor
  mTaylor3=[ti' wi'];
endfunction
