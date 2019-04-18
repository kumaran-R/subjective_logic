def cumulative_fusion(arg1, arg2):
    a1 = arg1["baserate"]
    a2 = arg2["baserate"]
    b1 = arg1["belief"]
    b2 = arg2["belief"]
    u1 = arg1["uncertainty"]
    u2 = arg2["uncertainty"]
    u = 0.0
    b = 0.0
    a = 0.0
    if u1 != 0 or u2 != 0:
        b = (b1 * u2 + b2 * u1) / (u1 + u2 - u1 * u2)
        u = u1 * u2 / (u1 + u2 - u1 * u2)

        if u1 != 1 or u2 != 1:
            a = (a1 * u2 + a2 * u1 - (a1 + a2) * u1 * u2) / (u1 + u2 - 2 * u1 * u2)
        else:
            a = (a1 + a2) / 2
    else:
        b = 0.5 * (b1 + b2)
        u = 0
        a = 0.5 * (a1 + a2)
    return {'baserate': a,
            'uncertainty': u,
            'belief': b,
            'disbelief': 1 - u - b,
            'projectedproba': b + a * u}


def deduction_calculate(arg1, arg2):
    ax = float(arg2["baserate"])
    bx = arg2["belief"]
    dx = arg2["disbelief"]
    ux = arg2["uncertainty"]
    ex = arg2["projectedproba"]

    ay = arg1[0]["baserate"]
    b0 = arg1[0]["belief"]
    d0 = arg1[0]["disbelief"]
    u0 = arg1[0]["uncertainty"]
    e0 = arg1[0]["projectedproba"]

    b1 = arg1[1]["belief"]
    d1 = arg1[1]["disbelief"]
    u1 = arg1[1]["uncertainty"]
    e1 = arg1[1]["projectedproba"]

    bIy = bx * b0 + dx * b1 + ux * (b0 * ax + b1 * (1 - ax))
    dIy = bx * d0 + dx * d1 + ux * (d0 * ax + d1 * (1 - ax))
    uIy = bx * u0 + dx * u1 + ux * (u0 * ax + u1 * (1 - ax))

    Pyvacuousx = b0 * ax + b1 * (1 - ax) + ay * (u0 * ax + u1 * (1 - ax))

    K = 0

    if (((b0 > b1) and (d0 > d1)) or ((b0 <= b1) and (d0 <= d1))):
        K = 0
    elif (b0 > b1) and (d0 <= d1):  # CASE II
        if Pyvacuousx <= (b1 + ay * (1 - b1 - d0)):  # CASE A
            if (ex <= ax):  # Case 1
                K = ax * ux * (bIy - b1) / (ay * ex)
            else:  # Case 2
                K = ax * ux * (dIy - d0) * (b0 - b1) / ((dx + (1 - ax) * ux) * ay * (d1 - d0))
        else:  # CASE B
            if (ex <= ax):  # Case 1
                K = (1 - ax) * ux * (bIy - b1) * (d1 - d0) / (ex * (1 - ay) * (b0 - b1))
            else:  # Case 2
                K = (1 - ax) * ux * (dIy - d0) / ((1 - ay) * (dx + (1 - ax) * ux))
    else:  # CASE III
        if (Pyvacuousx <= (b1 + ay * (1 - b1 - d0))):  # CASE A
            if (ex <= ax):  # Case 1
                K = (1 - ax) * ux * (dIy - d1) * (b1 - b0) / (ex * ay * (d0 - d1))
            else:  # Case 2
                K = (1 - ax) * ux * (bIy - b0) / (ay * (dx + (1 - ax) * ux))
        else:  # CASE B
            if (ex <= ax):  # Case 1
                K = ax * ux * (dIy - d1) / (ex * (1 - ay))
            else:  # Case 2
                K = ax * ux * (bIy - b0) * (d0 - d1) / ((1 - ay) * (b1 - b0) * (dx + (1 - ax) * ux))

    by = bIy - ay * K
    dy = dIy - (1 - ay) * K
    uy = uIy + K

    ey = by + ay * uy
    return {
        'baserate': ay,
        'uncertainty': uy,
        'belief': by,
        'disbelief': dy,
        'projectedproba': ey}


def average_fusion(arg1,arg2):
    a1 = arg1["baserate"]
    a2 = arg2["baserate"]
    b1 = arg1["belief"]
    b2 = arg2["belief"]
    d1 = arg1["disbelief"]
    d2 = arg2["disbelief"]
    u1 = arg1["uncertainty"]
    u2 = arg2["uncertainty"]
    
    u = 0.0
    b = 0.0
    a =0.0
    if u1 != 0 or u2 != 0:
        b = (b1 * u2 + b2 * u1) / (u1 + u2)
        u = 2 * u1 * u2 / (u1 + u2)
        a = (a1 + a2) / 2
    else:
        b = 0.5 * (b1 + b2)
        u = 0
        a = 0.5 * (a1 + a2)

    return {'baserate': a,
            'uncertainty': u,
            'belief': b,
            'disbelief': 1 - u - b,
            'projectedproba': b + a * u}
