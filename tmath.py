import re
import random
import asyncio
import numpy as np


async def ml(multiplicand, multiplier, obj=None):
    x1, x2 = 1, 1
    y1, y2 = 1, 1
    for i in range(multiplicand - 1):
        x1 *= 10
    for i in range(multiplicand):
        y1 *= 10
    for i in range(multiplier - 1):
        x2 *= 10
    for i in range(multiplier):
        y2 *= 10
    y1 -= 1
    y2 -= 1
    a = random.randint(x1, y1)
    b = random.randint(x2, y2)
    c = a * b
    if c == obj.c:
        await ml(multiplicand, multiplier, obj=obj)
    obj.c = c
    await obj.sendmsg(f"{a} * {b} = ?")
    while True:
        await asyncio.sleep(obj.timeout)
        await obj.readmsg()
        if obj.readlm == '/restart':
            await obj.restart()
        try:
            uc = re.findall(r"([0-9]{1,10})", obj.readlm)
            uc = int(uc[0])
        except:
            continue
        print(uc)
        if uc == obj.uc:
            continue
        obj.uc = uc
        if uc == c:
            await obj.sendmsg("You're God Damn right!")
            break
        elif uc != c:
            await obj.sendmsg(f"No, right answer is {c}!")
            break


async def dl(dividend, divider, obj=None):
    x1, x2 = 1, 1
    y1, y2 = 1, 1
    for i in range(dividend - 1):
        x1 *= 10
    for i in range(dividend):
        y1 *= 10
    for i in range(divider - 1):
        x2 *= 10
    for i in range(divider):
        y2 *= 10
    y1 -= 1
    y2 -= 1
    a = random.randint(x1, y1)
    b = random.randint(x2, y2)
    c1 = a // b
    c2 = a % b
    if c1 == obj.c1 or c2 == obj.c2:
        await dl(dividend, divider, obj=obj)
    obj.c1 = c1
    obj.c2 = c2
    await obj.sendmsg(f"{a} // | % {b} = ?")
    while True:
        await asyncio.sleep(obj.timeout)
        await obj.readmsg()
        if obj.readlm == '/restart':
            await obj.restart()
        try:
            uc = re.findall(r"[0-9]{1,10}", obj.readlm)
            uc1, uc2 = int(uc[0]), int(uc[1])
        except:
            continue
        if uc1 == obj.uc1 and uc2 == obj.uc2:
            continue
        obj.uc1 = uc1
        obj.uc2 = uc2
        if uc1 == c1 and uc2 == c2:
            await obj.sendmsg("You're God Damn right!")
            break
        else:
            await obj.sendmsg(f"No, right answer is {c1} with residual of {c2}!")
            break


