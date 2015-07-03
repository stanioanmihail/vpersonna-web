function octave_plot_stats()
    x=[1, 2, 4, 8, 16, 32, 64,];
    y=[409.633, 331.142, 352.821, 379.586, 364.017, 405.038, 343.217];
    y2=[34350, 29240, 28570, 29360, 28770, 28910, 29220];

    figure(1);
    plot(x, y);
    title("Performante interfata Advanced Statistics pe platforma Laptop Lenovo IdeaPad G510");
    xlabel("Numar colectii de date filtrate dupa data si insumate (numar zile)");
    ylabel("CPU Load(ms)");
    grid on;
    legend("CPU Load/agregare sesiuni per zile");

    figure(2);
    plot(x, y2);
    title("Performante interfata Advanced Statistics pe platforma Raspberry Pi 1 Model B");
    xlabel("Numar colectii de date filtrate dupa data si insumate (numar zile)");
    ylabel("CPU Load(ms)");
    grid on;
    legend("CPU Load/agregare sesiuni per zile");



endfunction
