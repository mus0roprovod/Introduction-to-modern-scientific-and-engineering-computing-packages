function hypersurf(A)

  x0 = -10; x1 = 10; xx = 100;
  y0 = -10; y1 = 10; yy = 100;

  x = linspace(x0, x1, xx);
  y = linspace(y0, y1, yy);
  [X, Y] = meshgrid(x, y);

  inv_1 = sum(diag(A)) - A(4, 4);
  inv_2 = det(A([1 2], [1 2])) + det(A([2 3], [2 3])) + det(A([1 3], [1 3]));
  inv_3 = det(A(1:3, 1:3));
  inv_4 = det(A);

  if (inv_3 != 0 && (inv_2 <= 0 || inv_1 * inv_3 <= 0) && 0 < inv_4)
    eigenvalues = eig(A(1:3, 1:3));
    Z_POS = sqrt(abs((-inv_4 / inv_3) - eigenvalues(1) * X.^2 - eigenvalues(2) * Y.^2) / eigenvalues(3));
    Z_NEG = - Z_POS;

    surf(X, Y, Z_POS);
    hold on;
    surf(X, Y, Z_NEG);

  endif


endfunction

function res = comp(a, b)
  res = abs(a) < abs(b);
endfunction
