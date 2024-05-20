## Copyright (C) 2024 Kira
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

## -*- texinfo -*-
## @deftypefn {} {@var{retval} =} checkerboard (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Kira <musoroprovod@musoroprovod>
## Created: 2024-03-24

function res = checkerboard (rows, cols)
  if nargin < 2
    n = rows;
    m = rows;
  else
    n = rows;
    m = cols;
  endif  
  
  
    res = zeros(n, m, 'logical');
    for r = 1:n
        for c = 1:m
            res(r, c) = mod(r + c, 2) == 0;
        end
    end    
    
endfunction