async def vml(multiplicand, multiplier, matrix=2, obj=None):
    x1, x2 = 1, 1
    y1, y2 = 1, 1
    for i in range(multiplicand - 1):
        x1 *= 10
    for i in range(multiplicand):
        y1 *= 10
    for i in range(multiplier - 1):
        x2 *= 10
    for i in range(multiplier):
        y2 *= 10
    y1 -= 1
    y2 -= 1
    a1 = random.randint(x1, y1)
    a2 = random.randint(x1, y1)
    b1 = random.randint(x1, y1)
    b2 = random.randint(x1, y1)
    l1 = random.randint(x2, y2)
    l2 = random.randint(x2, y2)
    if matrix == 2:
        a = np.matrix([[a1, b1],
                       [a2, b2]])
        b = np.matrix([[l1],
                       [l2]])
    elif matrix == 3:
        c1 = random.randint(x1, y1)
        c2 = random.randint(x1, y1)
        a3 = random.randint(x1, y1)
        b3 = random.randint(x1, y1)
        c3 = random.randint(x1, y1)
        l3 = random.randint(x2, y2)
        a = np.matrix([[a1, b1, c1],
                       [a2, b2, c2],
                       [a3, b3, c3]])
        b = np.matrix([[l1],
                       [l2],
                       [l3]])
    elif matrix == 2.5:
        choices = ["2x3", "3x2"]
        fch = np.random.choice(choices, 1, replace=True, p=[0.5, 0.5])
        if matrix == 2.5 and fch == "2x3":
            c1 = random.randint(x1, y1)
            c2 = random.randint(x1, y1)
            l3 = random.randint(x2, y2)
            a = np.matrix([[a1, b1, c1],
                           [a2, b2, c2]])
            b = np.matrix([[l1],
                           [l2],
                           [l3]])
        elif matrix == 2.5 and fch == "3x2":
            a3 = random.randint(x1, y1)
            b3 = random.randint(x1, y1)
            a = np.matrix([[a1, b1],
                           [a2, b2],
                           [a3, b3]])
            b = np.matrix([[l1],
                           [l2]])
    c = np.matmul(a, b)
    if matrix == 2 or matrix == 2.5 and fch == "2x3":
        c1, c2 = c[0], c[1]
        if c1 == obj.c1 or c2 == obj.c2:
            await vml(multiplicand, multiplier, obj=obj)
        obj.c1 = c2
        obj.c2 = c2
        await obj.sendmsg(f"{a}\n*\n{b}\n= ?")
        while True:
            await asyncio.sleep(obj.timeout)
            await obj.readmsg()
            if obj.readlm == '/restart':
                await obj.restart()
            try:
                uc = re.findall(r"[0-9]{1,10}", obj.readlm)
                uc1, uc2 = int(uc[0]), int(uc[1])
            except:
                continue
            if uc1 == obj.uc1 and uc2 == obj.uc2:
                continue
            obj.uc1 = uc1
            obj.uc2 = uc2
            if uc1 == c1 and uc2 == c2:
                await obj.sendmsg("You're God Damn right!")
                break
            else:
                await obj.sendmsg(f"No, right answer is {c1}, {c2}!")
                break
    elif matrix == 3 or matrix == 2.5 and fch == "3x2":
        c1, c2, c3 = c[0], c[1], c[2]
        if c1 == obj.c1 or c2 == obj.c2 or c3 == obj.c3:
            await mml(multiplicand, multiplier, obj=obj)
        obj.c1 = c1
        obj.c2 = c2
        obj.c3 = c3
        await obj.sendmsg(f"{a}\n*\n{b}\n= ?")
        while True:
            await asyncio.sleep(obj.timeout)
            await obj.readmsg()
            if obj.readlm == '/restart':
                await obj.restart()
            try:
                uc = re.findall(r"[0-9]{1,10}", obj.readlm)
                uc1, uc2, uc3 = int(uc[0]), int(uc[1]), int(uc[2])
            except:
                continue
            if uc1 == obj.uc1 and uc2 == obj.uc2 and uc3 == obj.uc3:
                continue
            obj.uc1 = uc1
            obj.uc2 = uc2
            obj.uc3 = uc3
            if uc1 == c1 and uc2 == c2 and uc3 == c3:
                await obj.sendmsg("You're God Damn right!")
                break
            else:
                await obj.sendmsg(f"No, right answer is {c1}, {c2}, {c3}!")
                break


