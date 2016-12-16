def indianFlag():
    s = [255, 153, 51]
    w = [255, 255, 255]
    g = [19, 136, 8]
    n = [0, 0, 128]

    return [
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        w, w, w, n, n, w, w, w,
        w, w, w, n, n, w, w, w,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g
    ]

def englishFlag():
    w = [255, 255, 255]
    r = [204, 0, 0]

    return [
        w, w, w, r, r, w, w, w,
        w, w, w, r, r, w, w, w,
        w, w, w, r, r, w, w, w,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        w, w, w, r, r, w, w, w,
        w, w, w, r, r, w, w, w,
        w, w, w, r, r, w, w, w,
    ]

def britishFlag():
    w = [255, 255, 255]
    b = [0, 51, 153]
    r = [204, 0, 0]

    return [
        b, w, w, r, r, w, w, b,
        w, b, w, r, r, w, b, w,
        w, w, b, r, r, b, w, w,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        w, w, b, r, r, b, w, w,
        w, b, w, r, r, w, b, w,
        b, w, w, r, r, w, w, b,
    ]
