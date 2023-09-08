## Copyright (C) 2020 Ever
## 
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see
## <https://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} mTaylor2 (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Ever <Ever@DESKTOP-DTLVF8T>
## Created: 2020-12-16

function [mTay2] = mTaylor2 (f,a,b,w0,n)
  syms t y
  dt=diff(f,t);
  dw=diff(f,y);
  derf1=dt+dw*f;
  h=(b-a)/n ;
  ti=a:h:b;
  wi(1)=w0;
  for i=1:n
    f1=double(h*subs(f,[t y], [ti(i) wi(i)]));
    f2=double(h^2/2*subs(derf1,[t y],[ti(i) wi(i)]));
    wi(i+1) = wi(i)+f1+f2;
  endfor
  mTay2=[ti' wi'];
endfunction
