#


#


#
def evaluate(y, w, capital_value):

    cv = capital_value

    tl_capital = [cv]
    tl_c1 = []
    tl_c2 = []
    tl_r = []

    kk = {'f1f': [], 'f1c': [], 'f2f': [], 'f2c': [], 'f1f_f2c': [], 'f1c_f2f': [], 'fc': [], 'f1': [], 'f2': []}

    for j in range(w.shape[0]):

        c1 = cv * w[j, 0]
        c2 = cv * w[j, 1]

        f1 = c1 / y[j, 0]
        f2 = c2 / y[j, 1]

        f1_f = int(f1)
        f1_c = f1_f + 1
        f2_f = int(f2)
        f2_c = f2_f + 1

        kk['f1f'].append(f1_f)
        kk['f1c'].append(f1_c)
        kk['f2f'].append(f2_f)
        kk['f2c'].append(f2_c)

        f1f_f2c = (f1_f * y[j, 0] + f2_c * y[j, 1]) <= cv
        f1c_f2f = (f1_c * y[j, 0] + f2_f * y[j, 1]) <= cv

        kk['f1f_f2c'].append(f1f_f2c)
        kk['f1c_f2f'].append(f1c_f2f)

        if f1f_f2c and not f1c_f2f:
            f1, f2 = f1_f, f2_c
        elif not f1f_f2c and f1c_f2f:
            f1, f2 = f1_c, f2_f
        elif f1f_f2c and f1c_f2f:
            rf1_f = f1_f * y[j, 0] / cv
            rf1_c = f1_c * y[j, 0] / cv
            rf2_f = f2_f * y[j, 1] / cv
            rf2_c = f2_c * y[j, 1] / cv
            f1f_f2c_diff = max([abs(rf1_f - w[j, 0]), abs(rf2_c - w[j, 1])])
            f1c_f2f_diff = max([abs(rf1_c - w[j, 0]), abs(rf2_f - w[j, 1])])
            if f1f_f2c_diff < f1c_f2f_diff:
                f1, f2 = f1_f, f2_c
            else:
                f1, f2 = f1_c, f2_f
        else:
            f1, f2 = f1_f, f2_f

        kk['f1'].append(f1)
        kk['f2'].append(f2)

        rem = cv - f1 * y[j, 0] - f2 * y[j, 1]
        cv = f1 * y[j + 1, 0] + f2 * y[j + 1, 1] + rem

        tl_c1.append(f1 * y[j, 0])
        tl_c2.append(f2 * y[j, 1])
        tl_r.append(rem)
        tl_capital.append(cv)

    return tl_capital, tl_c1, tl_c2, tl_r, kk
