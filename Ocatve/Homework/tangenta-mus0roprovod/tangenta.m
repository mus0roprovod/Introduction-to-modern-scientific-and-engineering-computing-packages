function tangenta(fd,dmin,dmax,n)
% Функция для построения графика касательной для параметрически заданной плоской кривой
  t = linspace(dmin, dmax, 2 * n + 1);

  points = zeros(2, length(t));
  for k = 1:length(t)
    points(:, k) = fd(t(k));
  endfor
  plot(points(1, :), points(2, :), 'b');

  t_mid = t(n + 1);
  df = diffi(@fd, t_mid);
  
  hold on;
  if eps < df(1)
    x = un 
  endif
  hold off; 
endfunction