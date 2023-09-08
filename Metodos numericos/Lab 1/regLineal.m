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
## @deftypefn {} {@var{retval} =} regLineal (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Ever <Ever@DESKTOP-DTLVF8T>
## Created: 2020-11-02


function [rLinea,m,b]=regLineal(xi,yi)
  
syms x;
n=length(xi);
sumaxy=0;
sumax=0;
sumay=0;
sumaxcuadrado=0;
for i=1:1:n
  sumaxy=sumaxy+xi(i)*yi(i);
  sumax=sumax+xi(i);
  sumay=sumay+yi(i);
  sumaxcuadrado=sumaxcuadrado+xi(i)^2;
 endfor
 m=(n*sumaxy-sumax*sumay)/(n*sumaxcuadrado-(sumax)^2);
 b=(sumay-m*sumax)/(n);
 rLinea=m*x+b;
endfunction
