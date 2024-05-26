function caterpillar(x,y,n)
  x_curve = x;
  y_curve = y;
  num_circles = n;
  radius = 1/2;
  figure;
  plot(x_curve, y_curve);
  hold on;
  
  plot_handles = zeros(1, num_circles);
  angle = linspace(0, 2*pi, 100);
  circle_x = @(phi) radius * cos(phi);
  circle_y = @(phi) radius * sin(phi);
  
  
  axis equal;
  center_index = 1; % для окружности первой 
  movement_direction = 1; 
  
  for i = 1:num_circles
    idx = center_index + (i-1) * 10; % шаг между окружностями
    if idx > length(x_curve)
        idx = length(x_curve);
    end
    x_center = x_curve(idx);
    y_center = y_curve(idx);
    plot_handles(i) = plot(circle_x(angle) + x_center, circle_y(angle) + y_center, 'r-');
  endfor
  
      
  bounce_count = 0; 
  max_bounces = 5;
  
    
  purple = [0.627, 0.125, 0.941];
  while bounce_count < max_bounces
      for i = 1:num_circles
          idx = max(min(center_index + (i-1) * 10, length(x_curve)), 1);
          x_center = x_curve(idx);
          y_center = y_curve(idx);
          set(plot_handles(i), 'XData', circle_x(angle) + x_center, 'YData', circle_y(angle) + y_center);
      endfor
          center_index += movement_direction;
    if center_index > (length(x_curve) - num_circles * 10) || center_index < 1
            movement_direction = -movement_direction;
            bounce_count += 1; 
        end
      drawnow;
  endwhile
  
  hold off;
endfunction
