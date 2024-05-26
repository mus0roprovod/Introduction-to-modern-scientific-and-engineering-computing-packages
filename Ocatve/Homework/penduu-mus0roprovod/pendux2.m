function [t, coords] = pendux2(params, initial_angles, time_range)
    % Начальные условия: углы и угловые скорости (в радианах и рад/с)
    y0 = [initial_angles(1), 0, initial_angles(2), 0];  % [theta1, omega1, theta2, omega2]

    % Решение дифференциальных уравнений с использованием ode45
    options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);
    [t, y] = ode45(@(t, y) doublePendulumODE(t, y, params), time_range, y0, options);

    % Преобразование углов в координаты
    theta1 = y(:, 1);
    theta2 = y(:, 3);

    x1 = params(1).l * sin(theta1);
    y1 = -params(1).l * cos(theta1);
    x2 = x1 + params(2).l * sin(theta2);
    y2 = y1 - params(2).l * cos(theta2);

    coords = [x1, y1, x2, y2]';
end

% Функция для вычисления производных двойного маятника
function dydt = doublePendulumODE(~, y, params)
    g = 9.81;  % Ускорение свободного падения
    L1 = params(1).l;
    L2 = params(2).l;
    m1 = params(1).m;
    m2 = params(2).m;

    theta1 = y(1);
    omega1 = y(2);
    theta2 = y(3);
    omega2 = y(4);

    delta_theta = theta2 - theta1;

    dydt = zeros(4, 1);
    dydt(1) = omega1;
    dydt(2) = (m2 * g * sin(theta2) * cos(delta_theta) - m2 * sin(delta_theta) * (L1 * omega1^2 * cos(delta_theta) + L2 * omega2^2) - (m1 + m2) * g * sin(theta1)) / (L1 * (m1 + m2 * sin(delta_theta)^2));
    dydt(3) = omega2;
    dydt(4) = ((m1 + m2) * (L1 * omega1^2 * sin(delta_theta) - g * sin(theta2) + g * sin(theta1) * cos(delta_theta)) + m2 * L2 * omega2^2 * sin(delta_theta) * cos(delta_theta)) / (L2 * (m1 + m2 * sin(delta_theta)^2));
end

