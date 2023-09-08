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
## @deftypefn {} {@var{retval} =} regCrec (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Ever <Ever@DESKTOP-DTLVF8T>
## Created: 2020-11-03

function [rCrec]=regCrec(xi,yi)
syms x;
n=length(xi);

for i=1:1:length(xi)
  xi(i)=1/(xi(i));
endfor

for i=1:1:length(yi)
  yi(i)=1/(yi(i));
endfor  
[f,m,c]=regLineal (xi, yi);
a=c^(-1);
b=m*a;
rCrec=(a*x)/(x+b);

endfunction
