params(1).m = 1;
params(1).l = 2;
params(2).m = 3;
params(2).l = 4;
initial_angles = [pi/4, pi/2];
time_range = [0, 20]; % Временной интервал
[t, coords] = pendux2(params, initial_angles, time_range);
figure;
hold on;
h1 = plot([0, coords(1, 1)], [0, coords(2, 1)], 'b', 'LineWidth', 2);
h2 = plot(coords(1, 1), coords(2, 1), 'bo', 'MarkerSize', 10, 'MarkerFaceColor', 'b');
h3 = plot([coords(1, 1), coords(3, 1)], [coords(2, 1), coords(4, 1)], 'r', 'LineWidth', 2);
h4 = plot(coords(3, 1), coords(4, 1), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
trajectory1 = plot(coords(1, 1), coords(2, 1), 'b--');
trajectory2 = plot(coords(3, 1), coords(4, 1), 'r--');
xlim([-2, 2]);
ylim([-2, 2]);
grid on;
axis equal;
trajectory_x1 = coords(1, 1);
trajectory_y1 = coords(2, 1);
trajectory_x2 = coords(3, 1);
trajectory_y2 = coords(4, 1);
for i = 1:length(t)
    set(h1, 'XData', [0, coords(1, i)], 'YData', [0, coords(2, i)]);
    set(h2, 'XData', coords(1, i), 'YData', coords(2, i));
    set(h3, 'XData', [coords(1, i), coords(3, i)], 'YData', [coords(2, i), coords(4, i)]);
    set(h4, 'XData', coords(3, i), 'YData', coords(4, i));
    set(trajectory1, 'XData', trajectory_x1, 'YData', trajectory_y1);
    set(trajectory2, 'XData', trajectory_x2, 'YData', trajectory_y2);
    title(sprintf('Double pendulum %.1f seconds', t(i)));  % Заголовок графика

    % Добавление текущих координат в траектории
    trajectory_x1 = [trajectory_x1, coords(1, i)];
    trajectory_y1 = [trajectory_y1, coords(2, i)];
    trajectory_x2 = [trajectory_x2, coords(3, i)];
    trajectory_y2 = [trajectory_y2, coords(4, i)];

    drawnow;
end

