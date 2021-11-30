import drawSvg as draw
import math


def build(Type, Inside, Outside, Depth, RailS, Glass, BackList):
    depthv = 0
    firstlen = (0, 0)

    if RailS <= 1:
        RailSString = str(RailS) + '"'
        LeftEnd = -60
        Numoffset = 11
        B45 = (4, 31)
        Lcorrect = 0.5
        flats = ()
    elif RailS <= 2:
        RailSString = str(RailS) + '"'
        LeftEnd = -75
        Numoffset = 8
        B45 = (8.6, 35)
        Lcorrect = 0
        lats = ()
    elif RailS <= 2.25:
        RailSString = str(RailS) + '"'
        LeftEnd = -79
        Numoffset = 4
        B45 = (9.6, 36.6)
        Lcorrect = 0.6
        lats = ()
    elif RailS <= 2.5:
        RailSString = str(RailS) + '"'
        LeftEnd = -82.5
        Numoffset = 5
        B45 = (10.6, 37.6)
        Lcorrect = 0.6
        lats = ()
    elif RailS <= 3:
        RailSString = str(RailS) + '"'
        LeftEnd = -87
        Numoffset = 5
        B45 = (12, 38.8)
        Lcorrect = 0.5
        lats = ()
    elif RailS > 3:
        RailSString = str(RailS) + '"'
        LeftEnd = -90
        Numoffset = -2
        B45 = (12.9, 39.5)
        Lcorrect = 0.3
        lats = ()


    if Type == "Flat":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 22, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        d.append(draw.Rectangle(LeftEnd, -5, 0.2, 5, transform="rotate(75)"))
    elif Outside == "Square":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        d.append(draw.Lines(LeftEnd, 25, LeftEnd+10, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
    elif Outside == "1/16R":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 21, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
        p.arc(LeftEnd+4, 21, 4, 90, 180)
        d.append(p)
        d.append(draw.Lines(LeftEnd+4, 25, LeftEnd+10, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
    elif Outside == "1/8R":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 19, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
        p.arc(LeftEnd+6, 19, 6, 90, 180)
        d.append(p)
        d.append(draw.Lines(LeftEnd+6, 25, LeftEnd+10, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
    elif Outside == "1/4R":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 17, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
        p.arc(LeftEnd+8, 17, 8, 90, 180)
        d.append(p)
        d.append(draw.Lines(LeftEnd+8, 25, LeftEnd+10, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
    elif Outside == "45B":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 19, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        d.append(draw.Rectangle(LeftEnd+B45[0], LeftEnd+B45[1], 0.2, 9.1-Lcorrect, transform="rotate(45)"))
        d.append(draw.Lines(LeftEnd+6, 25, LeftEnd+10, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
    elif Outside == "H": # REDO !!!!!!!!!!!!!!!!!!!!!
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 17, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
        p.arc(LeftEnd + 6, 17, 6, 90, 180)
        d.append(p)
        d.append(draw.Lines(LeftEnd+6, 23, LeftEnd+10, 23, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        d.append(draw.Lines(LeftEnd+10, 23, LeftEnd + 10, 25, close=False, fill='#000000', stroke='black',stroke_width='0.2'))
    elif Outside == "1/4C":
        d.append(draw.Lines(LeftEnd, -12, LeftEnd, 17, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
        p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
        p.arc(LeftEnd, 25, 8, -90, 0)
        d.append(p)
        d.append(draw.Lines(LeftEnd+8, 25, LeftEnd+10, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))

    d.append(draw.Lines(LeftEnd+10, 25, -20, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
    d.append(draw.Text(RailSString, 5, -50 + Numoffset, 30, fill='black'))

    if Type == "Recess":
        if Inside == "Square":
            if Depth == '1/8"':
                depthv = 8
            elif Depth == '3/16"':
                depthv = 10
            elif Depth == '1/4"':
                depthv = 12
            elif Depth == '5/16"':
                depthv = 14
            elif Depth == '3/8"':
                depthv = 16
            d.append(draw.Lines(-20, 25, -20, (25-depthv), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(-20, (25-depthv), 75, (25-depthv), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(-20, 27, -20, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, -5, (25-depthv+3)))
        elif Inside == "45":

            if Depth == '1/8"':
                depthv = 8
                depthy = 2
                deptha = -26
                depthb = 2
            elif Depth == '3/16"':
                depthv = 10
                depthy = 2.25
                deptha = -26
                depthb = 2
            elif Depth == '1/4"':
                depthv = 12
                depthy = 2.5
                deptha = -25
                depthb = 3
            elif Depth == '5/16"':
                depthv = 14
                depthy = 2.75
                deptha = -24
                depthb = 3
            elif Depth == '3/8"':
                depthv = 16
                depthy = 3.1
                deptha = -22
                depthb = 5


            end = -17
            d.append(draw.Rectangle(-3.8, -32, 0.2, depthv+4, transform="rotate(-225)", stroke_width='0.2'))
            xdiff = (math.sin(45) * (depthv+4))
            ydiff = (math.cos(45) * (depthv+4))
            start = -20+xdiff-depthy
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines((-20+xdiff-depthy), (25-ydiff-depthy), 75, (25-ydiff-depthy), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, 1, (25 - depthv + 4)))
            d.append(draw.Text("45°", 5, deptha, (25 - depthv + depthb)))

        elif Inside == "60":

            if Depth == '1/8"':
                depthv = 8
                deptha = -26
                depthb = 0
                deptht = (-14, 14.8)
                depthn = -4
            elif Depth == '3/16"':
                depthv = 10
                deptha = -25
                depthb = 1
                deptht = (-13, 13.1)
                depthn = -3
            elif Depth == '1/4"':
                depthv = 12
                deptha = -25
                depthb = 2
                deptht = (-12, 11.3)
                depthn = -3
            elif Depth == '5/16"':
                depthv = 14
                deptha = -24
                depthb = 3
                deptht = (-11, 9.3)
                depthn = -2
            elif Depth == '3/8"':
                depthv = 16
                deptha = -25
                depthb = 5
                deptht = (-10, 8)
                depthn = 0

            end = -17
            d.append(draw.Rectangle(4.6, -31.7, 0.2, depthv + 4, transform="rotate(-210)", stroke_width='0.2'))
            d.append(draw.Lines(deptht[0], deptht[1], 75, deptht[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = deptht[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, 1, (25 - depthv + 4 + depthn)))
            d.append(draw.Text("60°", 5, deptha, (25 - depthv + depthb)))

        elif Inside == "S45":

            if Depth == '1/8"':
                depthv = 8
                deptha = -21
                depthb = -3
                deptht = (-7.5, 12.5)
                depthn = -5
            elif Depth == '3/16"':
                depthv = 10
                deptha = -22
                depthb = -2
                deptht = (-6.1, 11.1)
                depthn = -5
            elif Depth == '1/4"':
                depthv = 12
                deptha = -21
                depthb = -1
                deptht = (-4.7, 9.7)
                depthn = -3
            elif Depth == '5/16"':
                depthv = 14
                deptha = -19
                depthb = 0
                deptht = (-3.3, 8.3)
                depthn = -3
            elif Depth == '3/8"':
                depthv = 16
                deptha = -20
                depthb = 2
                deptht = (-2, 7)
                depthn = -4

            end = -17
            d.append(draw.Lines(-20, 25, -20, 21, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(-20, 21, -16, 21, close=False, fill='#000000', stroke='black',stroke_width='0.2'))
            d.append(draw.Rectangle(-3.8, -26.2, 0.2, depthv + 4, transform="rotate(-225)", stroke_width='0.2'))
            d.append(draw.Lines(deptht[0], deptht[1], 75, deptht[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = deptht[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, 1, (25 - depthv + 4 + depthn)))
            d.append(draw.Text("45°", 5, deptha, (25 - depthv + depthb)))

        elif Inside == "DS":
            depthn = 0
            if Depth == '1/4"':
                depthv = 12
                depthn = 1
            elif Depth == '3/8"':
                depthv = 16
                depthn = 3

            end = -19
            fD = (-20, (25-(depthv/3)))
            fS = (fD[0]+(depthv/3), fD[1])
            d.append(draw.Lines(-20, 25, -20, 25-(depthv/3), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(fD[0], fD[1], (fD[0]+(depthv/3)), fD[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(fS[0], fS[1], fS[0], fD[1]-(depthv/3), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(fS[0], fD[1]-(depthv/3), 75, fD[1]-(depthv/3), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = fS[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, -6, (25 - depthv + 4 + depthn)))

        elif Inside == "45S45":
            depthn = 0
            if Depth == '1/4"':
                depthv = 3
                fS = (-15, 20.2)
                diff = 5
                depthn = -13
                SRect = (-3.8, -18)
                LFinal = (-5, 10.3)
                deptha = -20
                depthb = -8

            elif Depth == '3/8"':
                depthv = 5
                fS = (-13.8, 19)
                diff = 5
                depthn = -13
                SRect = (-3.8, -16.4)
                LFinal = (-3, 8)
                deptha = -20
                depthb = -8


            end = -17
            d.append(draw.Rectangle(-3.8, -32, 0.2, depthv + 4, transform="rotate(-225)", stroke_width='0.2'))
            d.append(draw.Lines(fS[0], fS[1], fS[0] + diff, fS[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines((fS[0] + diff), fS[1], (fS[0] + diff), (fS[1] - diff), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Rectangle(SRect[0], SRect[1], 0.2, depthv + 4, transform="rotate(-225)", stroke_width='0.2'))
            d.append(draw.Lines(LFinal[0], LFinal[1], 75, LFinal[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = LFinal[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, 2, (25 - depthv + 4 + depthn)))
            d.append(draw.Text("45°", 5, deptha, (25 - depthv + depthb)))

        elif Inside == "F":
            if Depth == '5/16"':
                depthv = 8
                firstlen = (-20.8, 15)
                secondlen = (-9, 25.8)
                virtline = (-9, 17.8)
                depthn = -3
            elif Depth == '3/8"':
                depthv = 10
                firstlen = (-20.8, 12.5)
                secondlen = (-6, 26)
                virtline = (-6, 16)
                depthn = -4


            end = -17
            d.append(draw.Lines(-20, 25, -20, 25 - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(firstlen[0], firstlen[1], depthv, 40, 85)
            p.arc(secondlen[0], secondlen[1], depthv, 225, 270)
            d.append(p)
            d.append(draw.Lines(virtline[0], virtline[1], virtline[0], virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(virtline[0], virtline[1] - (depthv / 4), 75, virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = virtline[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(
                draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, 2, (25 - depthv + 4 + depthn)))

        elif Inside == "H":
            if Depth == '1/8"':
                depthv = 8
                lengthc = 8
                lastc = (-10, 15)
                depthn = -4
            elif Depth == '3/16"':
                depthv = 10
                lengthc = 10
                lastc = (-7.6, 12.5)
                depthn = -4
            elif Depth == '1/4"':
                depthv = 12
                lengthc = 12
                lastc = (-5, 10)
                depthn = -4
            elif Depth == '5/16"':
                depthv = 14
                lengthc = 14
                lastc = (-2.5, 7.5)
                depthn = -4
            elif Depth == '3/8"':
                depthv = 16
                lengthc = 16
                lastc = (0, 5)
                depthn = -6

            end = -17
            d.append(draw.Lines(-20, 25, -20, 25-(depthv/4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(-20, 25-(depthv/4), -20+(depthv/4), 25-(depthv/4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(-20+(depthv/4), 25-(depthv/4) - lengthc, depthv, 0, 90)
            d.append(p)
            d.append(draw.Lines(lastc[0], lastc[1], 75, lastc[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = lastc[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(
                draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, 2, (25 - depthv + 4 + depthn)))




        elif Inside == "SQ45":
            if Depth == '1/8"':
                depthv = 8
                depthn = -4
                deptha = -23
                depthb = 4
            elif Depth == '3/16"':
                depthv = 10
                depthn = -4
                deptha = -23
                depthb = 6
            elif Depth == '1/4"':
                depthv = 12
                depthn = -4
                deptha = -23
                depthb = 8
            elif Depth == '5/16"':
                depthv = 14
                depthn = -4
                deptha = -23
                depthb = 10
            elif Depth == '3/8"':
                depthv = 16
                depthn = -4
                deptha = -23
                depthb = 12

            d.append(draw.Lines(-17, 22, -17, (22 - depthv), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Rectangle(-3.7, -31.9, 0.2, 4.5, transform="rotate(-225)", stroke_width='0.2'))
            d.append(draw.Lines(-17, (22 - depthv), 75, (22 - depthv), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = -17
            end = -19
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text(Depth, 5, -7, (25 - depthv + 4 + depthn)))
            d.append(draw.Text("45°", 3, deptha, (25 - depthv + depthb)))



    elif Type == "Raised":
        if Inside == "6060":
            depthv = 12
            deptha = -25
            depthb = 2
            deptht = (-12, 11.3)
            depthn = -3

            end = -17
            d.append(draw.Rectangle(4.6, -31.7, 0.2, depthv + 4, transform="rotate(-210)", stroke_width='0.2'))
            d.append(draw.Lines(deptht[0], deptht[1], depthv, deptht[1], close=False, fill='#000000', stroke='black',stroke_width='0.2'))
            start = deptht[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text('1/4"', 5, -4, (25 - depthv + 4 + depthn)))
            d.append(draw.Text("60°", 5, deptha, (25 - depthv + depthb)))
            d.append(draw.Rectangle(4.6, 15.7, 0.2, depthv + 4, transform="rotate(30)", stroke_width='0.2'))
            d.append(draw.Lines(20, 25, 75, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text("60°", 5, 18, (25 - depthv + 2)))



        elif Inside == "6045":
            depthv = 12
            deptha = -25
            depthb = 2
            deptht = (-12, 11.3)
            depthn = -3

            end = -17
            d.append(draw.Rectangle(4.6, -31.7, 0.2, depthv + 4, transform="rotate(-210)", stroke_width='0.2'))
            d.append(draw.Lines(deptht[0], deptht[1], depthv, deptht[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = deptht[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text('5/8"', 5, -4, (25 - depthv + 4 + depthn)))
            d.append(draw.Text("60°", 5, deptha, (25 - depthv + depthb)))
            d.append(draw.Rectangle(0.3, 16.3, 0.2, depthv + 1, transform="rotate(45)", stroke_width='0.2'))
            d.append(draw.Lines(21, 20.4, 25.5, 20.4, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(25.5, 20.4, 25.5, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(25.5, 25, 75, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text("45°", 5, 18, (25 - depthv - 1)))

        elif Inside == "FF":
            depthv = 10
            firstlen = (-20.8, 12.5)
            secondlen = (-6, 26)
            virtline = (-6, 16)
            depthn = -4

            end = -17
            d.append(draw.Lines(-20, 25, -20, 25 - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(firstlen[0], firstlen[1], depthv, 40, 85)
            p.arc(secondlen[0], secondlen[1], depthv, 225, 270)
            d.append(p)
            d.append(draw.Lines(virtline[0], virtline[1], virtline[0], virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(virtline[0], virtline[1] - (depthv / 4), 18, virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = virtline[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text('7/8"', 5, 2, (25 - depthv + 4 + depthn)))
            d.append(draw.Lines(18, virtline[1], 18, virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(32.7, firstlen[1], depthv, 95, 140)
            p.arc(18, secondlen[1], depthv, 270, 315)
            d.append(p)
            d.append(draw.Lines(32, 22.4, 32, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(32, 25, 75, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))

        elif Inside == "HH":
            depthv = 14
            lengthc = 14
            lastc = (-2.5, 7.5)
            depthn = -4

            end = -17
            d.append(draw.Lines(-20, 25, -20, 25 - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(-20, 25 - (depthv / 4), -20 + (depthv / 4), 25 - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(-20 + (depthv / 4), 25 - (depthv / 4) - lengthc, depthv, 0, 90)
            d.append(p)
            d.append(draw.Lines(lastc[0], lastc[1], 20, lastc[1], close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = lastc[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text('7/8"', 5, 5, (25 - depthv + 4 + depthn)))

            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(34, 25 - (depthv / 4) - lengthc, depthv, 90, 180)
            d.append(p)

            d.append(draw.Lines(34, 25 - (depthv / 4), 34 + (depthv / 4), 25 - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(34 + (depthv / 4), 25 - (depthv / 4), 34 + (depthv / 4), 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(34 + (depthv / 4), 25, 75, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))

        elif Inside == "F15":
            depthv = 10
            firstlen = (-20.8, 12.5)
            secondlen = (-6, 26)
            virtline = (-6, 16)
            depthn = -4

            end = -17
            d.append(draw.Lines(-20, 25, -20, 25 - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            p = draw.Path(fill='none', stroke='black', stroke_width='0.2')
            p.arc(firstlen[0], firstlen[1], depthv, 40, 85)
            p.arc(secondlen[0], secondlen[1], depthv, 225, 270)
            d.append(p)
            d.append(draw.Lines(virtline[0], virtline[1], virtline[0], virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(virtline[0], virtline[1] - (depthv / 4), 20, virtline[1] - (depthv / 4), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            start = virtline[0]
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text('1.125"', 5, 2, (25 - depthv + 4 + depthn)))

            d.append(draw.Rectangle(-8, 22.4, 0.2, depthv + 35, transform="rotate(75)", stroke_width='0.2'))
            d.append(draw.Lines(63, 25, 75, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))

        elif Inside == "FA":  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print("fa")

        elif Inside == "45G45":
            depthv = 16
            depthy = 3.1
            deptha = -22
            depthb = 5

            end = -17
            d.append(draw.Rectangle(-3.8, -32, 0.2, depthv + 4, transform="rotate(-225)", stroke_width='0.2'))
            xdiff = (math.sin(45) * (depthv + 4))
            ydiff = (math.cos(45) * (depthv + 4))
            start = -20 + xdiff - depthy
            jset = end - start
            jest = start + abs(jset)
            d.append(draw.Lines((-20 + xdiff - depthy), (25 - ydiff - depthy), 18, (25 - ydiff - depthy), close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(end, 25, jest, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(LeftEnd, 27, LeftEnd, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(start, 27, start, 37, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Text('5/8"', 5, 1, (25 - depthv + 4)))
            d.append(draw.Text("45°", 5, deptha, (25 - depthv + depthb)))

            d.append(draw.Rectangle(4.5, 20.7, 0.2, depthv - 2, transform="rotate(45)", stroke_width='0.2'))
            d.append(draw.Lines(27.8, 21.3, 32, 21.3, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(32, 21.3, 32, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))
            d.append(draw.Lines(32, 25, 75, 25, close=False, fill='#000000', stroke='black', stroke_width='0.2'))

            d.append(draw.Text("45°", 5, 26, (25 - depthv + depthb)))

    if BackList != []:
        BackInside = BackList[0]
        BackDepth = BackList[1]
        BackRailS = BackList[2]

        if BackRailS <= 1:
            if LeftEnd == -60:
                d.append(draw.Lines(LeftEnd, -12, -20, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))
                start = LeftEnd
                end = -45

        elif BackRailS <= 2:
            d.append(draw.Lines(LeftEnd, -12, -30, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))
            start = LeftEnd
            end = -30

        elif BackRailS <= 2.25:
            d.append(draw.Lines(LeftEnd, -12, -27.5, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))
            start = LeftEnd
            end = -27.5

        elif BackRailS <= 2.5:
            d.append(draw.Lines(LeftEnd, -12, -25, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))
            start = LeftEnd
            end = -25

        elif BackRailS <= 3:
            d.append(draw.Lines(LeftEnd, -12, -15, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))
            start = LeftEnd
            end = -15

        elif BackRailS > 3:
            d.append(draw.Lines(LeftEnd, -12, -9, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))
            start = LeftEnd
            end = -9


        if BackInside == "Straight":
            print("tr")









    else:
        d.append(draw.Lines(75, -12, LeftEnd, -12, close=False, fill='#eeee00', stroke='black', stroke_width='0.2'))







BackList = []
#Type = input("Recess, Raised:")
#Back = input("Back Pocket? True or False:")
# if Back == "False":
#     Back = False
# elif Back == "True":
#     Back = True
# if Back:
#     BackInside = input("BInside: Straight, 45, 60:")
#     BackDepth = input("BDepth: 1/8, 3/16, 1/4:")
#     BackRailS = input("BRS: 1, 2, 2.25, 2.5, 3, other can be rearranged later:")
#     BackList.append(BackInside)
#     BackList.append(BackDepth)
#     BackList.append(BackRailS)
#Inside = input("Inside: Square, 45, 60, S45, DS, 45S45, F, H, SQ45:")
#Outside = input("Outside: Square, 1/16R, 1/8R, 1/4R, 45B, H, 1/4C:")
#Depth = input('Depth: 1/8", 3/16", 1/4", 5/16", 3/8":')
#RailS = input('RS: 1", 2", 2.25", 2.5", 3", other can be rearranged later:')
#Glass = input("Glass: True or False:")
#Glass = bool(Glass)


Inside = "45S45"
Depth = '3/8"'
RailS = 1
Glass = False
Type = "Recess"
BackList = ["Straight", '1/8"', 3]
Outside = "1/16R"

InsideOp = ['45', 'Square', '60', 'S45', 'DS', '45S45', 'SQ45', '6060', '6045', 'FF', 'F', 'H']
OutsideOp = ["Square", "1/16R", "1/8R", "1/4R", "45B", "H", "1/4C"]
TypeOp = ["Recess", 'Raised']
RailSOp = [1, 2, 2.25, 2.5, 3, 4.2]  # Other == 4.2 for now
BackOp = []
GlassOp = False
DepthOp = ['1/8"', '3/16"', '1/4"', '5/16"', '3/8"']

# Make default setting and update live

# TO SCALE

Inch = 40
te = 0.375

cm = Inch/2.54

# ## TEST MODULE
# for t in TypeOp:
#     for i in InsideOp:
#         for o in OutsideOp:
#             for r in RailSOp:
#                 for D in DepthOp:
#                     d = draw.Drawing(200, 100, origin='center', displayInline=False)
#                     build(t, i, o, D, r, GlassOp, BackOp)
#                     savestring = str(TypeOp.index(t)) + str(InsideOp.index(i)) + str(OutsideOp.index(o)) + str(RailSOp.index(r)) + str(DepthOp.index(D)) + '.svg'
#                     d.saveSvg("SVGS/" + savestring)


d = draw.Drawing(200, 100, origin='center', displayInline=False)
build(Type, Inside, Outside, Depth, RailS, Glass, BackList)
d.saveSvg('example.svg')


# I can't do live updating, but I can use this script to create every different possible possiblility,
# and number them to easiely fetch them then I am able to just us JS and a web server to server each one live as a
# var is changed.

# Live updating can work, but it will have to load after every change which may not be wanted. Above is still better
# option


