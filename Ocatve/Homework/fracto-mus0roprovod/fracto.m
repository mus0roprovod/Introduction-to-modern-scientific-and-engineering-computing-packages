function fracto(p, ll, ur, xx, yy)
  % p - вектор коэффициентов полинома
  % ll, ur - координаты верхнего левого и нижнего правого углов прямоугольной области
  % xx, yy - количество точек разбиения для осей Ox и Oy
 
  dp = polyder(p);
  exact_roots = roots(p);

  x_range = linspace(ll(1), ur(1), xx);
  y_range = linspace(ur(2), ll(2), yy);
  [X, Y] = meshgrid(x_range, y_range);
  Z = X + 1i*Y;

  for iter = 1:50
    Z = Z - polyval(p, Z) ./ polyval(dp, Z);
  end
  
  colors = spring(length(p) - 1);
  tmp = Z;

  for k = 1:length(exact_roots)
    distances = abs(Z - exact_roots(k));
    is_close = distances < 0.001;
    tmp(is_close == 1) =  100 * rgb2gray(colors(k, :));
  end

   image(tmp);
endfunction
