function hyperplot(A)

  inv_1 = sum(diag(A)) - A(4, 4);
  inv_2 = det(A([1 2], [1 2])) + det(A([2 3], [2 3])) + det(A([1 3], [1 3]));
  inv_3 = det(A(1:3, 1:3));
  inv_4 = det(A);

  eigenvalues = eig(A(1:3, 1:3));
  if (inv_3 != 0 && (inv_2 <= 0 || inv_1 * inv_3 <= 0) && 0 < inv_4)

    a = sqrt(abs(inv_4 / (eigenvalues(1) * inv_3)));
    b = sqrt(abs(inv_4 / (eigenvalues(2) * inv_3)));
    c = sqrt(abs(inv_4 / (eigenvalues(3) * inv_3)));

    for k = 1:100

      A1 = 1 / a; B1 = - k / b; C1 = 1 / c; D1 = k;
      A2 = 1 / a; B2 = 1 / (k * b); C2 = - 1 / c; D2 = 1 / k;

      n1 = [A1, B1, C1];
      n2 = [A2, B2, C2];

      direction = cross(n1, n2);

      A = [n1; n2];
      b_1 = [-D1; -D2];

      point = pinv(A) * b_1;
      t = linspace(-10, 10, 100);

      X = point(1) + t * direction(1);
      Y = point(2) + t * direction(2);
      Z = point(3) + t * direction(3);

      plot3(X, Y, Z, 'r', 'LineWidth', 2);
      hold on;
    endfor
  endif
end
