function res = fence(rows, cols)
  # формирует по заданому количеству строк и столбцов логическую матрицу с чередующимися нулевыми и единичными столбцами.
    if nargin < 2
      n = rows;
      m = rows; 
    else
      n = rows;
      m = cols;
    endif
    
  
    res = ones(n, m, 'logical');
    res(:, 2:2:end) = 0;
end
