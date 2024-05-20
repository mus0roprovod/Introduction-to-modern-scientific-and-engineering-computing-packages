function res = diffi(fd,ts, h = 10 ^(-8))
  % Функция для приближенного вычисления значения производной векторной функции 
  for k = 1 : length(ts)
    res(k) = (fd(ts(k) + h) - fd(ts(k))) / h;  
  endfor
endfunction