function octave_plot()
    x=[5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560];
    y=[0.176, 0.194, 0.250, 0.299, 0.453, 0.747, 1.337, 2.455, 4.746, 9.450];
    y2=[7.780, 8.150, 9.890, 12.350, 17.420, 28.140, 48.930, 94.000, 176.300, 346.110];

    figure(1);
    plot(x, y);
    title("Performante modul agregare pe platforma Laptop Lenovo IdeaPad G510");
    xlabel("Numar intari de procesat");
    ylabel("CPU Load(s)");
    grid on;
    legend("CPU Load/nr. intrari de analizat");

    figure(2);
    plot(x, y2);
    title("Performante modul agregare pe platforma Raspberry Pi 1 Model B");
    xlabel("Numar intari de procesat");
    ylabel("CPU Load(s)");
    grid on;
    legend("CPU Load/nr. intrari de analizat");

    figure(3);
    plot(x, y, y2);
    title("Comparație performanțe între Lenovo și Raspberry PI");
    xlabel("Numar intari de procesat");
    ylabel("CPU Load(s)");
    grid on;
    legend("CPU Load Lenovo", "CPU Load Raspberry PI" );


endfunction