async def mml(multiplicand, multiplier, matrix=2, obj=None):
    x1, x2 = 1, 1
    y1, y2 = 1, 1
    for i in range(multiplicand - 1):
        x1 *= 10
    for i in range(multiplicand):
        y1 *= 10
    for i in range(multiplier - 1):
        x2 *= 10
    for i in range(multiplier):
        y2 *= 10
    y1 -= 1
    y2 -= 1
    a1 = random.randint(x1, y1)
    a2 = random.randint(x1, y1)
    b1 = random.randint(x1, y1)
    b2 = random.randint(x1, y1)
    l1 = random.randint(x2, y2)
    l2 = random.randint(x2, y2)
    q1 = random.randint(x2, y2)
    q2 = random.randint(x2, y2)
    if matrix == 2:
        a = np.matrix([[a1, b1],
                       [a2, b2]])
        b = np.matrix([[l1, q1],
                       [l2, q2]])
    elif matrix == 3:
        c1 = random.randint(x1, y1)
        c2 = random.randint(x1, y1)
        s1 = random.randint(x2, y2)
        s2 = random.randint(x2, y2)
        a3 = random.randint(x1, y1)
        b3 = random.randint(x1, y1)
        c3 = random.randint(x1, y1)
        l3 = random.randint(x2, y2)
        q3 = random.randint(x2, y2)
        s3 = random.randint(x2, y2)
        a = np.matrix([[a1, b1, c1],
                       [a2, b2, c2],
                       [a3, b3, c3]])
        b = np.matrix([[l1, q1, s1],
                       [l2, q2, s2],
                       [l3, q3, s3]])
    elif matrix == 2.5:
        choices = ["2x3", "3x2"]
        fch = np.random.choice(choices, 1, replace=True, p=[0.5, 0.5])
        if matrix == 2.5 and fch == "2x3":
            c1 = random.randint(x2, y2)
            c2 = random.randint(x2, y2)
            l3 = random.randint(x2, y2)
            q3 = random.randint(x2, y2)
            a = np.matrix([[a1, b1, c1],
                           [a2, b2, c2]])
            b = np.matrix([[l1, q1],
                           [l2, q2],
                           [l3, q3]])
        elif matrix == 2.5 and fch == "3x2":
            a3 = random.randint(x1, y1)
            b3 = random.randint(x1, y1)
            s1 = random.randint(x2, y2)
            s2 = random.randint(x2, y2)
            a = np.matrix([[a1, b1],
                           [a2, b2],
                           [a3, b3]])
            b = np.matrix([[l1, q1, s1],
                           [l2, q2, s2]])
    c = np.matmul(a, b)
    if matrix == 2 or matrix == 2.5 and fch == "2x3":
        c1, c2, c3, c4 = c[0, 0], c[0, 1], c[1, 0], c[1, 1]
        if c1 == obj.c1 or c2 == obj.c2:
            await mml(multiplicand, multiplier, obj=obj)
        elif c3 == obj.c3 or c4 == obj.c4:
            await mml(multiplicand, multiplier, obj=obj)
        obj.c1 = c1
        obj.c2 = c2
        obj.c3 = c3
        obj.c4 = c4
        await obj.sendmsg(f"{a}\n*\n{b}\n= ?")
        while True:
            await asyncio.sleep(obj.timeout)
            await obj.readmsg()
            if obj.readlm == '/restart':
                await obj.restart()
            try:
                uc = re.findall(r"[0-9]{1,10}", obj.readlm)
                uc1, uc2 = int(uc[0]), int(uc[1])
                uc3, uc4 = int(uc[2]), int(uc[3])
            except:
                continue
            if uc1 == obj.uc1 and uc2 == obj.uc2:
                continue
            elif uc3 == obj.uc3 and uc4 == obj.uc4:
                continue
            obj.uc1 = uc1
            obj.uc2 = uc2
            obj.uc3 = uc3
            obj.uc4 = uc4
            if uc1 == c1 and uc2 == c2 and uc3 == c3 and uc4 == c4:
                await obj.sendmsg("You're God Damn right!")
                break
            else:
                await obj.sendmsg(f"No, right answer is {c1}, {c2}, {c3}, {c4}")
                break
    elif matrix == 3 or matrix == 2.5 and fch == "3x2":
        c1, c2, c3 = c[0, 0], c[0, 1], c[0, 2]
        c4, c5, c6 = c[1, 0], c[1, 1], c[1, 2]
        c7, c8, c9 = c[2, 1], c[2, 1], c[2, 2]
        if c1 == obj.c1 or c2 == obj.c2 or c3 == obj.c3:
            await mml(multiplicand, multiplier, obj=obj)
        elif c4 == obj.c4 or c5 == obj.c5 or c6 == obj.c6:
            await mml(multiplicand, multiplier, obj=obj)
        obj.c1 = c1
        obj.c2 = c2
        obj.c3 = c3
        obj.c4 = c4
        obj.c5 = c5
        obj.c6 = c6
        obj.c7 = c7
        obj.c8 = c8
        obj.c9 = c9
        await obj.sendmsg(f"{a}\n*\n{b}\n= ?")
        while True:
            await asyncio.sleep(obj.timeout)
            await obj.readmsg()
            if obj.readlm == '/restart':
                await obj.restart()
            try:
                uc = re.findall(r"[0-9]{1,10}", obj.readlm)
                uc1, uc2, uc3 = int(uc[0]), int(uc[1]), int(uc[2])
                uc4, uc5, uc6 = int(uc[3]), int(uc[4]), int(uc[5])
                uc7, uc8, uc9 = int(uc[6]), int(uc[7]), int(uc[8])
            except:
                continue
            if uc1 == obj.uc1 and uc2 == obj.uc2 and uc3 == obj.uc3:
                continue
            elif uc4 == obj.uc4 and uc5 == obj.uc5 and uc6 == obj.uc6:
                continue
            elif uc7 == obj.uc7 and uc8 == obj.uc8 and uc9 == obj.uc9:
                continue
            obj.uc1 = uc1
            obj.uc2 = uc2
            obj.uc3 = uc3
            obj.uc4 = uc4
            obj.uc5 = uc5
            obj.uc6 = uc6
            obj.uc7 = uc7
            obj.uc8 = uc8
            obj.uc9 = uc9
            if uc1 == c1 and uc2 == c2 and uc3 == c3:
                await obj.sendmsg("You're God Damn right!")
                break
            else:
                await obj.sendmsg(f"No, right answer is {c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}, {c9}!")
                break
