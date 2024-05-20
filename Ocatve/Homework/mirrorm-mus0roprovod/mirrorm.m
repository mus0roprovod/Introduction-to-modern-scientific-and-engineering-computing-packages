function retval = mirrorm (a, n)
  [r,c] = size(a);
  a_ud = flipud(a);
  a_lr = fliplr(a);
  a_c = flipud(a_lr).'
  a_t = a.'
  A = [a_c(c - n + 1:end, r - n + 1:end), a_ud(r-n+1:end, :), a_t(c - n + 1:end, 1:n);
  a_lr(:, c - n + 1:end), a, a_lr(:, 1:n);
  a_t(1:n, r - n + 1:end), a_ud(1:n, :), a_c(1:n, 1:n)];
  retval = uint32(A);
endfunction
